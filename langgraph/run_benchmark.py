import time
import subprocess
import signal
import os
from graph_template import create_graph
from langchain_community.chat_models import ChatOllama

models = {
    "mistral": "mistral",
    "llama3": "llama3",
    "phi3": "phi3"
}

for model_name, model_id in models.items():
    print(f"\n Starting Ollama model: {model_id}")
    proc = subprocess.Popen(
        ["ollama", "run", model_id],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        preexec_fn=os.setsid  # allow group kill
    )

    print("Waiting for model to become responsive...")
    time.sleep(10)  # give the model some time to warm up

    try:
        print(f"Running LangGraph with model: {model_name}")
        llm = ChatOllama(model=model_id)
        graph = create_graph(llm)

        start_time = time.time()
        result = graph.invoke({"current_section": "The Future of Work in an AI World"})
        end_time = time.time()

        os.makedirs("outputs", exist_ok=True)
        output_path = f"outputs/{model_name}.txt"
        with open(output_path, "w") as f:
            f.write(result.get("final_report", "[No output generated]"))
            f.write(f"\n\n---\nExecution Time: {end_time - start_time:.2f} seconds")

        print(f"Output saved to: {output_path}")

    except Exception as e:
        print(f"Error during {model_id} execution:", str(e))

    finally:
        print(f"Stopping model: {model_id}")
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        time.sleep(2)

