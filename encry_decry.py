from cryptography.fernet import Fernet

# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Function to load the key from a file
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("[!] Key file not found. Generating a new key...")
        return generate_key()

# Function to encrypt a file
def encrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"[✔] File encrypted successfully: {encrypted_file_path}")

# Function to decrypt a file
def decrypt_file(file_path, key):
    cipher = Fernet(key)
    try:
        with open(file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        decrypted_file_path = file_path.replace(".enc", "_decrypted")
        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        print(f"[✔] File decrypted successfully: {decrypted_file_path}")
    except Exception as e:
        print(f"[X] Decryption failed: {str(e)}")

# Main function
def main():
    key = load_key()
    print(f"[!] Your encryption key (Keep it safe!): {key.decode()}\n")
    
    print("[1] Encrypt a File")
    print("[2] Decrypt a File")
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        file_path = input("Enter file path to encrypt: ").strip()
        encrypt_file(file_path, key)
    elif choice == "2":
        file_path = input("Enter encrypted file path: ").strip()
        decrypt_file(file_path, key)
    else:
        print("[X] Invalid choice! Exiting.")

if __name__ == "__main__":
    main()
