import openai
import os

# Set your OpenAI API key (using environment variable is safer)
openai.api_key = os.getenv(
    "OPENAI_API_KEY") or "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"


def chat_with_gpt():
    print("ChatGPT is ready! Type 'exit' to quit.\n")

    conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

        client = openai.OpenAI()  # Create client instance

while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break

            conversation.append({"role": "user", "content": user_input})

            # Updated API call for v1.0.0+
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation
            )

            reply = response.choices[0].message.content.strip()
            conversation.append({"role": "assistant", "content": reply})
            print(f"ChatGPT: {reply}\n")

        except openai.AuthenticationError:
            print("Error: Invalid API key or authentication failed")
            break
        except openai.RateLimitError:
            print("Error: Rate limit exceeded. Please try again later.")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    chat_with_gpt()
