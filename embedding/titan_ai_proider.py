from .provider import EmbeddingProvider

class TitanEmbeddingProvider(EmbeddingProvider):

    def create_embedding(self, text):
        return super().create_embedding(text)
    