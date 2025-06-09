#!/usr/bin/env python3

import json
import uuid

device_config = {
    "device_id": str(uuid.uuid4()),
    "hostname": "dashboard1",
    "ip_address": "192.168.1.42",
    "ssh_port": 2222,
    "username": "admin",
    "password": "admin",
    "firmware_version": "2.1.5",
    "features": ["lighting_control", "thermostat_control", "printer_control", "appliances_control"]
}

with open("lighting_node_config.json", "w") as f:
    json.dump(device_config, f, indent=4)

print("Device configuration generated: dashboard_config.json")
