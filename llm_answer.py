from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def generate_answer(question, context):
    result = qa_pipeline({
        'context': context,
        'question': question
    })
    return result['answer']