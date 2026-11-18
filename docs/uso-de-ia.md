# Uso de IA no projeto

Este documento registra como usei ferramentas de IA durante o P0.

## Como a IA foi usada

- **Ferramentas:** Claude (no navegador) no início do projeto; depois, Claude Code (app desktop).
- **Papel da IA:** tutor. Ela explica conceitos, aponta erros, revisa o que escrevi e dá dicas.
- **O que a IA não faz:** escrever ou editar o código do projeto. Todo o código é escrito por mim.
- **Segurança:** a IA não lê nem mostra o arquivo `.env` com as chaves.

## Registro

| Data | Ferramenta | O que pedi | O que fiz com isso |
|---|---|---|---|
| Antes de 02/11/2026 | Claude (navegador) | Ajuda para entender o problema e planejar a solução: escopo, estrutura de arquivos, formato de saída dos cards e uso de variáveis de ambiente. | Defini as decisões do projeto (só título e descrição nos cards, chamada ao LLM isolada em `llm_client.py`, saída com marcadores) e escrevi a estrutura inicial e os exemplos. |
| 02/11/2026 | Claude Code | Conferir se o `.venv` estava na pasta certa e fora do Git. | A IA confirmou que estava certo e apontou que meus arquivos estavam com `git add`, mas sem commit. Fiz o commit e o PR. |
| 12/11/2026 | Claude Code | Priorizar os módulos do curso de Python e estimar o prazo do P0. | Decidi fazer o módulo de JSON antes de voltar ao projeto. |
| 14/11/2026 | Claude Code | Relembrar o estado do projeto e o que falta fazer. Pedi para a IA manter este registro. | Revisei o plano para continuar o nível básico. |
| 14/11/2026 | Claude Code | Revisar minha leitura de User Story com várias linhas e entender o guia do LLM institucional (Ollama em container Docker). | A IA testou meu código e apontou dois problemas (quebras de linha perdidas e erro ao ler de arquivo), sem corrigir por mim. Defini os próximos passos. |
| 14/11/2026 | Claude Code | Pedi explicações diretas com o código correto (em vez de dicas) e ajuda para aprender Docker e instalá-lo. | A IA explicou o que é Docker, variáveis de ambiente e portas, e mostrou o código da leitura da entrada, da chamada ao Ollama e do Dockerfile, para eu digitar e testar. |
| 14/11/2026 | Claude Code | Entender o erro `No module named 'pip'` ao instalar o `requests`. | A IA descobriu que o Ubuntu foi atualizado (Python 3.12 → 3.14) e o `.venv` antigo quebrou. Instalei o `python3-venv` e recriei o `.venv`. |
| 14/11/2026 | Claude Code | Entender o aviso do Pylance sobre o `requests`, o campo de porta obrigatório da plataforma, e o que cada comando (apt, venv, pip, docker build/run/save) faz. | A IA revisou meu `llm_client.py` e apontou um trecho duplicado que sobrescrevia o prompt. Corrigi, refiz a imagem e entendi os comandos que estou usando. |
| 14/11/2026 | Claude Code | Entender o erro dos Logs do primeiro container na plataforma. | A IA explicou como ler o traceback e que o erro era o certificado HTTPS autoassinado do servidor (o LLM estava no ar). Desliguei a verificação do certificado temporariamente para testar, sabendo que é inseguro e precisa ser trocado depois. |
| 14/11/2026 | Claude Code | Entender o erro `502 Bad Gateway` no segundo teste. | A IA explicou que o LLM leva 1–2 minutos para ligar depois que o container inicia, e meu programa chamava antes disso. Coloquei uma espera no `CMD` do Dockerfile para testar. |
| 14/11/2026 | Claude Code | Entender o erro `504 Gateway Timeout` no terceiro teste. | A IA mostrou, pelos horários dos Logs, que o proxy desiste depois de ~30 s, e explicou o modo *streaming* do Ollama (resposta em pedaços, um JSON por linha). Mudei a chamada para usar streaming. |
| 14/11/2026 | Claude Code | Confirmar o resultado do quarto teste. | Funcionou: o LLM gerou 4 cards no formato pedido para a User Story da biblioteca. A IA conferiu a saída e listou os próximos passos. |
| 14/11/2026 | Claude Code | Entender o fluxo completo: Docker (imagem, container, rede), o portal da plataforma, HTTP/HTTPS e o servidor Ollama. | A IA explicou com um diagrama e relacionou cada erro que vi (SSL, 502, 504) à etapa do fluxo em que ele aconteceu. |
| 15/11/2026 | Claude Code | Entender o que é uma tag/release do Git e planejar o nível intermediário a partir do enunciado. | A IA explicou a diferença entre tag, branch e release e propôs uma divisão do código por responsabilidade e uma ordem de passos com commits pequenos. Criei a tag do nível básico e comecei o intermediário. |
| 15/11/2026 | Claude Code | Entender qual é o papel do `main.py` e começar o passo 1 do intermediário (exceções e configuração). | A IA explicou que o `main.py` só coordena e transforma as exceções em mensagens, e mostrou o código do `erros.py` e do `config.py`, que digitei e testei. |
| 15/11/2026 | Claude Code | Perguntar se o projeto deveria usar MVC ou outra organização de pastas. | A IA explicou por que o MVC não se encaixa num programa de terminal pequeno e sugeriu um pacote Python (`gerador_cards/`) com uma pasta separada para os testes. Movi os módulos para o pacote. |
