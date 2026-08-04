def chunk_document(lines, chunk_size):
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    chunks = []
    for i in range(0, len(lines), chunk_size):
        chunk = lines[i:i + chunk_size]
        chunks.append(chunk)
    return chunks



