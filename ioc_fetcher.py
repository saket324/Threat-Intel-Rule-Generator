import requests
import json

# Simulate threat IOC feed (AbuseIPDB, OTX etc.) 
simulated_iocs = {
    "ips": [
        "45.143.203.10",
        "103.75.201.2",
        "185.220.101.4",
        "209.141.38.71"
    ],
    "domains": [
        "malicious-example.com",
        "badsite.biz",
        "phishy.click"
    ]
}

# Save raw IOCs
with open("outputs/raw_iocs.json", "w") as f:
    json.dump(simulated_iocs, f, indent=4)

print("[+] Raw IOCs saved to outputs/raw_iocs.json")