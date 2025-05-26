import json
import requests

# Load IOCs
with open("outputs/raw_iocs.json", "r") as f:
    raw_data = json.load(f)

enriched_data = {"ips": [], "domains": raw_data.get("domains", [])}

for entry in raw_data.get("ips", []):
    ip = entry["value"]

    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        info = response.json()

        enriched_ip = {
            "value": ip,
            "type": "ip",
            "source": entry["source"],
            "timestamp": entry["timestamp"],
            "city": info.get("city"),
            "region": info.get("region"),
            "country": info.get("country"),
            "org": info.get("org")
        }

        print(f"[+] Enriched: {ip}")
        enriched_data["ips"].append(enriched_ip)

    except Exception as e:
        print(f"[!] Failed to enrich {ip}: {e}")

# Save results
with open("outputs/enriched_iocs.json", "w") as f:
    json.dump(enriched_data, f, indent=4)

print("[+] Saved enriched IOCs to outputs/enriched_iocs.json")