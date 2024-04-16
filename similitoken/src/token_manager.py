from typing import Dict, List, Tuple
from pythonparser.lexer import Token
import difflib
from difflib import Match

from tokens import token_functions


class TokenManager:
    """"""

    def __init__(self) -> None:
        pass

    def generate_tokens_from_file(self, file_data: Dict[str, str]) -> list[Token]:
        """Returns a list with the processed tokens from
        the content of a given file."""
        language_extention = file_data.get("extention")
        return token_functions[language_extention](file_data)

    def _process_identifier_token(
        self, token: Token, counter: int
    ) -> Tuple[str, str, str]:
        """Processes identifier tokens."""
        token_range = (
            token.loc.begin_pos,
            token.loc.end_pos,
            token.loc.expanded_from,
        )
        token_kind = token.kind
        token_value = f"ident_{counter}"
        return token_range, token_kind, token_value

    def _process_token(self, token: Token) -> Tuple[str, str, str]:
        """Processes non-identifier tokens."""
        token_range = (
            token.loc.begin_pos,
            token.loc.end_pos,
            token.loc.expanded_from,
        )
        token_kind = token.kind
        token_value = token.value
        return token_range, token_kind, token_value

    def _normalize_tokens_list(self, tokens_list: list[Token]) -> list[str]:
        """
        Takes a list of tokens and returns a copy with
        the identifiers tokens renamed as ident_n and
        without the ignored token kinds.
        """
        normalized_tokens = []
        ignored_token_types = ("newline",)
        identifiers_count = 0

        for token in tokens_list:
            token_type = token.kind
            if token_type == "ident":
                normalized_tokens.append(
                    self._process_identifier_token(token, counter=identifiers_count)
                )
                identifiers_count += 1
            elif token_type not in ignored_token_types:
                normalized_tokens.append(self._process_token(token))

        return normalized_tokens

    def _get_matching_blocks(
        self, file1_tokens: tuple[str], file2_tokens: tuple[str]
    ) -> list[Match]:
        """"""
        matcher = difflib.SequenceMatcher(None, file1_tokens, file2_tokens)
        matching_blocks = matcher.get_matching_blocks()
        return matching_blocks

    def _extract_index_range_from_tokens(self, tokens_list):
        """"""
        match_ranges = [token[0][:-1] for token in tokens_list]
        match_start = match_ranges[0][0]
        match_end = match_ranges[-1][-1]
        return match_start, match_end

    def find_match_ranges_from_tokens(self, token_list_1: str, token_list_2: str):
        """"""
        match_ranges = []
        normalized_list_1 = self._normalize_tokens_list(token_list_1)
        normalized_list_2 = self._normalize_tokens_list(token_list_2)
        token_values_1 = [token[1:] for token in normalized_list_1]
        token_values_2 = [token[1:] for token in normalized_list_2]
        matching_blocks = self._get_matching_blocks(token_values_1, token_values_2)

        for block in matching_blocks:
            i, j, n = block
            if n > 0:
                matching_tokens_1 = normalized_list_1[i : i + n]
                matching_tokens_2 = normalized_list_2[j : j + n]
                start_match_1, end_match_1 = self._extract_index_range_from_tokens(
                    matching_tokens_1
                )
                start_match_2, end_match_2 = self._extract_index_range_from_tokens(
                    matching_tokens_2
                )
                match_ranges.append(
                    ((start_match_1, end_match_1), (start_match_2, end_match_2))
                )

        return match_ranges
