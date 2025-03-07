from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

def get_details(job_posting):
   qa_pipeline = pipeline("question-answering")

   context = job_posting
   question1 = 'What is the salary range?'
   question2 = 'What is the job title?'
   question3 = 'What is the location?'

   salary = qa_pipeline(question=question1, context=context)['answer']
   title = qa_pipeline(question=question2, context=context)['answer']
   location = qa_pipeline(question=question3, context=context)['answer']

   return {'Salary': salary, 'Job title':title, 'Location': location}


@app.route("/process/", methods=["POST"])
def process():
    data = request.get_json()
    result = get_details(data["value"])
    return jsonify({"input": data["value"], "result": result})

if __name__ == "__main__":
    app.run(debug=True)