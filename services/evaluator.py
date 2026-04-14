from common.llm.ollama_client import generate

def evaluate_answer(question, answer, context):
    prompt = f"""
    Evaluate answer quality (0-10):

    Question: {question}
    Answer: {answer}
    Context: {context}

    Give score and reason.
    """

    return generate(prompt)