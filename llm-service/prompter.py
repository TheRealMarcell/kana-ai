import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

message = [
    {
        "role": "developer",
        "content": [
            {
                "type": "text",
                "text": """
                        You are a language assistant that will provide the user mnemonics to memorise the given kanji.
                        Based on the instruction, you will either provide a meaning mnemonic to help the user 
                        internalise and memorise the kanji meaning, or the reading mnemonic to help the user understand
                        how to sound out the word and say it (both on'yomi and kun'yomi readings).
                        
                        Assume the user has knowledge of the 'radicals' or building blocks that make up the kanji that 
                        is being questioned.
                        
                        You will output it in the following format:
                        mnemonic text here
                        """
            }
        ]
     },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Meaning mnemonic for 批"
            }
        ]
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=message
)

print(response.choices[0].message.content)

