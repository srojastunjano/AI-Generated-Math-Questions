from flask import Flask, render_template, request
import os
import openai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__) # os is being used to retrieve the environment-variable: OpenAI API key. 

openai_api_key = os.getenv("OPENAI_API_KEY")
organization_id = os.getenv("ID")

completion = openai.ChatCompletion.create(   #the completion variable hold the JSON responce that the ChatGPT API recieves
    model="gpt-3.5-turbo",
    temperature = "0.8",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ]
  )
ChatGPT = completion["messages"][0]["content"]
user_input = completion["messages"][1]["content"]

@app.route("/", methods=["POST"])
def index():

    if request.method == 'POST':
        user_input = request.form["user"]
        return render_template("main.html", ChatGPT=ChatGPT, user_input=user_input)
  
app.run(host="0.0.0.0", port=5000)


#Example of the responce I would get from ChatGPT API
# {   
#   "id": "chatcmpl-123",
#   "object": "chat.completion",
#   "created": 1677652288,
#   "model": "gpt-3.5-turbo-0613",
#   "choices": [{
#     "index": 0,
#     "message": {
#       "role": "assistant",
#       "content": "\n\nHello there, how may I assist you today?",
#     },
#     "finish_reason": "stop"
#   }],
#   "usage": {
#     "prompt_tokens": 9,
#     "completion_tokens": 12,
#     "total_tokens": 21
#   }