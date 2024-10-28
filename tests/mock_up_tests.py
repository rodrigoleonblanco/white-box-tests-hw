# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import subprocess
import unittest
from unittest.mock import patch, mock_open
from src.mock_up import read_data_from_file, execute_command, perform_action_based_on_time


class TestFunctions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="mock file content")
    def test_read_data_from_file_success(self, mock_file):
        result = read_data_from_file("dummy_file.txt")
        self.assertEqual(result, "mock file content")
        mock_file.assert_called_once_with("dummy_file.txt", 'r')

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_data_from_file_file_not_found(self, mock_file):
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("non_existent_file.txt")
        mock_file.assert_called_once_with("non_existent_file.txt", 'r')

    @patch("subprocess.run")
    def test_execute_command_success(self, mock_subprocess):
        mock_subprocess.return_value.stdout = "mock command output"
        result = execute_command(["echo", "Hello, World!"])
        self.assertEqual(result, "mock command output")
        mock_subprocess.assert_called_once_with(["echo", "Hello, World!"], capture_output=True, text=True)

    @patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "command"))
    def test_execute_command_failure(self, mock_subprocess):
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["false"])
        mock_subprocess.assert_called_once_with(["false"], capture_output=True, text=True)

    @patch("time.time", return_value=5)
    def test_perform_action_based_on_time_before_threshold(self, mock_time):
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()

    @patch("time.time", return_value=15)
    def test_perform_action_based_on_time_after_threshold(self, mock_time):
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()


if __name__ == '__main__':
    unittest.main()
