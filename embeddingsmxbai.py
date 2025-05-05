import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(model="mxbai-embed-large")

texto = "A realidade sempre é mais ou menos do que nós queremos."

vetor = embeddings.embed_query(texto)

print("Analisando a frase...")
print("Tamanho do vetor de embeddings:", len(vetor))
print("Valores iniciais do vetor:", vetor[:10])
