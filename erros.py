class ErroP0(Exception):
    """Base de todos os erros previstos do projeto. A mensagem já é escrita para o usuário."""


class EntradaVazia(ErroP0):
    pass


class ConfiguracaoInvalida(ErroP0):
    pass


class CredencialAusente(ErroP0):
    pass


class CredencialInvalida(ErroP0):
    pass


class LLMIndisponivel(ErroP0):
    pass


class FalhaDeComunicacao(ErroP0):
    pass


class TempoEsgotado(ErroP0):
    pass


class RespostaInvalida(ErroP0):
    pass