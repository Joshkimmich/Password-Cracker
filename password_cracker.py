import hashlib
import itertools
import string
import time

# Getting user input instead of hardcoded password
target_hash = input("Enter the SHA-256 hash to crack: ").strip()

# Character set and max password length
charset = "abcdefghijklmnopqrstuvwxyz"
max_length = 6

# Function: Generate Hash
def generate_hash():
    password = input("Enter the plaintext password to hash: ").strip()
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    print(f"\n[🔒] SHA-256 hash of '{password}':\n{hash_value}\n")
    return hash_value

# Function: Brute-Force attack
def brute_force_sha256(target_hash, charset, max_length):
    print(f"Target SHA-256 Hash: {target_hash}")
    start_time = time.time()
    attempts = 0
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_word = ''.join(guess)
            guess_hash = hashlib.sha256(guess_word.encode()).hexdigest()
            attempts += 1
            
            if guess_hash == target_hash:
                end_time = time.time()
                print(f"[✅] Password found: {guess_word}")
                print(f"[⏱️] Attempts: {attempts}")
                print(f"[⌛] Time taken: {end_time - start_time:.2f} seconds")
                return guess_word
            
    print("[-] Password not found.")
    return None

# Function: Dictionary Attack
def dictionary_attack(target_hash, wordlist_path = "wordlist.txt"):
    print(f"\n[🧾] Starting dictionary attack using {wordlist_path}....")
    
    try:
        with open(wordlist_path, "r", encoding="utf-8") as file:
            start_time = time.time()
            attempts = 0
            for word in file:
                word = word.strip() # Clean up extra spaces
                hashed_word = hashlib.sha256(word.encode()).hexdigest() # Hash the word
                attempts += 1 # Count the attempts
                
                if hashed_word == target_hash: # Check if the hash matches
                    end_time = time.time()
                    print(f"[✅] Password found: {word}")
                    print(f"[📚] Attempts: {attempts}")
                    print (f"[⌛] Time taken: {end_time - start_time:.2f} seconds")
                    return word
                
        print("[-] Password not found in wordlist.\n")
    except FileNotFoundError: # If the wordlist doesn't exist
        print ("❌ Wordlist file not found.")
    return None

    
# MAIN Program               
if __name__ == "__main__":
    # Ask user if they want brute-force or dictionary attack
    print("📌 Password Cracker Tool (SHA-256)\n")
    print("Choose an option:")
    print("1 - Generate SHA-256 hash from a password")
    print("2 - Crack a SHA-256 hash")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        generate_hash()
        
    elif choice == "2":    
        target_hash = input("Enter the SHA-256 hash to crack: ").strip()
        print("\nSelect cracking method:")
        print("1 - Brute-force attack (slow,short passowrds only)")
        print("2 - Dictionary attack (uses wordlist.txt) ")  
        method = input("Choose attack method - (1) Brute-force (2) Dictionary: ").strip()
    
    if method == "1":
        brute_force_sha256(target_hash, charset, max_length)
    elif method == "2":
        dictionary_attack(target_hash, "wordlist.txt")
    else:
        print("❌ Invalid option selected.")
        
else:
    print("Invalid option. Exiting.")        
        
        