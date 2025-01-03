from openai import OpenAI
client = OpenAI(
    api_key= "OPEN AI API KEY",
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a Virtual assitant known as Jarvis skilled in general tasks like alexa and google cloud."},
        {
            "role": "user",
            "content": "Write  about  programming."
        }
    ]
)
print(completion.choices[0].message.content)