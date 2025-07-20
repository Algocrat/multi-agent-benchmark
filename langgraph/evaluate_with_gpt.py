import openai
import os

openai.api_key = "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"  # Replace with your key

rubric = """
You are a content evaluator. Score the following text on a scale of 0–5 across:
1. Accuracy
2. Completeness
3. Coherence
4. Readability
5. Citation Use
6. Insightfulness

Respond in JSON format.
"""

outputs_dir = "outputs"
for filename in os.listdir(outputs_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(outputs_dir, filename), "r") as f:
            content = f.read()

        prompt = f"{rubric}\n\nContent:\n{content}"

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        score_output = response.choices[0].message.content
        with open(os.path.join(outputs_dir, f"{filename}_score.json"), "w") as f:
            f.write(score_output)

        print(f"Scored: {filename}")
