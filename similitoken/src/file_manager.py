import os
from typing import Dict


class FileManager:
    """Wrapper class that will process and store files information
    in order to find plagiarism between code files."""

    def __init__(self) -> None:
        """Initializes the FileManager."""
        self.processed_files = {}

    def _read_file_content(self, file_path: str) -> str:
        """Reads the content of a given file and returns it as a string.
        Args:
            file_path (str): The path to the file.
        Returns:
            str: The content of the file.
        """
        with open(file_path, "r") as file:
            return file.read()

    def load_file(self, file_path: str) -> None:
        """Processes and stores the data of a given file.
        Args:
            file_path (str): The path to the file.
        """
        file_name = os.path.basename(file_path)
        file_extension = file_name.rsplit(".", 1)[-1] if "." in file_name else None
        file_content = self._read_file_content(file_path)
        file_data = {
            "path": file_path,
            "name": file_name,
            "extension": file_extension,
            "content": file_content,
        }
        self.processed_files[file_path] = file_data

    def get_file_data(self, file_path: str, key: str = None) -> Dict[str, str]:
        """Retrieves data of a given file.
        Args:
            file_path (str): The path to the file.
            key (str, optional): The specific information to retrieve.
                If None, returns all file data. Defaults to None.
        Returns:
            Dict[str, str]: The requested file data.
        """
        file_data = self.processed_files.get(file_path)
        if not file_data:
            return {}
        if key:
            return {key: file_data.get(key)}
        return file_data
