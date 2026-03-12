# Password Cracking & Credential Attack Suite 🔐

A practical educational toolkit for password policy testing and credential security analysis.

> ⚠️ **Ethical Use Only** — Authorized environments only. Unauthorized use is illegal.

---

## 📌 Project Overview

This toolkit simulates real-world password attacks in a safe lab environment to help
understand how passwords are stored, hashed, and cracked. It supports dictionary
generation, hash extraction, brute force simulation, password strength analysis,
and audit report generation.

---

## 📁 Project Structure

| File | Module | Function |
|------|--------|----------|
| `main.py` | Automation | Runs all modules in order |
| `dictionary_generator.py` | Dictionary Generator | Generates password wordlist with mutations |
| `hash_extractor.py` | Hash Extractor | Extracts and identifies system hashes |
| `brute_force.py` | Brute Force Simulator | Cracks passwords via iteration |
| `password_analyzer.py` | Password Analyzer | Scores strength and calculates entropy |
| `report_generator.py` | Report Generator | Saves audit_report.txt |

---

## ⚙️ How It Works

1. User enters a password to **analyze** and a password to **crack**
2. Dictionary Generator creates a wordlist with leet-speak mutations
3. Hash Extractor detects OS and reads real system hashes
4. Brute Force Simulator tries all combinations against the target
5. Password Analyzer scores strength (0–5) and calculates entropy
6. Report Generator saves all results to `audit_report.txt`

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming language |
| `itertools` | Brute-force character combinations |
| `hashlib` | MD5, SHA-1, SHA-256, SHA-512 hashing |
| `math` | Entropy calculation |
| `platform` | OS detection (Linux / Windows) |

---

## 🚀 How to Run

**Step 1 — Place all 6 files in the same folder**

**Step 2 — Open terminal and run:**
```bash
python main.py
```

**Step 3 — Follow the prompts:**
```
Enter password to analyze : Admin@2024
Enter password to crack   : ab1
```

**Step 4 — View results in terminal and check `audit_report.txt`**

---

## 📊 Sample Output
```
MODULE 4 — PASSWORD ANALYZER
Password : Admin@2024
Score    : 5/5
Entropy  : 52.6 bits
Rating   : Very Strong
```

---

## 🔒 Security Notes

| Algorithm | Rating | Notes |
|-----------|--------|-------|
| MD5 | WEAK | Cracked in seconds, no salt |
| NTLM | WEAK | GPU-accelerated cracking |
| SHA-256 | MEDIUM | Better but aging |
| SHA-512 | GOOD | Salted, slow enough |
| Bcrypt | STRONG | Best for passwords |

---

## ⚖️ Legal Disclaimer

This toolkit is designed exclusively for:
- Authorized penetration testing with written permission
- Educational cybersecurity lab environments
- Security auditing of systems you own

Unauthorized use is illegal under **CFAA**, **UK Computer Misuse Act**, and equivalent laws.

---

## 👤 Author

**Yug Kapuriya**
- LinkedIn: Yug Kapuriya
- Email: yugkapuriya404@gmail.com
