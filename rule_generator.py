import json
from utils.mitre_mapping import MITRE_MAP

def generate_splunk_rules():
    with open("outputs/enriched_iocs.json", "r") as f:
        data = json.load(f)

    rules = []
    mitre_refs = set()

    # Generate rules for IPs
    if "ips" in data and data["ips"]:
        rules.extend([f"src_ip={ip}" for ip in data["ips"]])
        mitre_refs.update(MITRE_MAP["IPv4"].keys())

    # Generate rules for domains
    if "domains" in data and data["domains"]:
        rules.extend([f'domain="{domain}"' for domain in data["domains"]])
        mitre_refs.update(MITRE_MAP["domain"].keys())

    # Join rules
    spl_query = " OR ".join(rules)

    with open("outputs/splunk_rules.spl", "w") as f:
        f.write(spl_query + "\n\n")
        f.write("# MITRE ATT&CK Techniques:\n")
        for tid in mitre_refs:
            # Look up in either IPv4 or domain map
            description = MITRE_MAP["IPv4"].get(tid) or MITRE_MAP["domain"].get(tid)
            f.write(f"# {tid}: {description}\n")

    print("[*] SPL rules and MITRE mappings saved to outputs/splunk_rules.spl")

if __name__ == "__main__":
    generate_splunk_rules()
