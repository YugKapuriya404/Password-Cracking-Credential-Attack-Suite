"""
main.py — Runs all modules automatically:
  1. dictionary_generator.py
  2. hash_extractor.py
  3. brute_force.py
  4. password_analyzer.py
  5. report_generator.py
"""

from dictionary_generator import generate_dictionary
from hash_extractor       import extract_hashes
from brute_force          import brute_force
from password_analyzer    import analyze_password
from report_generator     import generate_report

def main():
    print("\n" + "="*55)
    print("   PASSWORD SECURITY TOOLKIT - AUTO RUN")
    print("="*55)

    # --- Ask user for input ---
    TEST_PASSWORD = input("\n  Enter password to analyze : ")
    CRACK_TARGET  = input("  Enter password to crack   : ")
    print()

    # Step 1 — Dictionary Generator
    print("[STEP 1] Generating Dictionary...")
    wordlist = generate_dictionary()
    print(f"  Words generated : {len(wordlist)}")
    print(f"  Sample words    : {list(wordlist)[:5]}")

    # Step 2 — Hash Extraction
    print("\n[STEP 2] Extracting Password Hashes...")
    shadow_results, sam_results = extract_hashes()

    # Step 3 — Brute Force
    print(f"\n[STEP 3] Running Brute-Force on '{CRACK_TARGET}'...")
    cracked = brute_force(target=CRACK_TARGET)

    # Step 4 — Password Analyzer
    print(f"\n[STEP 4] Analyzing Password: '{TEST_PASSWORD}'")
    score, entropy = analyze_password(TEST_PASSWORD)
    print(f"  Score   : {score}/5")
    print(f"  Entropy : {entropy} bits")

    # Step 5 — Report Generator
    print(f"\n[STEP 5] Generating Report...")
    report = generate_report(
        password=TEST_PASSWORD,
        score=score,
        entropy=entropy,
        wordlist=wordlist,
        cracked=cracked
    )
    print(report)

    # Save report to file
    with open("audit_report.txt", "w") as f:
        f.write(report)
    print("  Report saved to: audit_report.txt")

if __name__ == "__main__":
    main()