import subprocess
from datetime import datetime
from studyplus_records_api import fetch_studyplus_records

def commit_to_github(commit_message):
    # コミットの作成
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    # リモートリポジトリにプッシュ
    subprocess.run(['git', 'push'], check=True)

# 学習記録をGitHubにコミットする例
api_key = 'YOUR_STUDYPLUS_API_KEY'
study_records = fetch_studyplus_records(api_key)

if study_records:
    for record in study_records:
        date = datetime.now().strftime("%Y-%m-%d")
        message = f"Studied {record.subject} for {record.duration} minutes on {date}"
        commit_to_github(message)
