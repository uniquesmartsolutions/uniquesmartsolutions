#!/usr/bin/env python3

import os
import time
import logging
import shutil
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DeviceBackupManager")

BACKUP_SOURCE = "/var/iot_devices/data"
BACKUP_DEST = "/mnt/backups/iot_devices"

def create_backup_dir():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(BACKUP_DEST, f"backup_{timestamp}")
    os.makedirs(backup_dir, exist_ok=True)
    return backup_dir

def backup_device_data():
    logger.info("Starting device data backup process.")
    backup_dir = create_backup_dir()
    if os.path.exists(BACKUP_SOURCE):
        shutil.copytree(BACKUP_SOURCE, os.path.join(backup_dir, "data"))
        logger.info(f"Device data backed up to {backup_dir}")
    else:
        logger.warning(f"Source directory {BACKUP_SOURCE} does not exist.")
    logger.info("Backup process completed.")

def main():
    logger.info("Device Backup Manager started.")
    backup_device_data()
    logger.info("Device Backup Manager completed.")

if __name__ == "__main__":
    main()
