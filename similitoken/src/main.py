from file_manager import FileManager
from token_manager import TokenManager

if __name__ == "__main__":
    files = FileManager()
    tokens = TokenManager()

    file1 = "similitoken/tests/input_files/sum_1.py"
    file2 = "similitoken/tests/input_files/sum_2.py"

    files.load_file(file1)
    files.load_file(file2)

    file1_data = files.get_file_data(file1)
    file2_data = files.get_file_data(file2)

    file1_content = files.get_file_data(file1, "content")
    file2_content = files.get_file_data(file2, "content")

    file1_tokens = tokens.generate_tokens_from_file(file1_data)
    file2_tokens = tokens.generate_tokens_from_file(file2_data)

    matches = tokens.find_match_ranges_from_tokens(file1_tokens, file2_tokens)
    for match in matches:
        print(match)
        print(files.extract_content_from_range(match[0][0], match[0][1], file1_content))
        print(files.extract_content_from_range(match[1][0], match[1][1], file2_content))
