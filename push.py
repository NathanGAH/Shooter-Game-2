import os
import subprocess
import gdown

# --- CONFIGURATION ---
FILE_ID = "135ArAL7-6H73fZFMvT8QwdxJIyloEV0J"
OUTPUT_FILE = "ShooterGame2.sb3"

def download_drive_file():
    print("Fetching latest project from Google Drive...")
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, OUTPUT_FILE, quiet=False)

def run_git_pipeline():
    try:
        # 1. Stage all changes (new CSS/JS files, modified index.html, updated .sb3)
        print("Staging all local changes...")
        subprocess.run(["git", "add", "-A"], check=True)

        # 2. Check if there are changes to commit
        status = subprocess.check_output(["git", "status", "--porcelain"]).decode('utf-8').strip()
        if status:
            print("New changes detected! Committing locally...")
            subprocess.run(["git", "commit", "-m", "Auto-update project files"], check=True)
        else:
            print("No local changes detected.")

        # 3. Pull remote changes cleanly (working tree is now clean)
        print("Syncing with remote repository...")
        subprocess.run(["git", "pull", "--rebase"], check=True)

        # 4. Push to GitHub
        if status:
            print("Pushing updates to GitHub...")
            subprocess.run(["git", "push"], check=True)
            print("Successfully updated GitHub Pages!")
        else:
            print("Everything up to date!")

    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

if __name__ == "__main__":
    download_drive_file()
    run_git_pipeline()
