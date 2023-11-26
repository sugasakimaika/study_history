from studyplus_records_api import fetch_toggl_records

def commit_to_github(commit_message):
    # コミットの作成
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    # リモートリポジトリにプッシュ
    subprocess.run(['git', 'push'], check=True)

# Toggl Trackからの学習記録をGitHubにコミットする例
toggl_api_token = 'YOUR_TOGGL_API_TOKEN'
toggl_records = fetch_toggl_records(toggl_api_token)

if toggl_records:
    for subject, duration in toggl_records:
        date = datetime.now().strftime("%Y-%m-%d")
        message = f"Studied {subject} for {duration} minutes on {date}"
        commit_to_github(message)


toggl_records = fetch_toggl_records(toggl_api_token)
print("Fetched records:", toggl_records) 
