# Database Backup Setup Guide

This guide provides instructions on how to automatically download and run a shell script (`setup.sh`) that sets up a cron job for backing up a SQLite database. The script schedules a Python script to run daily, which creates a backup of the database.

## Prerequisites

- A Unix-like operating system (Linux, macOS)
- `wget` installed on your system (for downloading the script)
- Access to the terminal or command line
- Basic familiarity with terminal commands

## Steps

### 1. Download the Setup Script

Open a terminal and navigate to the directory where you want to download the `setup.sh` script. Use the following command to download it:

```bash
wget https://raw.githubusercontent.com/sherlock6147/naive_db_backup/main/setup.sh
```

### 2. Make the Script Executable

Before running the script, you need to make it executable. You can do this by running the following command in your terminal:

```bash
chmod +x setup.sh
```

### 3. Run the Setup Script

Now that the script is executable, you can run it. This script will download the database backup Python script, make it executable, and set up a cron job to run it daily. Execute the script by running:

```bash
./setup.sh
```

### 4. Verify the Cron Job

To ensure that the cron job has been added successfully, you can list your crontab entries with the following command:

```bash
crontab -l
```

This command displays all cron jobs scheduled under your user account. Look for the newly added job that corresponds to the database backup script.

## Troubleshooting

- If you encounter permissions errors, ensure you have the necessary permissions in your current directory or try running the commands with `sudo`.
- Ensure you have `wget` installed. You can usually install it with your package manager, e.g., `apt-get install wget` on Debian/Ubuntu or `brew install wget` on macOS.
