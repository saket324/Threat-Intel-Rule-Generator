# Threat-Intel-Rule-Generator
Pulls IOCs from threat feeds and generates SIEM-ready detection rules

# How this works

- Fetches live IOCs (IPs and domains from AlienVault OTX and other open feeds)
- Enriches IPs using [ipinfo.io](https://ipinfo.io) and gathers data such as geolocation, ISP and organization details
- Outputs:
  - `raw_iocs.json`: Raw indicators from public threat feeds
  - `enriched_iocs.json`: Enriched IP indicators
  - `splunk_rules.spl`: SIEM detection query in Splunk format

# MITRE ATT&CK Mapping

- **T1589.003** – Gather Victim Network Information: IP Addresses  
- **T1071.001** – Application Layer Protocol: Web Traffic  
- **T1057** – Process Discovery (Mapped from observed IOC usage patterns)

# To Run

```bash
pip install -r requirements.txt

python otx_fetcher.py        # Pulls IOCs from live sources
python ioc_enricher.py       # Adds enrichment from ipinfo.io
python rule_generator.py     # Generates SIEM-ready Splunk rules