from typing import List, Dict

from pythonparser import lexer, source, diagnostic
from lexic_unit import LexicUnit as Token


def generate_python_tokens(file_data: Dict[str, str]) -> List[Token]:
    """Return a list of Token objects with the tokens found in a code file."""
    file_path = file_data.get("path")
    file_content = file_data.get("content")
    buffer = source.Buffer(file_content, file_path)
    engine = diagnostic.Engine()
    tokens = lexer.Lexer(buffer, (3, 6), diagnostic_engine=engine)
    tokens_list = [
        Token((token.loc.begin_pos, token.loc.end_pos), token.kind, token.value)
        for token in tokens
    ]
    return tokens_list


parser_functions = {
    "py": generate_python_tokens,
}
