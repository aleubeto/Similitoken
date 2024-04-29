import unittest
from tests.test_file_manager import *
from tests.test_token_manager import *

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("test_file_manager")
    test_suite = test_loader.discover("test_token_manager")
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
