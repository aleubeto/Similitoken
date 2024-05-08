from typing import Dict, List, Tuple
from difflib import SequenceMatcher, Match

from parsers import parser_functions
from lexic_unit import LexicUnit as Token


class TokenManager:
    def __init__(self) -> None:
        """Initialize the TokenManager."""
        self.ignored_token_types = {"newline", "comment"}

    def generate_tokens_from_file(self, file_data: Dict[str, str]) -> List[Token]:
        """Generate tokens from file data.
        Args:
            file_data (Dict[str, str]): Data of the file.
        Returns:
            List[Token]: List of generated tokens.
        Raises:
            ValueError: If the file extension is not supported.
        """
        language_extension = file_data.get("extension")
        if language_extension in parser_functions:
            return parser_functions[language_extension](file_data)
        raise ValueError(f"Unsupported file extension: {language_extension}")

    def _process_identifier_token(
        self, token: Token, counter: int
    ) -> Tuple[Tuple[int, int, str], str, str]:
        """Process an identifier token, renaming it.
        Args:
            token (Token): Identifier token.
            counter (int): Counter for renaming the identifier.
        Returns:
            Tuple[Tuple[int, int], str, str]: Processed token details.
        """
        return token.range, token.kind, f"ident_{counter}"

    def _process_token(self, token: Token) -> Tuple[Tuple[int, int, str], str, str]:
        """Process a token without modifying it, except comments.
        Args:
            token (Token): Token to process.
        Returns:
            Tuple[Tuple[int, int], str, str]: Processed token details.
        """
        return token.range, token.kind, token.value

    def _normalize_tokens_list(
        self, tokens_list: List[Token]
    ) -> List[Tuple[Tuple[int, int, str], str, str]]:
        """Normalize the token list.
        Rename identifiers and remove ignored tokens.
        Args:
            tokens_list (List[Token]): List of tokens to normalize.
        Returns:
            List[Tuple[Tuple[int, int], str, str]]: Normalized token list.
        """
        normalized_tokens = []
        visited_ident_tokens = {}
        identifiers_count = 0
        for token in tokens_list:
            if token.kind == "ident":
                value = token.value
                if value not in visited_ident_tokens:
                    renamed_token = self._process_identifier_token(
                        token, identifiers_count
                    )
                    visited_ident_tokens[value] = renamed_token
                    identifiers_count += 1
                normalized_tokens.append(visited_ident_tokens[value])
            elif token.kind not in self.ignored_token_types:
                normalized_tokens.append(self._process_token(token))
        return normalized_tokens

    def _get_matching_blocks(
        self, tokens1: List[str], tokens2: List[str]
    ) -> List[Match]:
        """Find matching blocks of tokens.
        Use difflib to find matching blocks.
        Args:
            tokens1 (List[str]): List of tokens from the first set.
            tokens2 (List[str]): List of tokens from the second set.
        Returns:
            List[Match]: List of matching blocks of tokens.
        """
        matcher = SequenceMatcher(None, tokens1, tokens2)
        return matcher.get_matching_blocks()

    def find_match_ranges_from_tokens(
        self, token_list_1: List[Token], token_list_2: List[Token], match_size: int = 1
    ) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        """Find match ranges between two lists of tokens.
        Args:
            token_list_1 (List[Token]): First list of tokens.
            token_list_2 (List[Token]): Second list of tokens.
            match_size (int, optional): Minimum size of the match. Defaults to 1.
        Returns:
            List[Tuple[Tuple[int, int], Tuple[int, int]]]: List of match ranges.
        """
        normalized_list_1 = self._normalize_tokens_list(token_list_1)
        normalized_list_2 = self._normalize_tokens_list(token_list_2)
        token_values_1 = [token[2] for token in normalized_list_1]
        token_values_2 = [token[2] for token in normalized_list_2]
        matching_blocks = self._get_matching_blocks(token_values_1, token_values_2)
        match_ranges = []
        for block in matching_blocks:
            if block.size > match_size:
                match_1_start, match_2_start, size = block
                file_1_match_start_range = normalized_list_1[match_1_start][0]
                file_2_match_start_range = normalized_list_2[match_2_start][0]
                file_1_match_end_range = normalized_list_1[match_1_start + size - 1][0]
                file_2_match_end_range = normalized_list_2[match_2_start + size - 1][0]
                match_range_1 = (file_1_match_start_range[0], file_1_match_end_range[1])
                match_range_2 = (file_2_match_start_range[0], file_2_match_end_range[1])
                match_ranges.append((match_range_1, match_range_2))
        return match_ranges
