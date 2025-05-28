import tiktoken

def count_tokens(text: str, base_encoding: str) -> int:
    encoding = tiktoken.get_encoding(base_encoding)
    tokens = encoding.encode(text)
    return len(tokens)