import math
import json

def generate_keys():
    # Choose larger prime numbers for p and q
    p = 61
    q = 53

    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose a suitable value for e
    e = 17  # Typically, this is a small prime number

    # Calculate d
    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(char, e, n) for char in message]
    return encrypted_message

def save_to_json(data):
    with open('encrypted_data.json', 'w') as json_file:
        json.dump(data, json_file)

def main():
    # Get user input
    user_input = input("Enter text to be encrypted: ")

    # Convert user input to a list of integers
    message = [ord(char) for char in user_input]

    # Generate keys
    public_key, private_key = generate_keys()
    print(f'Public key: {public_key}')
    print(f'Private key: {private_key}')

    # Encrypt the message
    encrypted_message = encrypt(message, public_key)

    # Save encrypted message to JSON
    data_to_save = {'encrypted_message': encrypted_message}
    save_to_json(data_to_save)

    print("Encrypted message saved to 'encrypted_data.json'.")

if __name__ == "__main__":
    main()
