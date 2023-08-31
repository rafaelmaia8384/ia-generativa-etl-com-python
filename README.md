# Desafio do módulo Explorando IA Generativa em um Pipeline de ETL com Python
## Dio


## O que esse projeto faz
Dado um arquivo dados.csv contendo informacões sobre pessoas, o projeto faz a leitura das informacões usando o package pandas e as envia para a API da OpenAI para obter um resumo sobre a pessoa em questão. Logo após o app salva as informacões no arquivo resumos.json.

## Pré requisitos
Para rodar esse projeto, crie um arquivo .env na raíz do repositório e defina a variável de ambiente com a api_key da openai

## Como rodar
```
pip install -r requirements.txt
python main.py
```