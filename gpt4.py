import openai
import json
from dotenv import load_dotenv

# Load .env file
load_dotenv()


MODEL = "gpt-3.5-turbo"

while True:
    # Deserializing the list of dictionaries from the file
    with open('history.txt', 'r') as file:
        deserialized_messages = json.load(file)


    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=deserialized_messages,
        temperature=0,
        max_tokens=128
    )

    # Writing the serialized string to a file
    deserialized_messages.append(response.choices[0].message)
    with open('history.txt', 'w') as file:
        file.write(json.dumps(deserialized_messages))

    print(response)