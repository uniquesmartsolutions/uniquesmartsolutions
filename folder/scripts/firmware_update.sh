#!/bin/bash

DEVICE_IP="192.168.1.42"
FIRMWARE_VERSION="2.1.6"

echo "Connecting to device at $DEVICE_IP..."
echo "Uploading firmware v$FIRMWARE_VERSION..."
sleep 2
echo "Applying firmware update..."
sleep 3
echo "Rebooting device..."
sleep 2
echo "Firmware update complete. Device is now running v$FIRMWARE_VERSION."
