#!/usr/bin/env python3

import os
import time
import logging
import random
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NetworkLatencyMonitor")

DEVICE_IPS = [f"192.168.1.{i}" for i in range(10, 60)]
LATENCY_LOG = "logs/network_latency_log.json"

def simulate_ping(ip):
    latency_ms = random.uniform(1, 200)
    logger.info(f"Ping to {ip}: {latency_ms:.2f} ms")
    return latency_ms

def collect_latency_data():
    logger.info("Starting network latency monitoring.")
    data = {}
    for ip in DEVICE_IPS:
        latency = simulate_ping(ip)
        data[ip] = latency
    os.makedirs("logs", exist_ok=True)
    with open(LATENCY_LOG, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Latency data written to {LATENCY_LOG}")

def main():
    logger.info("Network Latency Monitor started.")
    collect_latency_data()
    logger.info("Network Latency Monitor completed.")

if __name__ == "__main__":
    main()
