# ⏰ Task 5: Crontab Setup

## 1. Make the Python script executable from anywhere
Ensure `check_for_new_commit.py` is executable and has correct path in the wrapper:
Example path: `/home/ubuntu/check_for_new_commit.py`

## 2. Create the Wrapper Script
Save and chmod the script:
```bash
chmod +x /home/ubuntu/run_commit_check.sh
```

## 3. Edit Crontab
```bash
crontab -e
```

## 4. Add this line to run every 5 minutes:
```
*/5 * * * * /home/ubuntu/run_commit_check.sh
```

## 5. View logs
```bash
tail -f /var/log/cicd_commit_checker.log
```

✅ This ensures your deployment pipeline runs automatically on new commits.