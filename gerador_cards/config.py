import os
from dataclasses import dataclass, field

from gerador_cards.erros import ConfiguracaoInvalida


@dataclass
class Configuracao:
    base_url: str
    modelo: str
    api_key: str | None = field(default=None, repr=False)


def carregar_configuracao():
    base_url = os.environ.get("LLM_BASE_URL", "").strip()
    modelo = os.environ.get("LLM_MODEL", "").strip()
    api_key = os.environ.get("LLM_API_KEY", "").strip() or None

    if not base_url:
        raise ConfiguracaoInvalida("A variável LLM_BASE_URL não foi definida. Veja o .env.example.")
    if not base_url.startswith(("http://", "https://")):
        raise ConfiguracaoInvalida(
            f"LLM_BASE_URL precisa começar com http:// ou https:// (valor atual: {base_url})."
        )
    if not modelo:
        raise ConfiguracaoInvalida("A variável LLM_MODEL não foi definida. Veja o .env.example.")

    return Configuracao(base_url=base_url.rstrip("/"), modelo=modelo, api_key=api_key)