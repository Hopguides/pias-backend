
import os
import subprocess
import requests

# GitHub repository details
repo_name = "pias-backend"
repo_description = "PIAS (Procurement Intelligence Agent System) - AI-powered backend for procurement automation with 5 specialized agents"
private = False
github_token = os.getenv("GITHUB_TOKEN")

if not github_token:
    raise ValueError("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")

# Initialize git repository
subprocess.run(["git", "init"], check=True)

# Add all files to git
subprocess.run(["git", "add", "."], check=True)

# Create initial commit
subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

# Create GitHub repository using GitHub API
headers = {
    "Authorization": f"token {github_token}"
}
data = {
    "name": repo_name,
    "description": repo_description,
    "private": private
}
response = requests.post("https://api.github.com/user/repos", headers=headers, json=data)
response.raise_for_status()

# Extract the clone URL from the response
repo_info = response.json()
clone_url = repo_info["clone_url"]

# Set up remote origin
subprocess.run(["git", "remote", "add", "origin", clone_url], check=True)

# Push to GitHub
subprocess.run(["git", "push", "-u", "origin", "master"], check=True)
