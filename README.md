# CI-CD-pipeline-demo

## 🚀 CI/CD Pipeline for Static HTML using Python, Bash & Cron on NGINX (Beginner Friendly)

This project builds a lightweight CI/CD pipeline using core DevOps tools without requiring a CI platform like Jenkins or GitHub Actions. It uses:

- 🧱 Bash for deployment
- 🐍 Python to check GitHub commits
- ⏰ Cron for automation
- 🌐 NGINX to host a simple static HTML page

---

## 📁 Project Structure
```
.
├── 01_html_project/              # Task 1: Static HTML Website
├── 02_nginx_setup/              # Task 2: Setup guide for NGINX
├── 03_check_commits_python/     # Task 3: GitHub commit-checking script
├── 04_deploy_bash_script/       # Task 4: Bash script to deploy code + restart NGINX
├── 05_cronjob/                  # Task 5: Cron job + wrapper to run Python script
├── 06_documentation/            # Task 6: README + notes
```

---

## ✅ Task-by-Task Instructions

### 🔹 Task 1: HTML Project
📁 `01_html_project/index.html` contains a simple static site:
```html
<h1>Welcome to My CI/CD Website!</h1>
<p>Deployed at: <span id="deploy-time"></span></p>
```

You can expand this into a full site or landing page as needed.

---

### 🔹 Task 2: NGINX Setup on EC2 or Local Linux
📄 `02_nginx_setup/nginx_setup_guide.md`

```bash
sudo apt update && sudo apt install nginx -y
sudo systemctl enable nginx
```

- Serves files from `/var/www/html`
- Test by visiting `http://<your-ec2-ip>` in the browser

---

### 🔹 Task 3: Python Script – Detect New Commits
📄 `03_check_commits_python/check_for_new_commit.py`

- Uses GitHub API to check the latest commit SHA on a branch
- Compares with previously stored SHA in `/tmp/last_commit_sha.txt`
- If new commit → calls `bash deploy_site.sh`

✅ Requirements:
```bash
export GITHUB_TOKEN=ghp_your_pat_here
```

Replace:
- `REPO_OWNER`, `REPO_NAME`, and `BRANCH`

---

### 🔹 Task 4: Bash Deployment Script
📄 `04_deploy_bash_script/deploy_site.sh`

```bash
git clone https://github.com/your-username/your-repo.git /tmp/html_cicd_repo
cp /tmp/html_cicd_repo/01_html_project/index.html /var/www/html/index.html
sudo systemctl restart nginx
```

- Make sure to `chmod +x deploy_site.sh`

---

### 🔹 Task 5: Cron Job Setup
📄 `05_cronjob/`

- `run_commit_check.sh` is a wrapper to run the Python script and log output
- Logs go to: `/var/log/cicd_commit_checker.log`

🛠 Setup Crontab:
```bash
crontab -e
```

Add:
```
*/5 * * * * /home/ubuntu/run_commit_check.sh
```

---

## 🔍 Task 6: Final Test

### ✅ Steps to Validate:

1. Make sure NGINX is up and serving from `/var/www/html`
2. Push a new commit to the GitHub repo (e.g., update `index.html`)
3. Wait for cron to run (or trigger manually)
   ```bash
   bash /home/ubuntu/run_commit_check.sh
   ```
4. Visit your site (`http://<your-ec2-ip>`) and confirm the new content is deployed

---

## 📘 Notes

- Avoid hardcoding secrets — use environment variables
- Secure NGINX by disabling directory listing, and enabling HTTPS (future enhancement)
- You can add email or Telegram alert on deploy success via cron/log tail

---
