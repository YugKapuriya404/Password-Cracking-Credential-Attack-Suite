import os
import platform
import subprocess

def get_algorithm(h):
    if h.startswith("$6$"): return "SHA-512"
    if h.startswith("$5$"): return "SHA-256"
    if h.startswith("$1$"): return "MD5"
    if h in ("*", "!", "x"): return "Locked"
    if len(h) == 32:         return "NTLM"
    return "Unknown"

def extract_hashes():
    print("\n" + "="*45)
    print("   HASH EXTRACTION MODULE")
    print(f"   OS: {platform.system()}")
    print("="*45)

    if platform.system() == "Linux":
        try:
            with open("/etc/shadow", "r") as f:
                print(f"\n  {'Username':<15} {'Algorithm':<12} {'Hash'}")
                print("  " + "-"*40)
                for line in f:
                    p = line.strip().split(":")
                    if len(p) >= 2:
                        print(f"  {p[0]:<15} {get_algorithm(p[1]):<12} {p[1][:20]}...")
        except PermissionError:
            print("  Run as root to read /etc/shadow.")

    elif platform.system() == "Windows":
        result = subprocess.run(
            ["wmic", "useraccount", "get", "name,sid,disabled"],
            capture_output=True, text=True
        )
        print(f"\n  {'Username':<20} {'SID':<40} {'Status'}")
        print("  " + "-"*65)
        for line in result.stdout.strip().split("\n")[1:]:
            p = line.split()
            if len(p) >= 2:
                status = "Disabled" if p[0] == "TRUE" else "Active"
                print(f"  {p[-1]:<20} {' '.join(p[1:-1]):<40} {status}")

    else:
        print("  OS not supported.")

    print("="*45)
    return [], []