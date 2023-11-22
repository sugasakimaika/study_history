pytestimport unittest
from unittest.mock import patch
from commit_to_github import commit_to_github

class TestCommitToGithub(unittest.TestCase):
    @patch('commit_to_github.subprocess.run')
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
