from PIL import Image

def encrypt_decrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            r_encrypted = r ^ key
            g_encrypted = g ^ key
            b_encrypted = b ^ key

            pixels[x, y] = (r_encrypted, g_encrypted, b_encrypted)

    img.save(output_path)
    
if __name__ == "__main__":
    mode = input("Please select your option? (encrypt/decrypt): ").lower()
    image_path = input("Enter the path of the image: ")
    key = int(input("Enter the encryption key (0-255): "))
    output_path = input("Enter the output path(format: {anyname}.jpg)for the processed image: ")

    if mode == "encrypt" or mode == "decrypt":
        encrypt_decrypt_image(image_path, key, output_path)
        print(f"The image has been successfully {mode}ed and saved at {output_path}")
    else:
        print("Invalid mode. Please enter either 'encrypt' or 'decrypt'.")
