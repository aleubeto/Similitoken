import os
from typing import Dict


class FileManager:
    """"""

    def __init__(self) -> None:
        self.processed_files = {}
        pass

    def _read_file_content(self, file_path: str) -> str:
        """"""
        with open(file_path, "r") as file:
            return file.read()

    def _generate_tokens_from_content(self, file_content: str) -> list[str]:
        """"""
        return []

    def load_file(self, file_path: str) -> None:
        """"""
        file_name = os.path.basename(file_path)
        file_extension = file_name.split(".", 1)[1]
        file_content = self._read_file_content(file_path)
        file_tokens = self._generate_tokens_from_content(file_content)
        file_data = {
            "file_name": file_name,
            "file_extention": file_extension,
            "file_content": file_content,
            "tokens": file_tokens,
        }
        formatted_path = os.path.normpath(file_path)
        self.processed_files[formatted_path] = file_data
        print(self.processed_files)

    def get_file_data(self, file_path) -> Dict[str, str]:
        """"""
        return self.processed_files[file_path]
