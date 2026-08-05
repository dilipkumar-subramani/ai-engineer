class VeotorStore:

    def __init__(self):
        self.vectors = []

    def save(self,embedding):
        if embedding is None:
            raise ValueError("Embedding is mandatory!!!")

        self.vectors.append(embedding)
        return len(self.vectors)
