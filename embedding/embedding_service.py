import random

class EmbeddingService:

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
        return embeddings
