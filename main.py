from document.reader import read_document
from document.chunker import chunk_document

lines = read_document("data/document.txt")
chunks = chunk_document(lines, 2)

print(f"Chunks:{chunks}")