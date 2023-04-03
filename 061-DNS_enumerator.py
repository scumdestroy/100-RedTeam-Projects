import dns.resolver

def enumerate_dns_records(domain):
    """Enumerate DNS records for a given domain."""
    records = {}

    # Get the A records for the domain
    a_records = []
    try:
        answers = dns.resolver.query(domain, "A")
        for rdata in answers:
            a_records.append(str(rdata))
        records["A"] = a_records
    except dns.resolver.NXDOMAIN:
        pass

    # Get the MX records for the domain
    mx_records = []
    try:
        answers = dns.resolver.query(domain, "MX")
        for rdata in answers:
            mx_records.append(str(rdata.exchange))
        records["MX"] = mx_records
    except dns.resolver.NoAnswer:
        pass

    # Get the NS records for the domain
    ns_records = []
    try:
        answers = dns.resolver.query(domain, "NS")
        for rdata in answers:
            ns_records.append(str(rdata))
        records["NS"] = ns_records
    except dns.resolver.NoAnswer:
        pass

    # Get the TXT records for the domain
    txt_records = []
    try:
        answers = dns.resolver.query(domain, "TXT")
        for rdata in answers:
            txt_records.append(str(rdata))
        records["TXT"] = txt_records
    except dns.resolver.NoAnswer:
        pass

    return records

if __name__ == "__main__":
    # Enumerate DNS records for example.com
    domain = "example.com"
    records = enumerate_dns_records(domain)
    print(f"DNS records for {domain}:")
    for record_type, record_data in records.items():
        print(f"{record_type} records: {', '.join(record_data)}")
