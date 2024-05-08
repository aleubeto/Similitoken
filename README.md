# Similitoken: Code files match blocks detector

Library to detect plagiarism by comparing files, detecting codeblock matches and returning their ranges, statistics and other utilities.

### Installation guide

1. Create a virtual environment using `python -m venv venv`
2. Activate your virtual environment using `source venv/Scripts/activate`
3. Install the package dependencies with `pip install git+https://github.com/aleubeto/Similitoken`

### Test suite execution guide

To execute the package whole test suite just clone the repository, install the dependencies and run `python similitoken/tests/test_suite.py` in your command line.

### Usage

#### Supported programming languages

Since the **Similitoken** project is based on comparing plain text files by turning them into tokens lists, there is a list of programming languages that are supported for being parsed by this project:

- Python
- C (comming soon)

#### File Manager

You can use this module to process and store files information in order to find plagiarism between code files.

```python
files = FileManager()
file1 = "path/to/file1.py"
file2 = "path/to/file2.py"

# Store files info inside file manager
files.load_file(file1)
files.load_file(file2)

# Retrieve the files data (path, name, extension, content)
file1_data = files.get_file_data(file1)
file2_data = files.get_file_data(file2)
```

#### Token Manager

You can use this module to find plagiarism between files by generating a lists of tokens from their content and compare them to identify ranges from matching code blocks.

```python
tokens = TokenManager()

# Generate tokens from files data
file1_tokens = tokens.generate_tokens_from_file(file1_data)
file2_tokens = tokens.generate_tokens_from_file(file2_data)

# Retrieve ranges from matching blocks between files
matches = tokens.find_match_ranges_from_tokens(
    file1_tokens, file2_tokens, match_size=3
)
```
