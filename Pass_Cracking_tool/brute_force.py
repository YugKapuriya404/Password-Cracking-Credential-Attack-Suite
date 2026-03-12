import itertools
import string
import time

TARGET_PASSWORD = "ab1"
CHARSET = string.ascii_lowercase + string.digits

def brute_force(target=TARGET_PASSWORD):
    attempts = 0
    start_time = time.time()

    for length in range(1, 6):
        for guess in itertools.product(CHARSET, repeat=length):
            attempts += 1
            if ''.join(guess) == target:
                print("  Password Found :", ''.join(guess))
                print("  Attempts       :", attempts)
                print("  Time Taken     :", round(time.time() - start_time, 3), "seconds")
                return ''.join(guess)

    print("  Password not found.")
    return None