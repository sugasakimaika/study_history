import requests
from datetime import datetime
from config import api_token
import base64

def fetch_toggl_records(api_token):
    # Toggl Track APIエンドポイント
    url = 'https://api.track.toggl.com/api/v9/me/time_entries'

    # APIトークンのBase64エンコード
    encoded_token = base64.b64encode(f'{api_token}:api_token'.encode('utf-8')).decode('utf-8')
    headers = {'Authorization': f'Basic {encoded_token}'}

    # 現在の日付を取得し、ISO 8601フォーマットに変換
    today = datetime.now().strftime("%Y-%m-%dT00:00:00+00:00")

    # リクエストのパラメータを設定
    params = {'start_date': today}

    # APIリクエストを実行
    response = requests.get(url, headers=headers, params=params)

    # レスポンスのステータスコードをチェック
    if response.status_code == 200:
        # JSONレスポンスを処理してタイムエントリのリストを返す
        records = response.json()
        return [(record['description'], round(record['duration'] / 60)) for record in records if record['duration'] > 0]
    else:
        # エラーの場合はNoneを返す
        return None

# 使用例

toggl_records = fetch_toggl_records(api_token)
print(toggl_records)
