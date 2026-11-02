prompt = """Receba a User Story abaixo e a divida em cards, cada um com seu título e descrição, para um quadro Kanban.

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
    txt = f"Card 1\nTítulo: Título 1\nDescrição: {user_story}"
    return txt