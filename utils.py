from datetime import datetime

def build_ioc_entry(value, ioc_type, source):
    return {
        "value": value,
        "type": ioc_type,
        "source": source,
        "timestamp": datetime.utcnow().isoformat()
    }
