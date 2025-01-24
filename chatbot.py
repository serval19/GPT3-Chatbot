import openai
def askgpt(text):
    openai.api_key="Openai key here"
    response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        temperature=0.6,
        max_tokens=150
    )
    return print(response.choices[0].text)
def main():
    while True:
        print("GPT: Ask me a Question:\n")
        q=input()
        askgpt(q)
        print("\n")
main()



