import sys
import time
import os
from crewai import Crew, Agent, Task
from langchain_ollama import ChatOllama

if len(sys.argv) != 2:
    print("Usage: python run_crewai_benchmark.py <ollama/model>")
    sys.exit(1)

model = sys.argv[1]
llm = ChatOllama(model=model)

planner = Agent(
    role='Planner',
    goal='Define and organize the workflow sections that will be processed',
    backstory='Expert in structuring reports and creating clear outlines.',
    verbose=True,
    llm=llm
)

researcher = Agent(
    role='Researcher',
    goal='Perform research and content generation for each section',
    backstory='Expert in detailed analysis and information synthesis.',
    verbose=True,
    llm=llm
)

composer = Agent(
    role='Composer',
    goal='Aggregate and compile research outputs into a final structured report',
    backstory='Skilled editor and writer specializing in coherent document assembly.',
    verbose=True,
    llm=llm
)

task_planner = Task(
    description=(
        "Produce a list of sections for the report titled "
        "'The Future of Work in an AI World': "
        "1) Impact of AI on white‑collar jobs, "
        "2) Future of remote work with AI, "
        "3) AI and automation in blue‑collar sectors, "
        "4) Policy & ethical challenges."
    ),
    agent=planner,
    expected_output="A bullet-list of the four section titles."
)

task_researcher = Task(
    description=(
        "For each section listed, write a standalone 300‑word analysis. "
        "Input will be the list of section titles."
    ),
    agent=researcher,
    expected_output="A dict mapping each section title to its 300‑word analysis."
)

task_composer = Task(
    description=(
        "Take the analyses produced for each section and combine them "
        "into one cohesive report, with headings and transitions."
    ),
    agent=composer,
    expected_output="A single markdown document stitching all four analyses."
)

crew = Crew(
    agents=[planner, researcher, composer],
    tasks=[task_planner, task_researcher, task_composer],
    process="sequential",
    verbose=True
)

os.makedirs("outputs", exist_ok=True)
start = time.time()
result = crew.kickoff()
end = time.time()

# Convert result to string before writing
output_text = str(result)

output_file = f"outputs/crewai_{model.replace('/', '_')}_full_report.txt"
with open(output_file, "w") as f:
    f.write(output_text)
    f.write(f"\n\nExecution Time: {end - start:.2f} seconds")

print(f"Benchmark complete for {model}. Full report saved to {output_file}")

