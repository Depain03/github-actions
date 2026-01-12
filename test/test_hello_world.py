import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
import importlib.util

# Import the printhello function from hello-world.py
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
script_path = os.path.join(script_dir, "hello-world.py")

spec = importlib.util.spec_from_file_location("hello_world", script_path)
hello_world = importlib.util.module_from_spec(spec)

# Mock argparse to avoid it trying to parse test arguments
with patch('sys.argv', ['hello-world.py', '--name', 'test']):
    spec.loader.exec_module(hello_world)


class TestPrintHello(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_printhello_with_name(self, mock_stdout):
        """Test printhello function with a name"""
        hello_world.printhello("Alice")
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello World, Alice!")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_printhello_with_different_name(self, mock_stdout):
        """Test printhello function with different name"""
        hello_world.printhello("Bob")
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello World, Bob!")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_printhello_with_empty_string(self, mock_stdout):
        """Test printhello function with empty string"""
        hello_world.printhello("")
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello World, !")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_printhello_with_special_characters(self, mock_stdout):
        """Test printhello function with special characters"""
        hello_world.printhello("John-Doe")
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello World, John-Doe!")


if __name__ == '__main__':
    unittest.main()
