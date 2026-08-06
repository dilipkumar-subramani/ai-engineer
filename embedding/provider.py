from abc import ABC, abstractmethod

class EmbeddingProvider(ABC):

    @abstractmethod
    def create_embedding(self, text):
        pass