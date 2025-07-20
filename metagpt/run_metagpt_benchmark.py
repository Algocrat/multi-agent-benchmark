# run_metagpt_benchmark.py (clean version – no config2 dependency)

import os
import time
from langchain_ollama import ChatOllama

models = os.getenv("OLLAMA_MODELS", "llama3,mistral,phi3").split(",")

class Message:
    def __init__(self, content: str):
        self.content = content

class Planner:
    def _act(self, msg: Message) -> Message:
        sections = [
            "Impact of AI on white-collar jobs",
            "Future of remote work with AI",
            "AI and automation in blue-collar sectors",
            "Policy & ethical challenges"
        ]
        result = "\n".join(sections)
        print(f"📝 Sections:\n{result}")
        return Message(content=result)

class Researcher:
    def __init__(self, llm):
        self.llm = llm

    def _act(self, msg: Message) -> Message:
        section = msg.content
        prompt = f"As a Researcher, write a 300-word analysis on: {section}"
        result = self.llm.invoke(prompt).content.strip()
        print(f"\n🧠 [{section}] Analysis (first 300 chars):\n{result[:300]}\n")
        return Message(content=result)

class Composer:
    def _act(self, msg: Message) -> Message:
        input_str = msg.content
        parts = input_str.split("|||", 1)
        sections = parts[0].strip().split("\n")
        analyses = parts[1].strip().split("|||")

        if len(sections) != len(analyses):
            raise ValueError("Mismatch between section and analysis counts.")

        report = ["# The Future of Work in an AI World\n"]
        for s, a in zip(sections, analyses):
            report.append(f"## {s}\n{a}\n")

        return Message(content="\n".join(report))

def run_metagpt_for_model(model_name):
    print(f"\n🚀 Running MetaGPT-style benchmark for: {model_name}")
    start = time.time()

    llm = ChatOllama(
        model=model_name,
        temperature=0.7,
        max_tokens=2048,
        streaming=True
    )

    planner = Planner()
    researcher = Researcher(llm)
    composer = Composer()

    try:
        planner_output = planner._act(Message(content="Start Planning")).content

        section_list = planner_output.split("\n")
        analysis_outputs = [
            researcher._act(Message(content=sec)).content for sec in section_list
        ]

        joined = planner_output + "|||" + "|||".join(analysis_outputs)
        final_report = composer._act(Message(content=joined)).content

        elapsed = time.time() - start
        os.makedirs("outputs", exist_ok=True)
        out_path = f"outputs/metagpt_ollama_{model_name}.txt"
        with open(out_path, "w") as f:
            f.write(final_report)
            f.write(f"\n\nExecution Time: {elapsed:.2f} seconds")

        print(f"\n✅ Done for {model_name}. Report saved to: {out_path}")

    except Exception as e:
        print(f"❌ Error for {model_name}: {e}")

if __name__ == "__main__":
    for model in models:
        run_metagpt_for_model(model)

