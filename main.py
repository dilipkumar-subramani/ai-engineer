from embedding.embedding_service import EmbeddingService
from embedding.embedding_provider_resolver import EmbeddingProviderResolver

def main():
     # 1. Create resolver
    resolver = EmbeddingProviderResolver()

    # 2. Inject resolver into service
    service = EmbeddingService(resolver)

    # 3. Create embedding
    try:
        result = service.create_embedding(
        "insurance",
        "Commercial loan booking document"
        )
    except ValueError as e:
        print(e)
        return {
            "error": str(e)
        }

    print(result)

if __name__ == "__main__":
    main()

