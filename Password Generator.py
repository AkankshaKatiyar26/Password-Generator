import random
import string

def generate_password(length, complexity):
    # Define character sets
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Build the character pool based on complexity
    char_pool = lower_chars
    if complexity >= 2:
        char_pool += upper_chars
    if complexity >= 3:
        char_pool += digits
    if complexity >= 4:
        char_pool += special_chars

    # Generate a random password
    if not char_pool:
        return "Error: Complexity level too low."
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be a positive integer. Please try again.")
                continue
            complexity = int(input("Enter the complexity level (1-4):\n1. Lowercase letters\n2. Lowercase + Uppercase letters\n3. Lowercase + Uppercase letters + Digits\n4. Lowercase + Uppercase letters + Digits + Special characters\n"))
            if complexity not in [1, 2, 3, 4]:
                print("Complexity level must be between 1 and 4. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
        break

if __name__ == "__main__":
    main()
