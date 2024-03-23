import os
import shutil
from datetime import datetime, timedelta

DB_PATH = '~/website/db.sqlite3'
BACKUP_DIR = '~/.revisions'
MAX_DAILY_BACKUPS = 7
MAX_MONTHLY_BACKUPS = 3

def backup_database(db_path, backup_dir, is_monthly=False):
    # Create backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Format backup filename
    timestamp = datetime.now().strftime("%Y-%m-%d")
    backup_filename = f"backup_{timestamp}{'_monthly' if is_monthly else ''}.db"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    # Copy the database file
    shutil.copy2(db_path, backup_path)
    print(f"Database backed up to {backup_path}")

def cleanup_old_backups(backup_dir, max_backups, is_monthly=False):
    # List all backup files
    backups = [f for f in os.listdir(backup_dir) if f.endswith('_monthly.db' if is_monthly else '.db')]
    backups.sort(reverse=True)
    
    # Remove oldest backups beyond max_backups limit
    for backup in backups[max_backups:]:
        os.remove(os.path.join(backup_dir, backup))
        print(f"Old backup removed: {backup}")

def perform_backups():
    # Backup database daily
    backup_database(DB_PATH, BACKUP_DIR)
    cleanup_old_backups(BACKUP_DIR, MAX_DAILY_BACKUPS)
    
    # Check if first day of the month for monthly backup
    today = datetime.now()
    if today.day == 1:
        backup_database(DB_PATH, BACKUP_DIR, is_monthly=True)
        cleanup_old_backups(BACKUP_DIR, MAX_MONTHLY_BACKUPS, is_monthly=True)

if __name__ == "__main__":
    perform_backups()
