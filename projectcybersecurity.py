import cv2
import os

def encryption(message, shift_key):

        # message (str): The message to encrypt.
        # shift (int): The shift key to use for encryption.
        # returns encrypted message

    encrypted_msg = ""
    for char in message:
        if char.isalpha():
            # Determine the starting alphabet ('a' or 'A')
            start_alpha = ord('a') if char.islower() else ord('A')
            # Apply the Caesar cipher transformation
            encrypted_char = chr((ord(char) - start_alpha + shift_key) % 26 + start_alpha)
            encrypted_msg += encrypted_char
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_msg += char
    return encrypted_msg

def decryption(encrypted_message, shift_key):

        # encrypted_message (str): The encrypted message to decrypt.
         # shift (int): The shift key used for encryption.
        # returns str: The decrypted message.
    return encryption(encrypted_message, -shift_key)

# Load the image
image_path = input("Enter image file directory: ")
image = cv2.imread(image_path)
# Get the secret message to hide
secret_message = input("Enter the secret message: ")
# Get the shift key for the Caesar cipher
shift_key = int(input("Enter the shift key (an integer): "))
# Get the password for encryption and decryption
password = input("Enter the encoding password: ")
# Encrypt the secret message using Caesar cipher
encrypted_message = encryption(secret_message, shift_key)
# Create dictionaries to map characters and their corresponding ASCII codes
character_to_code = {}
code_to_character = {}
for i in range(255):
    character = chr(i)
    character_to_code[character] = i
    code_to_character[i] = character

# Embed the encrypted message into the image using pixel values
m = 0  # Row index
n = 0  # Column index
z = 0  # Color channel index (0 for red, 1 for green, 2 for blue)

for i in range(len(encrypted_message)):
    # Modify the color value of the corresponding pixel
    image[n, m, z] = character_to_code[encrypted_message[i]]

    # Update indices for the next character
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encrypted_image.jpg", image)

# Open the encrypted image to confirm encryption
os.startfile("encrypted_image.jpg")

# Decrypt the message from the encrypted image
decrypted_message = ""
m = 0  # Row index
n = 0  # Column index
z = 0  # Color channel index (0 for red, 1 for green, 2 for blue)
# Verify the password before decryption
password_to_decrypt = input("Enter the decrypting password: ")

if password == password_to_decrypt:
    # Decrypt the message using the same approach as encryption
    for i in range(len(encrypted_message)):
        decrypted_message += code_to_character[image[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    # Apply Caesar cipher decryption to obtain the original message
    decrypted_msg = decryption(decrypted_message, shift_key)
    print("Decrypted message is:", decrypted_msg)
else:
    # Invalid password prevents decryption
    print("Invalid password")