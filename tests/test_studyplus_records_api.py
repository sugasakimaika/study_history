import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import patch
from src.studyplus_records_api import fetch_studyplus_records

class TestStudyPlusRecordsAPI(unittest.TestCase):
    def test_fetch_studyplus_records_success(self):
        # Mock the requests.get method to return a successful response
        with patch('studyplus_records_api.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {'data': 'study records'}

            api_key = 'VALID_API_KEY'
            result = fetch_studyplus_records(api_key)

            # 200と確認できて、得られるresult(StudyRecord)が期待通りであるか確認
            self.assertEqual(result, {'data': 'study records'})

    def test_fetch_studyplus_records_failure(self):
        # Mock the requests.get method to return a failure response
        with patch('studyplus_records_api.requests.get') as mock_get:
            mock_get.return_value.status_code = 404

            # Call the function with an invalid API key
            api_key = 'INVALID_API_KEY'
            result = fetch_studyplus_records(api_key)

            # Assert that the response is None
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
