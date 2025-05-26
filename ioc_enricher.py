import json
import requests

# Load raw IOCs
with open("outputs/raw_iocs.json", "r") as f:
    data = json.load(f)

enriched_data = {"ips": [], "domains": data["domains"]}  # untouched domains for now

# Enrich IPs with ipinfo
for ip in data["ips"]:
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        info = response.json()

        enriched_ip = {
            "ip": ip,
            "city": info.get("city"),
            "region": info.get("region"),
            "country": info.get("country"),
            "org": info.get("org"),
        }
        print(f"[+] Enriched: {ip}")
        enriched_data["ips"].append(enriched_ip)
    except Exception as e:
        print(f"[!] Failed to enrich {ip}: {e}")

# Save enriched data
with open("outputs/enriched_iocs.json", "w") as f:
    json.dump(enriched_data, f, indent=4)

print("[+] Enriched IOCs saved to outputs/enriched_iocs.json")