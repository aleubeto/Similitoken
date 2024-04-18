from typing import Dict, List, Tuple
from pythonparser.lexer import Token
import difflib
from difflib import Match

from tokens import token_functions

class TokenManager:
    def __init__(self) -> None:
        self.ignored_token_types = ("newline", "comment")  # Ajuste para ignorar los comentarios en el análisis

    def generate_tokens_from_file(self, file_data: Dict[str, str]) -> List[Token]:
        language_extension = file_data.get("extension")
        if language_extension and language_extension in token_functions:
            return token_functions[language_extension](file_data)
        else:
            raise ValueError(f"Unsupported file extension: {language_extension}")

    def _process_identifier_token(self, token: Token, counter: int) -> Tuple[Tuple[int, int, str], str, str]:
        """Return token details with identifiers renamed."""
        token_range = (token.loc.begin_pos, token.loc.end_pos)
        return (token_range, token.kind, f"ident_{counter}")

    def _process_token(self, token: Token) -> Tuple[Tuple[int, int, str], str, str]:
        """Return token details without modification, except comments."""
        token_range = (token.loc.begin_pos, token.loc.end_pos)
        return (token_range, token.kind, token.value)

    def _normalize_tokens_list(self, tokens_list: List[Token]) -> List[Tuple[Tuple[int, int, str], str, str]]:
        """Normalize the token list by renaming identifiers and removing ignored tokens."""
        normalized_tokens = []
        identifiers_count = 0
        for token in tokens_list:
            if token.kind == "ident":
                normalized_tokens.append(self._process_identifier_token(token, identifiers_count))
                identifiers_count += 1
            elif token.kind not in self.ignored_token_types:
                normalized_tokens.append(self._process_token(token))
        return normalized_tokens

    def _get_matching_blocks(self, tokens1: List[str], tokens2: List[str]) -> List[Match]:
        """Use difflib to find matching blocks of tokens."""
        matcher = difflib.SequenceMatcher(None, tokens1, tokens2)
        return matcher.get_matching_blocks()

    def find_match_ranges_from_tokens(self, token_list_1: List[Token], token_list_2: List[Token]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        """Find match ranges between two lists of tokens."""
        normalized_list_1 = self._normalize_tokens_list(token_list_1)
        normalized_list_2 = self._normalize_tokens_list(token_list_2)
        token_values_1 = [token[2] for token in normalized_list_1]
        token_values_2 = [token[2] for token in normalized_list_2]
        matching_blocks = self._get_matching_blocks(token_values_1, token_values_2)
        match_ranges = []
        for block in matching_blocks:
            if block.size > 0:
                start1, start2, size = block
                match_range_1 = (normalized_list_1[start1][0][0], normalized_list_1[start1 + size - 1][0][1])
                match_range_2 = (normalized_list_2[start2][0][0], normalized_list_2[start2 + size - 1][0][1])
                match_ranges.append((match_range_1, match_range_2))
        return match_ranges
    
    def find_relevant_matches(self, token_list_1, token_list_2):
        normalized_list_1 = self._normalize_tokens_list(token_list_1)
        normalized_list_2 = self._normalize_tokens_list(token_list_2)
        token_values_1 = [token[2] for token in normalized_list_1]
        token_values_2 = [token[2] for token in normalized_list_2]
        matcher = difflib.SequenceMatcher(None, token_values_1, token_values_2)
        matching_blocks = matcher.get_matching_blocks()

        relevant_matches = []
        for block in matching_blocks:
            if block.size > 1:  # Considerar sólo bloques de un tamaño mínimo
                start1, start2, size = block
                match_range_1 = (normalized_list_1[start1][0][0], normalized_list_1[start1 + size - 1][0][1])
                match_range_2 = (normalized_list_2[start2][0][0], normalized_list_2[start2 + size - 1][0][1])
                relevant_matches.append((match_range_1, match_range_2))
        return relevant_matches
