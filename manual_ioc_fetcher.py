import requests
import json
import csv
from utils import build_ioc_entry

def fetch_feodo_ips():
    url = "https://feodotracker.abuse.ch/downloads/ipblocklist.json"
    response = requests.get(url)
    lines = response.text.splitlines()

    ips = []
    for line in lines:
        if line.strip() and not line.startswith("#"):
            ips.append(line.strip())
    return ips

def fetch_urlhaus_domains():
    url = "https://urlhaus.abuse.ch/downloads/csv_online/"
    response = requests.get(url)
    lines = response.content.decode("utf-8").splitlines()

    domains = set()
    reader = csv.reader(lines)
    for row in reader:
        if not row or row[0].startswith("#"):
            continue
        try:
            url = row[2]
            domain = url.split("/")[2]
            domains.add(domain)
        except Exception:
            continue
    return list(domains)

def fetch_all_iocs():
    all_iocs = {"ips": [], "domains": []}

    feodo_ips = fetch_feodo_ips()
    for ip in feodo_ips:
        all_iocs["ips"].append(build_ioc_entry(ip, "ip", "Feodo Tracker"))

    urlhaus_domains = fetch_urlhaus_domains()
    for domain in urlhaus_domains:
        all_iocs["domains"].append(build_ioc_entry(domain, "domain", "URLhaus"))

    with open("outputs/raw_iocs.json", "w") as f:
        json.dump(all_iocs, f, indent=4)

    print(f"[+] Saved {len(all_iocs['ips'])} IPs and {len(all_iocs['domains'])} domains to raw_iocs.json")

if __name__ == "__main__":
    fetch_all_iocs()