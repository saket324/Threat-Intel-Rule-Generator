import json

# Load enriched IOCs
with open("outputs/enriched_iocs.json", "r") as f:
    data = json.load(f)

ips = [entry["ip"] for entry in data["ips"]]

# Splunk query
splunk_query = " OR ".join([f"src_ip={ip}" for ip in ips])

# Save to file
with open("outputs/splunk_rules.spl", "w") as f:
    f.write(splunk_query)

print("[+] Splunk detection rule generated in outputs/splunk_rules.spl")