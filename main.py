import os
import json
import pandas as pd
import openai
from dotenv import load_dotenv

load_dotenv(".env")

openai.api_key = os.getenv("OPENAI_API_KEY")

functions = [
    {
        "name": "generate_person_resume",
        "description": "Geração de resumo sobre a vida de uma pessoa.",
        "parameters": {
            "type": "object",
            "properties": {
                "resume": {
                    "type": "string",
                    "description": "Resumo da vida de uma pessoa de acordo com os dados fornecidos.",
                },
            },
            "required": [
                "resume",
            ],
        },
    }
]


def get_user_resume(data):
    messages = [
        {
            "role": "system",
            "content": "Você é uma IA que ajuda a resumir a história de vida de pessoas.",
        },
        {
            "role": "user",
            "content": "Faça um resumo de no máximo 300 caracteres de acordo com esses dados:\n\n"
            + data,
        },
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        functions=functions,
        messages=messages,
        function_call={"name": "generate_person_resume"},
    )
    result = json.loads(response.choices[0]["message"]["function_call"]["arguments"])
    return result["resume"]


print("Lendo dados.csv...")
df = pd.read_csv("dados.csv")
resumos = []

for _, row in df.iterrows():
    print(f"Gerando resumo para {row['nome']}...")
    row_dict = row.to_dict()
    row_str = json.dumps(row_dict)
    resume = get_user_resume(row_str)
    resumos.append(
        {
            "nome": row_dict["nome"],
            "resumo": resume,
        }
    )

print("Salvando resumos.json ...")
df_resumos = pd.DataFrame(resumos)
df_resumos.to_json("resumos.json", orient="records")

print("Done!")
