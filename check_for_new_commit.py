import requests
import json
import os

# GitHub repo details (replace these)
REPO_OWNER = "your-github-username"
REPO_NAME = "your-repo-name"
BRANCH = "main"  # or 'master'
TOKEN = os.getenv("GITHUB_TOKEN")  # store your PAT as env variable

# Store last commit SHA
SHA_FILE = "/tmp/last_commit_sha.txt"

def get_latest_commit():
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits/{BRANCH}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch commits: {response.status_code} - {response.text}")

    return response.json()["sha"]

def has_new_commit():
    latest_sha = get_latest_commit()

    # If SHA file does not exist
    if not os.path.exists(SHA_FILE):
        with open(SHA_FILE, "w") as f:
            f.write(latest_sha)
        return True

    with open(SHA_FILE, "r") as f:
        old_sha = f.read().strip()

    if old_sha != latest_sha:
        print("✅ New commit detected!")
        with open(SHA_FILE, "w") as f:
            f.write(latest_sha)
        return True
    else:
        print("ℹ️ No new commit.")
        return False

if __name__ == "__main__":
    if has_new_commit():
        os.system("bash /home/ubuntu/deploy_site.sh")  # Path to your bash deployment script