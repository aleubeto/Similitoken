from file_manager import FileManager

if __name__ == "__main__":
    files = FileManager()
    file1 = "similitoken/tests/input_files/sum_1.py"
    file2 = "similitoken/tests/input_files/sum_2.py"

    files.load_file(file1)
    files.load_file(file2)

    files.compare_files(file1, file2)
