import re

def tokenizar_texto(texto):
    return re.findall(r'\b\w+\b', texto)
