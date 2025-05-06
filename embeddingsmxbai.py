import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(model="mxbai-embed-large")

texto = "batatinha quando nasce espalha a rama pelo chao"

vetor = embeddings.embed_query(texto)

print("Analisando a frase...")
print("Tamanho do vetor de embeddings:", len(vetor))
print("Valores iniciais do vetor:", vetor[:10])
