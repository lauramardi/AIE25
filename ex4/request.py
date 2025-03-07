import requests
import pandas as pd

df = pd.read_csv('job_postings.csv')

url = "http://127.0.0.1:5000/process/"


for description in df['job_description']:
    data = {"value": description}
    response = requests.post(url, json=data)
    print(response.json())

