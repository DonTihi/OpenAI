from openai import OpenAI
import sys


def openai():
    client = OpenAI(
        api_key=sys.argv[1],
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Translate into Spanish: As a beginner data scientist, I'm excited to learn about OpenAI API!"}
        ]
    )
    output = response.choices[0].message.content

    return output


if __name__ == '__main__':
    print(openai())

