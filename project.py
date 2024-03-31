def request_password():
    """
    Requests a password from the user and verifies that it has at least 10 characters,
    at least one uppercase letter, and at least one number.
    """
    while True:
        password = input("Enter a password (must have at least 16 characters, at least one uppercase letter, and at least one number): ")
        if len(password) >= 16 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
            print("Valid password.")
            return password
        else:
            print("The password must have at least 10 characters, at least one uppercase letter, and at least one number. Try again.")

def save_password(password):
    """
    Saves the valid password to a text file named 'passwords.txt'.
    """
    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')
    print("Password saved in 'passwords.txt'.")

def load_passwords():
    """
    Reads and displays the stored passwords from the 'passwords.txt' file.
    """
    try:
        with open('passwords.txt', 'r') as file:
            passwords = file.readlines()
            if not passwords:
                print("No passwords stored.")
            else:
                print("Stored passwords:")
                for i, password in enumerate(passwords, start=1):
                    print(f"{i}. {password.strip()}")
    except FileNotFoundError:
        print("'passwords.txt' file does not exist.")

def main():
    """
    Main function that executes the program.
    """
    print("S.K.I.: Password Management Program")

    # Request and validate the password
    password = request_password()

    # Save the password to a file
    save_password(password)

    # Load and display stored passwords
    load_passwords()

if __name__ == "__main__":
    main()




