# Ted-CLI: Terminal Password Manager

Ted-CLI is a command-line password manager that allows you to securely store and retrieve passwords associated with different URLs. 

## Installation
#### Clone the repository from GitHub:

```bash
git clone https://github.com/mehdi-alouane/ted-cli
```
Change to the project directory:

```bash
cd ted-cli
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

#### Available Commands
The following commands are available in Ted-CLI:

##### Set Master Password
This command sets the master password used to encrypt and decrypt your stored passwords.

```bash
python main.py set-master-password
```
You will be prompted to enter and confirm your master password. Make sure to remember this password as it will be required for accessing your passwords later.

#### Add Password
This command allows you to add a new password for a specific URL.

```sql
python main.py add-password --url <URL>
```
You will be prompted to enter your master password and the password associated with the URL. The password will be securely stored and encrypted.

#### Get Password
This command retrieves the password associated with a specific URL.

```sql
python main.py get-password --url <URL>
```

You will be prompted to enter your master password. If the password is correct, the stored password for the given URL will be displayed.

#### List Passwords
This command lists all the stored passwords and their associated URLs.

```
python main.py list-passwords
```
You will be prompted to enter your master password. If the password is correct, a list of all saved passwords will be displayed.

Usage Example
Here's an example of how to use Ted-CLI:

Set the master password:

```arduino
python main.py set-master-password
```

Add a password for a URL:

```sql
python main.py add-password --url example.com
```
Enter your master password and the password associated with example.com.

#### Retrieve the password for a URL:
```sql
python main.py get-password --url example.com
```
Enter your master password. If correct, the stored password for example.com will be displayed.

#### List all saved passwords:

```bash
python main.py list-passwords
```
Enter your master password. A list of all saved passwords and their associated URLs will be displayed.