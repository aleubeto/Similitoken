import os
from typing import Dict, List, Tuple
from pythonparser.lexer import Token
import difflib
from difflib import Match

from tokens import token_functions


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
        formatted_path = os.path.normpath(file_path)
        self.processed_files[formatted_path] = file_data

    def get_file_data(self, file_path: str, key: str = None) -> Dict[str, str]:
        """Returns a dictionary with name, path, file extention,
        content and tokens list from a given file."""
        formatted_path = os.path.normpath(file_path)
        file_data = (
            self.processed_files.get(formatted_path).get(key)
            if key
            else self.processed_files.get(formatted_path)
        )
        return file_data

    def extract_content_from_range(
        self, start_index: int, end_index: int, file_content: str
    ) -> str:
        """"""
        return file_content[start_index:end_index]
