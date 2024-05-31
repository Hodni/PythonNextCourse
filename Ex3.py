import string

# Define custom exceptions for specific validation errors
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, message="The username contains an illegal character"):
        super().__init__(message)

class UsernameTooShort(Exception):
    def __init__(self, message="The username is too short"):
        super().__init__(message)

class UsernameTooLong(Exception):
    def __init__(self, message="The username is too long"):
        super().__init__(message)

class PasswordMissingCharacter(Exception):
    def __init__(self, message="The password is missing a character"):
        super().__init__(message)

class PasswordTooShort(Exception):
    def __init__(self, message="The password is too short"):
        super().__init__(message)

class PasswordTooLong(Exception):
    def __init__(self, message="The password is too long"):
        super().__init__(message)

def validate_username(username):
    """Validate the username according to the specified rules."""
    legal_chars = string.ascii_letters + string.digits + '_'

    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()
    if any(char not in legal_chars for char in username):
        raise UsernameContainsIllegalCharacter()

def validate_password(password):
    """Validate the password according to the specified rules."""
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()

    if not any(char.isupper() for char in password):
        raise PasswordMissingCharacter("The password is missing an uppercase letter")
    if not any(char.islower() for char in password):
        raise PasswordMissingCharacter("The password is missing a lowercase letter")
    if not any(char.isdigit() for char in password):
        raise PasswordMissingCharacter("The password is missing a digit")
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingCharacter("The password is missing a special character")

def check_input(username, password):
    """Check both username and password by validating them."""
    validate_username(username)
    validate_password(password)
    print("OK")

def main():
    """Main function to test the validation logic."""
    test_cases = [
        ("1", "2"),
        ("0123456789ABCDEFG", "2"),
        ("A_a1.", "12345678"),
        ("A_1", "2"),
        ("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary"),
        ("A_1", "abcdefghijklmnop"),
        ("A_1", "ABCDEFGHIJLKMNOP"),
        ("A_1", "ABCDEFGhijklmnop"),
        ("A_1", "4BCD3F6h1jk1mn0p"),
        ("A_1", "4BCD3F6.1jk1mn0p")
    ]

    for username, password in test_cases:
        try:
            check_input(username, password)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
