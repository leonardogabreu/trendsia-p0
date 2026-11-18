#!/usr/bin/env python3
import sys

from gerador_cards.llm_client import gerar_texto

print("Digite a User Story. Para terminar, aperte Ctrl+D numa linha vazia:\n")

user_story = sys.stdin.read().strip()

if user_story == "":
    print("Erro: nenhuma User Story foi informada.")
    sys.exit(1)

print(gerar_texto(user_story))