import requests
from studyrecord import StudyRecord

def fetch_studyplus_records(api_key):
    # Studyplus APIのエンドポイントURL（実際のURLに置き換えてください）
    url = 'https://api.studyplus.example.com/records'

    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # JSONレスポンスをStudyRecordオブジェクトに変換
        records = response.json()
        return [StudyRecord(subject=record['subject'], duration=record['duration']) for record in records]
    else:
        return None
