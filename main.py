import openai

openai.api_key = ""  # Insert your own API key here


def gpt_chat_bot(msg):
    answer = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": msg}]
    )

    return answer.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("Your input to ChatGPT: ")

        if user_input == "q":
            break

        response = gpt_chat_bot(user_input)
        print(f"Chatbot: {response}")
