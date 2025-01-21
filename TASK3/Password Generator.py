import random
import string

def generate_password(length, complexity):
    characters = ''
    if complexity >= 1:
        characters += string.ascii_lowercase
    if complexity >= 2:
        characters += string.ascii_uppercase
    if complexity >= 3:
        characters += string.digits
    if complexity >= 4:
        characters += string.punctuation

    if not characters:
        raise ValueError("Invalid complexity level")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        complexity = int(input("Enter the complexity level (1 to 4):\n"
                               "1: Lowercase letters\n"
                               "2: Lowercase and Uppercase letters\n"
                               "3: Lowercase, Uppercase letters and Digits\n"
                               "4: Lowercase, Uppercase letters, Digits and Special characters\n"
                               "Your choice: "))

        if length <= 0:
            raise ValueError("Password length must be a positive integer")

        password = generate_password(length, complexity)
        print(f"Generated password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
