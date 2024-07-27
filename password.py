import random
import string

def generate_password(length):
    # Define the character sets to use in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    # Prompt the user to enter the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Length should be greater than zero.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print("Generated password:", password)
        
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
