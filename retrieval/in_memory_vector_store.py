from vector_store import VectorStore
from vector_store import VectorDocument

class InMemoryVectorStore(VectorStore):

    def __init__(self):
        self.documents = []

    def add(self,document: VectorDocument) -> None:
        self.documents.append(document)

    