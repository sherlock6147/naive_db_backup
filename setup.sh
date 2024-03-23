#!/bin/bash

# URL of the Python backup script
SCRIPT_URL="https://raw.githubusercontent.com/sherlock6147/naive_db_backup/main/db_backup.py"

# Destination directory where the backup script will be stored
DEST_DIR="~/.backups_utils"
mkdir -p "$DEST_DIR"

# File name for the backup script
SCRIPT_NAME="db_backup.py"
SCRIPT_PATH="$DEST_DIR/$SCRIPT_NAME"

# Path to your Python interpreter (adjust if necessary)
PYTHON_BIN="/usr/bin/python3"

# Log file for backup script output
LOG_FILE="~/,backups/logfile.log"

# Download the backup script
wget -O "$SCRIPT_PATH" "$SCRIPT_URL"

# Making the backup script executable
chmod +x "$SCRIPT_PATH"

# Backup line to remove existing cron job for the script, if any, to prevent duplicates
(crontab -l | grep -v "$SCRIPT_NAME" ; echo "0 2 * * * $PYTHON_BIN $SCRIPT_PATH >> $LOG_FILE 2>&1") | crontab -

# Confirmation message
echo "Cron job for the database backup script has been set up successfully."