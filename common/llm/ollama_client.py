import ollama

def generate(prompt, model="llama3"):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": "Answer based only on provided context."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']