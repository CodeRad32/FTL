import secrets
import string
import logging
import base64

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_key(length=16, use_special_chars=False, custom_chars=None, output_format='str'):
    """
    Generate a random key of given length.

    Parameters:
    length (int): The length of the key to be generated. Default is 16.
    use_special_chars (bool): Whether to include special characters in the key. Default is False.
    custom_chars (str): Custom characters to use for key generation. Default is None.
    output_format (str): The format of the key ('str', 'hex', 'base64'). Default is 'str'.
    
    Returns:
    str: The generated key.
    """
    if length <= 0:
        logging.error("Length must be a positive integer")
        raise ValueError("Length must be a positive integer")

    # Define the characters to use in the key
    if custom_chars:
        characters = custom_chars
    else:
        characters = string.ascii_letters + string.digits
        if use_special_chars:
            characters += string.punctuation

    # Generate a random key
    key = ''.join(secrets.choice(characters) for _ in range(length))
    
    # Validate the strength of the generated key
    if not validate_key_strength(key):
        logging.warning("The generated key may not be strong enough.")
    
    # Convert key to the desired format
    if output_format == 'hex':
        key = key.encode('utf-8').hex()
    elif output_format == 'base64':
        key = base64.b64encode(key.encode('utf-8')).decode('utf-8')

    logging.info(f"Generated Key: {key}")
    return key

def validate_key_strength(key):
    """
    Validate the strength of the generated key based on entropy.

    Parameters:
    key (str): The key to be validated.

    Returns:
    bool: True if the key is strong, False otherwise.
    """
    entropy = len(set(key)) / len(key)
    if entropy < 0.5:
        logging.warning("The key has low entropy and may not be strong enough.")
        return False
    logging.info("The key has high entropy and is considered strong.")
    return True

def interactive_mode():
    """
    Interactive mode for generating keys based on user input.
    """
    try:
        length = int(input("Enter the length of the key: "))
        use_special_chars = input("Use special characters? (yes/no): ").lower() == 'yes'
        custom_chars = input("Enter custom characters (leave blank for default): ") or None
        output_format = input("Enter output format (str/hex/base64): ") or 'str'

        key = generate_key(length, use_special_chars, custom_chars, output_format)
        if validate_key_strength(key):
            print(f"Generated Key: {key}")
        else:
            print("Generated key may not be strong enough.")
    except ValueError as e:
        logging.error(f"Invalid input: {e}")
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    # Example usage
    key = generate_key(16, use_special_chars=True, output_format='base64')
    validate_key_strength(key)

    # Run interactive mode
    interactive_mode()
