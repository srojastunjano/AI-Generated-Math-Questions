from flask import Flask, render_template
import os
import openai
# import json
# import requests


app = Flask(__name__)
openai.organization = "org-yZ9iYd4rWaYlLEfWMT6sYE3s"
openai.api_key = os.getenv("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") # os is being used to retrieve the environment-variable: OpenAI API key. 

completion = openai.ChatCompletion.create(   #the completion variable hold the JSON responce that the ChatGPT API recieves
    model="gpt-3.5-turbo",
    temperature = "0.8",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ]
  )

@app.route("/")
def index():
    chatgpt = completion["messages"][0]["content"]
    user = completion["messages"][1]["content"]
    return render_template("main.html", chatgpt=chatgpt, user=user )

app.run(host="0.0.0.0", port=5000)

print(completion.choices[0].message)

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