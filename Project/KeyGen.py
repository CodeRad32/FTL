import secrets
import string

def generate_key(length=16, use_special_chars=False):
    """
    Generate a random key of given length.

    Parameters:
    length (int): The length of the key to be generated. Default is 16.
    use_special_chars (bool): Whether to include special characters in the key. Default is False.

    Returns:
    str: The generated key.
    """
    if length <= 0:
        raise ValueError("Length must be a positive integer")

    # Define the characters to use in the key
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    # Generate a random key
    key = ''.join(secrets.choice(characters) for _ in range(length))

    return key

# Example usage:
if __name__ == "__main__":
    key = generate_key(16, use_special_chars=True)
    print(f"Generated Key: {key}")
