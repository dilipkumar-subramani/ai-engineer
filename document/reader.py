def read_document(file_name):
    with open(file_name) as file:
        content = [line.strip() for line in file if line.strip()]
    return content



            


