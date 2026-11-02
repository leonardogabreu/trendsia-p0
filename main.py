#!/usr/bin/env python3
from llm_client import gerar_texto

print("Escreva uma User Story (Título + Descrição): \n")

user_story = input()

cards = gerar_texto(user_story)
print(cards)