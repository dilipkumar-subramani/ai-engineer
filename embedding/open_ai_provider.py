from .provider import EmbeddingProvider

class OpenAIEmbeddingProvider(EmbeddingProvider):

    def create_embedding(self, chunk):
        print("Using OpenAI Embeddings")

        return{
            "provider": "openai",
            "text" : chunk,
            "embedding": [1,2,3]
        }





    
