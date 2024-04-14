import os
import difflib
from typing import Dict

from tokens import token_functions, normalize_tokens_list
from pythonparser.lexer import Token


class FileManager:
    """Wrapper class that will process and store files information
    in order to find plagiarism between code files."""

    def __init__(self) -> None:
        self.processed_files = {}
        pass

    def _read_file_content(self, file_path: str) -> str:
        """Returns the content of a given file inside
        a string."""
        with open(file_path, "r") as file:
            return file.read()

    def _generate_tokens_from_file(self, file_data: Dict[str, str]) -> list[Token]:
        """Returns a list with the processed tokens from
        the content of a given file."""
        language_extention = file_data.get("extention")
        return token_functions[language_extention](file_data)

    def load_file(self, file_path: str) -> None:
        """Process and stores the data of a given file inside
        the processed_files dictionary."""
        file_name = os.path.basename(file_path)
        file_extension = file_name.split(".", 1)[1]
        file_content = self._read_file_content(file_path)
        file_data = {
            "path": file_path,
            "name": file_name,
            "extention": file_extension,
            "content": file_content,
        }
        file_tokens = self._generate_tokens_from_file(file_data)
        file_data["tokens"] = file_tokens
        formatted_path = os.path.normpath(file_path)
        self.processed_files[formatted_path] = file_data

    def get_file_data(self, file_path) -> Dict[str, str]:
        """Returns a dictionary with name, path, file extention,
        content and tokens list from a given file."""
        formatted_path = os.path.normpath(file_path)
        return self.processed_files[formatted_path]

    def compare_files(self, file1_path: str, file2_path: str) -> list[str]:
        """"""
        file1_tokens = self.get_file_data(file1_path).get("tokens")
        file2_tokens = self.get_file_data(file2_path).get("tokens")
        normalized_file1_tokens = normalize_tokens_list(file1_tokens)
        normalized_file2_tokens = normalize_tokens_list(file2_tokens)
