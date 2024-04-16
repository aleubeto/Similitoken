from file_manager import FileManager
from token_manager import TokenManager
from plotter import plot_matches

if __name__ == "__main__":
    files = FileManager()
    file1 = "similitoken/tests/input_files/sum_1.py"
    file2 = "similitoken/tests/input_files/sum_2.py"
    files.load_file(file1)
    files.load_file(file2)

    file1_data = files.get_file_data(file1)
    file2_data = files.get_file_data(file2)

    tokens = TokenManager()
    file1_tokens = tokens.generate_tokens_from_file(file1_data)
    file2_tokens = tokens.generate_tokens_from_file(file2_data)
    matches = tokens.find_match_ranges_from_tokens(file1_tokens, file2_tokens)

    file1_content = files.get_file_data(file1, "content")
    file2_content = files.get_file_data(file2, "content")
    for match in matches:
        print(match)
        match_range_1, match_range_2 = match[0], match[1]
        print(file1_content[match_range_1[0] : match_range_1[1]])
        print(file2_content[match_range_2[0] : match_range_2[1]])

    plot_matches(matches, len(file1_content), len(file2_content), img_name="prueba")
