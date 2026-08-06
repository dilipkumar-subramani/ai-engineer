class EmbeddingProviderResolver:

    def __init__(self):
        self.providers = {
            #  "legal": TitanEmbeddingProvider(),
            # "medical": OpenAIEmbeddingProvider(),
            # "banking": VoyageEmbeddingProvider()
        }

    def get_provider(self, document_type):
        return self.providers[document_type]
