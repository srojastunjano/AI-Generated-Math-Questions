from flask import Flask, render_template, request
import os
import openai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__) # os is being used to retrieve the environment-variable: OpenAI API key. 

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY 

@app.route('/', methods=["GET", "POST"])
def index():
    gpt_answer = "No Answer yet"
    if request.method == 'POST':
      completion = openai.ChatCompletion.create(   #the completion variable hold the JSON responce that the ChatGPT API recieves
        model="gpt-3.5-turbo",
        temperature = 0.8,
        messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": request.form["user_input"]}
        ]
      )
      print(completion)
      gpt_answer = completion["choices"][0]["message"]["content"]
      

    return render_template('main.html', gpt_answer=gpt_answer)

app.run()
