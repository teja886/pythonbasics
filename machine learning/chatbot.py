import openai
from pyexpat.errors import messages

openai.api_key="AIzaSyBFoHHMKRYkpK0Ca3DGQ5SItZDhFh2EJt8"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gemini-1.5-pro",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit","exist","bye"]:
            break

        response = chat_with_gpt(user_input)
        print("chatbox: ",response)