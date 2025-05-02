# Acesso-ollama
Repositório de script python para conexão ao ollama e geração de embeddings.

## Instalação de dependências
--Ter python 3.11 instalado previamente na máquina
1) Instalar ollama na máquina a partir do link: https://ollama.com/download

2)Instalar o modelo llama 3.2 de 3 bilhões ou um 1 bilhão de parâmetros digitando no terminal: ollama run llama3.2

3) Verificar as versões do ollama instaladas com: ollama list

4) Testar o funcionamento com o comando: ollama run llama3.2

5)Instalar o langchain ollama: https://python.langchain.com/docs/integrations/llms/ollama/ pip install -U langchain-ollama

6) Instalar a biblioteca de embeds em https://ollama.com/library/mxbai-embed-large ollama pull mxbai-embed-large

7) Instalar pacotes para o funcionamento correto do código: pip install langchain-community scikit-learn numpy

