from boltiotai import openai
import os


question = input("Q: what is your question/instruction?\n")
while True:

    openai.api_key = os.environ['OPENAI_API_KEY']

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": "Who won the world series in 2020?"
        }, {
            "role":
            "assistant",
            "content":
            "The Los Angeles Dodgers won the World Series in 2020."
        }, {
            "role": "user",
            "content": question
        }])

    output = response['choices'][0]['message']['content']

    print("\n Ans", output, "\n")
    question = input("Q: what is your next question/instruction?\n")
