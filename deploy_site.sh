#!/bin/bash

# 📂 Deployment Variables
REPO_URL="https://github.com/your-github-username/your-repo-name.git"
DEPLOY_DIR="/var/www/html"
TMP_DIR="/tmp/html_cicd_repo"

echo "🛠️ Starting deployment..."

# Step 1: Clone latest repo to temp folder
rm -rf "$TMP_DIR"
git clone "$REPO_URL" "$TMP_DIR"

# Step 2: Copy HTML to NGINX directory
if [ -f "$TMP_DIR/01_html_project/index.html" ]; then
    cp "$TMP_DIR/01_html_project/index.html" "$DEPLOY_DIR/index.html"
    echo "✅ HTML file deployed to $DEPLOY_DIR"
else
    echo "❌ index.html not found in $TMP_DIR"
    exit 1
fi

# Step 3: Restart NGINX
sudo systemctl restart nginx
echo "🔁 NGINX restarted"

echo "🚀 Deployment completed!"