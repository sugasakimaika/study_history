import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import patch
from src.commit_to_github import commit_to_github
from src.studyplus_records_api import fetch_studyplus_records

class TestCommitToGithub(unittest.TestCase):
    @patch('src.commit_to_github.subprocess.run')
    def test_commit_to_github(self, mock_run):
        # Mock the subprocess.run method to avoid actual execution
        mock_run.return_value = None

        # Call the function with a commit message
        commit_message = "Test commit"
        commit_to_github(commit_message)

        # Assert that the subprocess.run method was called with the correct arguments
        mock_run.assert_called_with(['git', 'add', '.'], check=True)
        mock_run.assert_called_with(['git', 'commit', '-m', commit_message], check=True)
        mock_run.assert_called_with(['git', 'push'], check=True)

if __name__ == '__main__':
    unittest.main()
