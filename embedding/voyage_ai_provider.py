from .provider import EmbeddingProvider

class VoyageEmbeddingProvider(EmbeddingProvider):
    
    def create_embedding(self, text):
         print("Using Voyage Embeddings")

         return {
            "provider": "Voyage",
            "text" : text,
            "embedding": [1,2,3]
        }
 