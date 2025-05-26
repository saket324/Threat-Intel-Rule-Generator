import json
import requests
from OTXv2 import OTXv2
from config import OTX_API_KEY

def fetch_otx_iocs():
    print("[*] Authenticating with OTX...")
    otx = OTXv2(OTX_API_KEY)

    print("[*] Fetching public threat indicators from OTX pulses...")

    try:
        # Use authenticated pulse subscription endpoint
        url = "https://otx.alienvault.com/api/v1/pulses/subscribed"
        headers = {"X-OTX-API-KEY": OTX_API_KEY}
        response = requests.get(url, headers=headers)
        data = response.json()
        pulses = data.get("results", [])
    except Exception as e:
        print(f"[!] Failed to fetch indicators: {e}")
        return

    iocs = {
        "ips": [],
        "domains": []
    }

    for pulse in pulses:
        indicators = pulse.get("indicators", [])
        for indicator in indicators:
            if indicator["type"] == "IPv4":
                iocs["ips"].append(indicator["indicator"])
            elif indicator["type"] == "domain":
                iocs["domains"].append(indicator["indicator"])

    print(f"[+] Extracted {len(iocs['ips'])} IPs and {len(iocs['domains'])} domains.")

    with open("outputs/raw_iocs.json", "w") as f:
        json.dump(iocs, f, indent=4)

    print("[+] IOC data saved to outputs/raw_iocs.json")

if __name__ == "__main__":
    fetch_otx_iocs()
