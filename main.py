from embedding.embedding_service import EmbeddingService
from embedding.embedding_provider_resolver import EmbeddingProviderResolver

def main():
     # 1. Create resolver
    resolver = EmbeddingProviderResolver()

    # 2. Inject resolver into service
    service = EmbeddingService(resolver)

    # 3. Create embedding
    result = service.create_embedding(
        "banking",
        "Commercial loan booking document"
    )

    print(result)

if __name__ == "__main__":
    main()

