import os
import requests
import json

PROMPT = """Receba a User Story abaixo e a divida em cards, cada um com seu título e descrição, para um quadro Kanban.

Regras:
- Use somente informações presentes na User Story.
- Não invente prazos, horas ou responsáveis.
- Para cada card, use exatamente este formato:

Card N
Título: ...
Descrição: ...

Aqui está a User Story:
{user_story}"""


def gerar_texto(user_story):
    base_url = os.environ.get("LLM_BASE_URL")
    modelo = os.environ.get("LLM_MODEL")

    # Sem as variáveis definidas (localmente), devolve uma resposta falsa
    if not base_url or not modelo:
        return "Card 1\nTítulo: Resposta falsa\nDescrição: LLM_BASE_URL ou LLM_MODEL não definida."

    prompt_final = PROMPT.format(user_story=user_story)

    dados = {
        "model": modelo,
        "prompt": prompt_final,
        "stream": True,
        "think": False,
    }

    resposta = requests.post(base_url + "/api/generate", json=dados, timeout=180, verify=False, stream=True)

    resposta.raise_for_status()

    texto = ""
    for linha in resposta.iter_lines():
        if not linha:
            continue
        pedaco = json.loads(linha)
        texto += pedaco.get("response", "")
        if pedaco.get("done"):
            break

    return texto