#!/bin/bash
# This script runs the commit-check Python script

LOG_FILE="/var/log/cicd_commit_checker.log"
PY_SCRIPT="/home/ubuntu/check_for_new_commit.py"

echo "🕒 Running CI/CD check at $(date)" >> $LOG_FILE
/usr/bin/python3 $PY_SCRIPT >> $LOG_FILE 2>&1