import bcrypt
import json
from getpass import getpass

# Function to encrypt the master password using bcrypt
def encrypt_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

# Function to verify the master password
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Function to save the encrypted master password to a file
def save_master_password(hashed_password):
    with open('master_password.txt', 'wb') as file:
        file.write(hashed_password)

# Function to load the encrypted master password from a file
def load_master_password():
    with open('master_password.txt', 'rb') as file:
        hashed_password = file.read()
    return hashed_password

# Function to save passwords associated with URLs to a JSON file
def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

# Function to load passwords from the JSON file
def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    return passwords

# Main function to manage passwords
def manage_passwords():
    try:
        hashed_password = load_master_password()
        passwords = load_passwords()
    except FileNotFoundError:
        hashed_password = None
        passwords = {}

    if not hashed_password:
        print("No master password found. Let's set a new one.")
        while True:
            master_password = getpass("Enter the master password: ")
            confirm_password = getpass("Confirm the master password: ")
            if master_password == confirm_password:
                hashed_password = encrypt_password(master_password)
                save_master_password(hashed_password)
                break
            else:
                print("Passwords do not match. Try again.")
    
    while True:
        entered_password = getpass("Enter the master password to continue: ")
        if verify_password(entered_password, hashed_password):
            print("Access granted.")
            break
        else:
            print("Incorrect password. Try again.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Save a password")
        print("2. Retrieve a password")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            url = input("Enter the URL: ")
            password = getpass("Enter the password: ")
            passwords[url] = password
            save_passwords(passwords)
            print("Password saved successfully!")

        elif choice == '2':
            url = input("Enter the URL to retrieve the password: ")
            if url in passwords:
                print(f"Password for {url}: {passwords[url]}")
            else:
                print("Password not found.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    manage_passwords()
