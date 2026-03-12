from datetime import datetime

def generate_report(password=None, score=None, entropy=None, wordlist=None, cracked=None):
    report = []
    report.append("=" * 45)
    report.append("   PASSWORD SECURITY AUDIT REPORT")
    report.append("=" * 45)
    report.append(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if wordlist is not None:
        report.append(f"\n  [Dictionary Generator]")
        report.append(f"  Total words generated : {len(wordlist)}")
        report.append(f"  Sample words          : {list(wordlist)[:5]}")

    if cracked is not None:
        report.append(f"\n  [Brute Force Result]")
        report.append(f"  Password cracked      : {cracked}")

    if password and score is not None and entropy is not None:
        report.append(f"\n  [Password Analysis]")
        report.append(f"  Password              : {password}")
        report.append(f"  Strength Score        : {score}/5")
        report.append(f"  Entropy               : {entropy} bits")
        if   score == 5: rating = "Very Strong "
        elif score >= 3: rating = "Moderate "
        else:            rating = "Weak "
        report.append(f"  Rating                : {rating}")

    report.append(f"\n  [Recommendations]")
    report.append(f"  - Weak passwords are vulnerable to brute-force attacks.")
    report.append(f"  - Use long, complex passwords (12+ characters).")
    report.append(f"  - Avoid predictable patterns like names or years.")
    report.append(f"  - Use a password manager.")
    report.append("=" * 45)

    return "\n".join(report)