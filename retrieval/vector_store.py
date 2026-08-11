from abc import ABC, abstractmethod
from typing import List

from models.vector_document import VectorDocument

class VectorStore(ABC):

    @abstractmethod
    def add_all(self, document: VectorDocument) -> None:
        pass

    @abstractmethod
    def add_all(self, documents: List[VectorDocument]) -> None:
        pass

    @abstractmethod
    def similarity_search(
        self,
        quey_embedding: List[float],
        top_k:int
    ) -> List[VectorDocument]:
        pass
    

