#!/usr/bin/env python3
"""
DNS OSINT Reconnaissance Script
Educational use only – query only targets you own or have permission to test.
"""

import dns.resolver

# ── Helper to safely query a DNS record ──────────────────────────────
def query_dns(domain: str, record_type: str) -> None:
    """Try to resolve 'record_type' for 'domain' and print results."""
    print(f"\n[+] {record_type} records for {domain}:")
    try:
        answers = dns.resolver.resolve(domain, record_type)
        for rdata in answers:
            # rdata.to_text() gives a clean string representation
            print(f"  {rdata.to_text()}")
    except dns.resolver.NoAnswer:
        print("  No records of this type.")
    except dns.resolver.NXDOMAIN:
        print("  Domain does not exist – check spelling.")
    except dns.resolver.Timeout:
        print("  Query timed out. The DNS server might be unreachable.")
    except Exception as e:
        print(f"  Unexpected error: {e}")

# ── Main routine ─────────────────────────────────────────────────────
def main():
    print("=" * 65)
    print(" DNS OSINT Tool – MX, TXT, A, AAAA, NS, SOA, CNAME lookup")
    print("=" * 65)
    print("Enter 'quit' to exit.\n")

    while True:
        # Get target domain
        domain = input("Target domain (e.g., example.com): ").strip()
        if domain.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if not domain:
            continue   # empty input, ask again

        # Perform the lookups
        query_dns(domain, "A")     # IPv4 address
        query_dns(domain, "AAAA")  # IPv6 address
        query_dns(domain, "MX")    # Mail servers
        query_dns(domain, "TXT")   # Text records (SPF, DKIM, etc.)
        query_dns(domain, "NS")    # Name Servers
        query_dns(domain, "SOA")   # Start of Authority
        query_dns(domain, "CNAME") # Canonical Name (Aliases)
        
        print("\n" + "-" * 65)

if __name__ == "__main__":
    main()
      
