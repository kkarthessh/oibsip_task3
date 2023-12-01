import random
import string
def generate_password(length, use_lowercase_letters,use_uppercase_letters, use_numbers, use_punctuations):
    use_lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', ]
    use_uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    use_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    use_punctuations = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    if use_lowercase_letters:
        use_lowercase_letters += string.ascii_lowercase
    if use_uppercase_letters:
        use_uppercase_letters += string.ascii_uppercase
    if use_numbers:
        use_numbers += string.digits
    if use_punctuations:
        use_punctuations += string.punctuation
    if not use_lowercase_letters:
        print("Error: At least one lowercase letter set must be selected.")
        return None
    if not use_uppercase_letters:
        print("Error: At least one uppercase letter set must be selected.")
        return None
    if not use_numbers:
        print("Error: At least one number set must be selected.")
        return None
    if not use_punctuations:
        print("Error: At least one punctuation set must be selected.")
        return None
    password_uppercase = ''.join(random.choice(use_uppercase_letters) for i in range(length))
    password_lowercase = ''.join(random.choice(use_lowercase_letters) for i in range(length))
    password_numbers = ''.join(random.choice(use_numbers) for i in range(length))
    password_punctuations = ''.join(random.choice(use_punctuations) for i in range(length))
    return length,password_uppercase,password_lowercase,password_numbers,password_punctuations
def get_user_input():
    length = int(input("Enter the password length: "))
    use_uppercase_letters = input("Include uppercase letters: ").lower() == 'yes'
    use_lowercase_letters = input("Include lowercase letters: ").lower() == 'yes'
    use_numbers = input("Include numbers: ").lower() == 'yes'
    use_punctuations = input("Include punctuations: ").lower() == 'yes'
    return length,use_uppercase_letters,use_lowercase_letters,use_numbers,use_punctuations
def main():
    (length,use_uppercase_letters,use_lowercase_letters,use_numbers,use_punctuations)=get_user_input()
    (password_length,password_use_uppercase_letters,password_use_lowercase_letters,password_use_numbers,password_use_punctuations)= generate_password(length,use_uppercase_letters,use_lowercase_letters,use_numbers,use_punctuations)
    if password_length=='yes':
        print("Generated Password:", password_length)
    if password_use_uppercase_letters=='yes':
        print("Generated password:",password_use_uppercase_letters)
    if password_use_lowercase_letters=='yes':
        print("Generated password:",password_use_lowercase_letters)
    if password_use_numbers=='yes':
        print("Generated password:",password_use_numbers)
    if password_use_punctuations=='yes':
        print("Generated password:",password_use_punctuations)
if __name__ == "__main__":
    main()   