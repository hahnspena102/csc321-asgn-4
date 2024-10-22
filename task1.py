import hashlib
import random
import string
import time

def sha256_hash(input_string):
    input_bytes = input_string.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(input_bytes)

    return sha256.hexdigest()

def truncate_hash(hash_string, bits):
    #Take the first (bits / 4) characters of hash_string
    truncated_bits = bits // 4
    truncated_hash_str = hash_string[:truncated_bits]

    #Convert this substring to an integer (base 16)
    truncated_hash_int = int(truncated_hash_str, 16)

    #Create a bitmask of 'bits' number of 1s
    bitmask = (1 << bits) - 1

    #Perform bitwise AND between the integer and the bitmask
    bitwised = truncated_hash_int & bitmask

    #Return the result
    return bitwised

def hamming_distance(s1, s2):
    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            count += 1
    return count

def find_hamming_distance_1():
    base = generate_random_str()
    print(base)
    for i in range(len(base)):
        modified_char = chr(ord(base[i]) ^ (1 << i))
        modified = base[:i] + modified_char + base[i+1:]
        if hamming_distance(base, modified) == 1:
            return base, modified
    return None, None

def find_collision(bits, max_attempts):
    seen = {}
    start_time = time.time()
    for attempt in range(max_attempts):
        s = generate_random_str()
        h = truncate_hash(sha256_hash(s), bits)
        if seen.get(h):
            end_time = time.time()
            elapsed_time = end_time - start_time
            return seen[h], s, attempt, elapsed_time
        else:
            seen[h] = s
    end_time = time.time()
    elapsed_time = end_time - start_time
    return None, None, max_attempts, elapsed_time


def generate_random_str():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))


def task_1a():
    print("Task 1a: SHA256 hashes of arbitrary inputs")
    test_input = ["Hello, World!", "Python", "Cryptography"]
    for inp in test_input:
        hashed = sha256_hash(inp)
        print(f"Input: {inp}, Hashed: {hashed}")

def task_1b():
    print("Task 1b: Strings with Hamming Distance of 1")
    
    for i in range(3):
        strings = find_hamming_distance_1()
        hash1 = sha256_hash(strings[0])
        hash2 = sha256_hash(strings[1])
        print(f"s1: {strings[0]}, s2: {strings[1]}, h1: {hash1}, h2: {hash2}")

def task_1c():
    print("Task 1c: Finding collisions for truncated hashes")
    bits = range(8, 51)
    time = []
    inputs = []

    for b in bits:
        collision = find_collision(b, 1000000000000)
        time.append(collision[3])
        inputs.append((collision[0],collision[1]))

    print("Bits\tTime\t\t\tInputs")
    for i in range(len(bits)):
        print(f"{bits[i]}\t{time[i]}\t{inputs[i]}")
    
    

if __name__ == "__main__":
    task_1a()
    print()
    task_1b()
    print()
    task_1c()
    


