from .embedding_provider_resolver import EmbeddingProviderResolver

class EmbeddingService:

    def __init__(self, embeddingResolver:EmbeddingProviderResolver):
        self.providerResolver = embeddingResolver

    def create_embedding(self, document_type, text):
        if text is None:
            raise ValueError("text is not provided!!!") 

        provider = self.providerResolver.get_provider(document_type)
         
        return provider.create_embedding(text)

    