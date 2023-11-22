import subprocess
from datetime import datetime

def commit_to_github(commit_message):
    # コミットの作成
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    # リモートリポジトリにプッシュ
    subprocess.run(['git', 'push'], check=True)

# 学習記録をGitHubにコミット
if study_records:
    for record in study_records:
        date = datetime.now().strftime("%Y-%m-%d")
        message = f"Studied {record['subject']} for {record['duration']} on {date}"
        commit_to_github(message)
