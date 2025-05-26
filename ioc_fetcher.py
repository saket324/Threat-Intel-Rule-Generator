import requests
import json

# Feodo Tracker JSON Feed (botnet IPs)
FEED_URL = "https://feodotracker.abuse.ch/downloads/ipblocklist.json"

def fetch_iocs():
    response = requests.get(FEED_URL)
    lines = response.text.splitlines()

    ips = []
    for line in lines:
        if line.startswith("#") or not line.strip():
            continue
        ips.append(line.strip())

    data = {
        "ips": ips[:20],  # limit for testing
        "domains": []     # could add real domain feed later
    }

    with open("outputs/raw_iocs.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"[+] Fetched {len(data['ips'])} IPs from live feed.")

if __name__ == "__main__":
    fetch_iocs()
