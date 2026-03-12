import math
import string

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)
    return len(password) * math.log2(charset)

def analyze_password(password):
    score = 0
    if len(password) >= 8:                             score += 1
    if any(c.islower() for c in password):             score += 1
    if any(c.isupper() for c in password):             score += 1
    if any(c.isdigit() for c in password):             score += 1
    if any(c in string.punctuation for c in password): score += 1

    entropy = calculate_entropy(password)
    return score, round(entropy, 2)