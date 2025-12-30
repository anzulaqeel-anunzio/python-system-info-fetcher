# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fetcher.core import SystemInfo

def main():
    parser = argparse.ArgumentParser(description="System Info Fetcher CLI")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON (useful for piping)")
    
    args = parser.parse_args()

    fetcher = SystemInfo()
    data = fetcher.get_info()

    if args.json:
        import json
        print(json.dumps(data, indent=4))
    else:
        print(fetcher.format_output(data))

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
