from .open_ai_provider import OpenAIEmbeddingProvider
from .titan_ai_proider import TitanEmbeddingProvider
from .voyage_ai_provider import VoyageEmbeddingProvider

class EmbeddingProviderResolver:

    def __init__(self):
        self.providers = {
             "legal": TitanEmbeddingProvider(),
            "medical": OpenAIEmbeddingProvider(),
            "banking": VoyageEmbeddingProvider()
        }

    def get_provider(self, document_type):
        provider =self.providers.get(document_type)

        if provider is None:
          raise ValueError(
            f"No embedding provider configured for document type: {document_type}"
          )

        return provider
