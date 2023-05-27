import bcrypt
import json
import click
from getpass import getpass

PASSWORD_FILE = 'passwords.json'
MASTER_PASSWORD_FILE = 'master_password.txt'

# Function to encrypt the master password using bcrypt
def encrypt_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

# Function to verify the master password
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Function to save the encrypted master password to a file
def save_master_password(hashed_password):
    with open(MASTER_PASSWORD_FILE, 'wb') as file:
        file.write(hashed_password)

# Function to load the encrypted master password from a file
def load_master_password():
    with open(MASTER_PASSWORD_FILE, 'rb') as file:
        hashed_password = file.read()
    return hashed_password

# Function to save passwords associated with URLs to a JSON file
def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file)

# Function to load passwords from the JSON file
def load_passwords():
    try:
        with open(PASSWORD_FILE, 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    return passwords

# Command to set the master password
@click.command()
def set_master_password():
    hashed_password = load_master_password()

    if hashed_password:
        click.echo("Master password already set.")
    else:
        while True:
            master_password = getpass("Enter the master password: ")
            confirm_password = getpass("Confirm the master password: ")

            if master_password == confirm_password:
                hashed_password = encrypt_password(master_password)
                save_master_password(hashed_password)
                click.echo("Master password set successfully.")
                break
            else:
                click.echo("Passwords do not match. Try again.")

# Command to add a password
@click.command()
@click.option('--url', prompt=True, help='The URL associated with the password')
def add_password(url):
    hashed_password = load_master_password()
    passwords = load_passwords()

    if not hashed_password:
        click.echo("No master password found. Please set the master password first.")
        return

    entered_password = getpass("Enter the master password: ")
    if not verify_password(entered_password, hashed_password):
        click.echo("Incorrect password. Access denied.")
        return

    password = getpass("Enter the password: ")
    passwords[url] = password
    save_passwords(passwords)
    click.echo("Password saved successfully.")

# Command to retrieve a password
@click.command()
@click.option('--url', prompt=True, help='The URL associated with the password')
def get_password(url):
    hashed_password = load_master_password()
    passwords = load_passwords()

    if not hashed_password:
        click.echo("No master password found. Please set the master password first.")
        return

    entered_password = getpass("Enter the master password: ")
    if not verify_password(entered_password, hashed_password):
        click.echo("Incorrect password. Access denied.")
        return

    if url in passwords:
        click.echo(f"Password for {url}: {passwords[url]}")
    else:
        click.echo("Password not found.")

# Command to list all passwords
@click.command()
def list_passwords():
    hashed_password = load_master_password()
    passwords = load_passwords()

    if not hashed_password:
        click.echo("No master password found. Please set the master password first.")
        return

    entered_password = getpass("Enter the master password: ")
    if not verify_password(entered_password, hashed_password):
        click.echo("Incorrect password. Access denied.")
        return

    if passwords:
        click.echo("List of saved passwords:")
        for url, password in passwords.items():
            click.echo(f"URL: {url}, Password: {password}")
    else:
        click.echo("No passwords saved.")

# Grouping commands
@click.group()
def password_manager():
    pass

password_manager.add_command(set_master_password)
password_manager.add_command(add_password)
password_manager.add_command(get_password)
password_manager.add_command(list_passwords)

if __name__ == '__main__':
    password_manager()
