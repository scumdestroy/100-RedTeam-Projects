import hashlib
import argparse
import multiprocessing
import time

def find_hash(target, hash_type, wordlist):
    start_time = time.time()
    hash_object = get_hash_object(hash_type)

    with open(wordlist, 'r') as file:
        lines = file.readlines()

    pool = multiprocessing.Pool()
    results = []

    for line in lines:
        word = line.strip()
        result = pool.apply_async(perform_hash, args=(word, target, hash_object))
        results.append(result)

    pool.close()
    pool.join()

    for result in results:
        hashed_word, hashed_value = result.get()
        if hashed_value == target:
            print(f"Hash found: {hashed_word}")
            break

    elapsed_time = time.time() - start_time
    print(f"Execution time: {elapsed_time} seconds")

def get_hash_object(hash_type):
    hash_type = hash_type.lower().replace("-", "")
    if hash_type == "sha1":
        return hashlib.sha1()
    elif hash_type == "sha256":
        return hashlib.sha256()
    elif hash_type == "md5":
        return hashlib.md5()
    else:
        raise ValueError("Invalid hash type")

def perform_hash(word, target, hash_object):
    hashed_word = hash_object.hexdigest()
    return word, hashed_word

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-threaded hash finder script")
    parser.add_argument("target", type=str, help="The target string to match")
    parser.add_argument("hash_type", type=str, help="The hash type to use (e.g., SHA-1, SHA-256, MD5)")
    parser.add_argument("wordlist", type=str, help="Path to the wordlist file")
    args = parser.parse_args()

    find_hash(args.target, args.hash_type, args.wordlist)
