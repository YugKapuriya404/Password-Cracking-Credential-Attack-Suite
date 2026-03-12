names   = ["admin", "user", "test"]
years   = ["1999", "2000", "2023", "2024"]
symbols = ["!", "@", "#"]

leet_map = {"a": "@", "e": "3", "i": "1", "o": "0", "s": "$"}

def leet_transform(word):
    for char, rep in leet_map.items():
        word = word.replace(char, rep)
    return word

def generate_dictionary():
    wordlist = set()

    for name in names:
        wordlist.add(name)
        wordlist.add(name.capitalize())

        for year in years:
            wordlist.add(name + year)
            wordlist.add(name.capitalize() + year)

        for sym in symbols:
            wordlist.add(name + sym)

        wordlist.add(leet_transform(name))

    return wordlist