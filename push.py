import os
import subprocess
import gdown

# --- CONFIGURATION ---
FILE_ID = "135ArAL7-6H73fZFMvT8QwdxJIyloEV0J"
OUTPUT_FILE = "ShooterGame2.sb3"

def sync_git_pull():
    print("Syncing with remote repository...")
    subprocess.run(["git", "pull", "--rebase"], check=True)

def download_drive_file():
    print("Fetching latest project from Google Drive...")
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, OUTPUT_FILE, quiet=False)

def push_git_changes():
    try:
        # Stage all updated files (index.html, ShooterGame2.sb3, etc.)
        subprocess.run(["git", "add", "-A"], check=True)

        # Check if there are staged changes ready to commit
        status = subprocess.check_output(["git", "status", "--porcelain"]).decode('utf-8').strip()
        if not status:
            print("No changes detected. Skipping push.")
            return

        print("New changes detected! Committing and pushing to GitHub...")
        subprocess.run(["git", "commit", "-m", "Auto-update project files"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Successfully updated GitHub Pages!")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

if __name__ == "__main__":
    # 1. Sync remote changes while working directory is clean
    sync_git_pull()

    # 2. Download the latest file from Google Drive
    download_drive_file()

    # 3. Stage, commit, and push changes
    print("Checking Git state...")
    push_git_changes()
