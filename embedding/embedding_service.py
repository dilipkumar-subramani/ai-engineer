import random

class EmbeddingService:

    def __init__(self, provider):
        self.provider = provider

    def create_embedding(self, chunk: str):
        if chunk is None:
            raise ValueError("chunk is not provided!!!") 

        embeddings = {
            "id":  random.randint(0, len(chunk)),
            "text" : chunk,
            "embedding": [
                len(chunk),
                chunk.lower().count("loan"),
                chunk.lower().count("interest")
            ]            
        }
        return self.provider.create_embedding(self, chunk)
