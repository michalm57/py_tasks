from transformers import pipeline
question_answerer = pipeline("question-answering", model="clarin-knext/herbert-large-poquad")
question="Co lubi pies"
context = "Pies lubi mleko"
result = question_answerer(question=question, context=context)
print(result)