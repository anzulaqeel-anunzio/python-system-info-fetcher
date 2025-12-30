# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import platform
import os
import sys
import psutil # We need to check if user has this, otherwise fallback or error gracefully. 
              # For this project, I'll stick to standard library to ensure zero-dependency,
              # effectively making it a "Basic System Info Fetcher".
              # Wait, standard lib platform module is quite good.

class SystemInfo:
    def get_info(self):
        info = {
            "OS": platform.system(),
            "OS Release": platform.release(),
            "OS Version": platform.version(),
            "Architecture": platform.machine(),
            "Hostname": platform.node(),
            "Processor": platform.processor(),
            "Python Version": sys.version.split()[0],
            "CPU Cores": os.cpu_count()
        }
        
        # Try to get more if on Linux/Unix
        try:
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    if "MemTotal" in line:
                        mem_kb = int(line.split()[1])
                        info["Total Memory"] = f"{mem_kb / 1024 / 1024:.2f} GB"
                        break
        except FileNotFoundError:
            info["Total Memory"] = "Unknown (psutil not installed)"

        return info

    def format_output(self, info):
        lines = []
        lines.append("=" * 40)
        lines.append("SYSTEM INFORMATION")
        lines.append("=" * 40)
        for k, v in info.items():
            lines.append(f"{k:<15}: {v}")
        lines.append("-" * 40)
        return "\n".join(lines)

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
