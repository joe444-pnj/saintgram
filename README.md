# Saintgram

Saintgram is a Python tool that allows you to fetch Instagram user information, including obfuscated emails and phone numbers, as well as follower and following lists.

## Features

- Retrieve basic account information, such as username, ID, follower count, and more.
- Fetch obfuscated email addresses and phone numbers.
- List followers and following accounts with contact information.
- Supports command-line interface.

## Note: 
The tool requires the user to be friends with the victim account or public target account in order to fetch any private or sensitive data, including followers, following lists, obfuscated emails, and phone numbers.

## Installation

1. Clone the repository:
   ```bash
   :git clone https://github.com/joe444-pnj/saintgram.git
   :cd saintgram

2. Install the required packages:
  ```bash
  pip install -r requirements.txt
   ```

## Usage Example
1. Retrieving User Information: To retrieve basic user information like username, ID, followers, following count, and obfuscated contact details (if available), use the -i option:
```bash
python saintgram.py -s <sessionID> -u <username> -o i
```
Example:

```bash
python saintgram.py -s 1234567890%3aABCDEF%3a1234567890 -u johndoe -o i
```
This command retrieves and displays user information for the Instagram account with the username johndoe.


2. Listing Followers: To list followers of a specific user:

```bash
python saintgram.py -s <sessionID> -u <username> -o f
```
Example:

```bash
python saintgram.py -s 1234567890%3aABCDEF%3a1234567890 -u johndoe -o f
```
This command retrieves the followers of johndoe and displays their information, including any public contact details.

3. Listing Following Accounts: To list the accounts that a user is following:

```bash
python saintgram.py -s <sessionID> -u <username> -o w
```
Example:

```bash
python saintgram.py -s 1234567890%3aABCDEF%3a1234567890 -u johndoe -o w
```
This command retrieves the first 50 accounts that johndoe is following.


## 📚 To retrieve the sessionID
![](https://files.catbox.moe/1rfi6j.png)


## OR WITH EXTENTION 
![](https://files.catbox.moe/tu3000.png)




