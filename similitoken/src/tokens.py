from pythonparser import lexer, source, diagnostic
from typing import Dict


def generate_python_tokens(file_data: Dict[str, str]) -> list:
    """Return a list of Token objects with the tokens found in a code file."""
    file_path = file_data.get("path")
    file_content = file_data.get("content")
    buffer = source.Buffer(file_content, file_path)
    engine = diagnostic.Engine()
    tokens = lexer.Lexer(buffer, (3, 6), diagnostic_engine=engine)
    tokens_list = [token for token in tokens]
    return tokens_list


token_functions = {
    "py": generate_python_tokens,
}
