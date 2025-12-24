from unstructured.partition.text import partition_text

def structure_text(raw_text):
    elements = partition_text(text=raw_text)
    return [str(e) for e in elements]
