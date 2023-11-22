import requests

def fetch_studyplus_records(api_key):
    # Studyplus APIのエンドポイントURL
    url = 'STUDYPLUS_API_ENDPOINT'
    
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Studyplus APIキー
api_key = 'YOUR_STUDYPLUS_API_KEY'
study_records = fetch_studyplus_records(api_key)
