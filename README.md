# Image Encryption Tool Using Pixel Manipulation

This is a simple image encryption and decryption tool that manipulates the pixels of an image using a basic XOR operation on their RGB values. The encryption and decryption processes are symmetric, meaning the same key can be used to both encrypt and decrypt an image.

## Features

- **Encrypt Images**: Scrambles the pixels of an image by applying a bitwise XOR operation on the RGB values using a key provided by the user.
- **Decrypt Images**: Restores the encrypted image back to its original form using the same key that was used for encryption.
- **Symmetric Encryption**: Encryption and decryption both rely on the same key, making the process reversible.

## Requirements

- Python 3.x
- `Pillow` library (for image manipulation)

### Installation

Before using the script, ensure that the `Pillow` library is installed. You can install it using pip:

```bash
pip install Pillow
```

## Usage

### 1. Encrypt an Image

To encrypt an image, follow these steps:

1. Run the script.
2. Select the "encrypt" mode.
3. Provide the path to the image you want to encrypt.
4. Input a key (a number between 0 and 255).
5. Specify the output path where you want to save the encrypted image.

### 2. Decrypt an Image

To decrypt an image, repeat the steps but select "decrypt" mode and ensure you provide the **same key** that was used for encryption.

### Example

```bash
Do you want to encrypt or decrypt the image? (encrypt/decrypt): encrypt
Enter the path of the image: input.jpg
Enter the encryption key (0-255): 42
Enter the output path for the processed image: encrypted_image.jpg
```

To decrypt the same image, you would:

```bash
Do you want to encrypt or decrypt the image? (encrypt/decrypt): decrypt
Enter the path of the image: encrypted_image.jpg
Enter the encryption key (0-255): 42
Enter the output path for the processed image: decrypted_image.jpg
```

## How It Works

- **XOR Operation**: The tool uses an XOR operation (`^`) on each pixel's RGB values with the user-provided key. XOR is a reversible operation, so applying it again with the same key restores the original pixel values.
- **Symmetric Encryption**: The same key is used for both encryption and decryption. The security of the encryption depends on the secrecy of the key.

## Notes

- The key must be a number between 0 and 255 (as RGB values are constrained to this range).
- Ensure the same key is used for both encryption and decryption, otherwise, the image will not be restored correctly.
- This is a basic form of encryption and is not intended for high-security applications.

## License

This project is open-source and free to use. Feel free to modify and distribute it as needed.
