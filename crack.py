import argparse
import hashlib
import os

good = "\033[92m[+]\033[0m"
bad = "\033[91m[-]\033[0m"
info = "\033[94m[*]\033[0m"


def dictionary_attack(hashvalue, hashtype, wordlist_file="wordlist.txt"):
    if not os.path.exists(wordlist_file):
        print(f"{bad} Wordlist file not found: {wordlist_file}")
        return None

    with open(wordlist_file, "r", encoding="latin-1") as f:
        for word in f:
            word = word.strip()
            if not word:
                continue
            hashed = hashlib.new(hashtype, word.encode()).hexdigest()
            if hashed == hashvalue:
                return word
    return None


api_sets = {
    32: "md5",
    40: "sha1",
    64: "sha256",
    96: "sha384",
    128: "sha512",
}

def crack_hash(hashvalue):
    htype = api_sets.get(len(hashvalue))
    if not htype:
        print(f"{bad} Unsupported hash length: {hashvalue}")
        return None

    print(f"{info} Trying {htype.upper()} for {hashvalue}")

    result = dictionary_attack(hashvalue, htype)
    if result:
        print(f"{good} (offline) {hashvalue} : {result}")
        return result
    else:
        print(f"{bad} Not found in wordlist: {hashvalue}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Offline Hash Cracker (Dictionary Attack)")
    parser.add_argument("-s", dest="hash", help="Single hash")
    parser.add_argument("-f", dest="file", help="File containing hashes")
    parser.add_argument("-w", dest="wordlist", default="wordlist.txt", help="Wordlist file (default: wordlist.txt)")
    args = parser.parse_args()

    if args.hash:
        crack_hash(args.hash)
    elif args.file:
        if not os.path.exists(args.file):
            print(f"{bad} Hash file not found: {args.file}")
            return
        with open(args.file, "r") as f:
            for line in f:
                h = line.strip()
                if h:
                    crack_hash(h)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
