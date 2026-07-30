from retrieval_engine import retrieve
from llm import generate_answer

def retrieve_and_answer(question):
    context = retrieve(question)
    answer = generate_answer(question, context)
    return answer