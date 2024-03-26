from openai import OpenAI
import sys

def openAI():
    client = OpenAI(
        api_key=sys.argv[1],
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    return (print(completion.choices[0].message))


if __name__ == '__main__':
    openAI()

