from file_manager import FileManager
from token_manager import TokenManager
from plotter import Plotter

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
    matches = tokens.find_match_ranges_from_tokens(
        file1_tokens, file2_tokens, match_size=3
    )

    file1_content = file1_data["content"]
    file2_content = file2_data["content"]

    for match in matches:
        print("---------------")
        print("Match Found:")
        print(f"File 1 Content [{match[0][0]}:{match[0][1]}]:")
        print(file1_content[match[0][0] : match[0][1]])
        print(f"File 2 Content [{match[1][0]}:{match[1][1]}]:")
        print(file2_content[match[1][0] : match[1][1]])
        print("---------------")

    # Creación de una instancia de Plotter y llamada a la función plot_matches
    plotter = Plotter()
    plotter.plot_matches(matches, img_name="comparison_output")
