from pythonparser import lexer, source, diagnostic
from typing import Dict

from pythonparser.lexer import Token


def process_token(token: Token, counter: int, rename: bool = False) -> list[str]:
    """"""
    token_range = f"{token.loc.begin_pos}-{token.loc.end_pos}-{token.loc.expanded_from}"
    token_kind = token.kind
    token_value = f"ident_{counter}" if rename else token.value
    return [token_range, token_kind, token_value]


def normalize_tokens_list(tokens_list: list[Token]) -> list[str]:
    """"""
    normalized_tokens = []
    ignored_token_types = ("newline",)
    identifiers_count = 0

    for token in tokens_list:
        if token.kind == "ident":
            normalized_tokens.append(
                process_token(token, counter=identifiers_count, rename=True)
            )
            identifiers_count += 1
        elif token.kind not in ignored_token_types:
            normalized_tokens.append(process_token(token, counter=identifiers_count))

    return normalized_tokens


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
