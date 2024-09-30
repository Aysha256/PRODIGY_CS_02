from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_pixel = (b, g, r)  # Swap red and blue 
            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    messagebox.showinfo("Success", "Image encrypted successfully!")

def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_pixel = (b, g, r)  # Swap back red and blue 
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    messagebox.showinfo("Success", "Image decrypted successfully!")

def open_file():
    file_path = filedialog.askopenfilename()
    return file_path

def encrypt_action():
    input_path = open_file()
    if input_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if output_path:
            encrypt_image(input_path, output_path)

def decrypt_action():
    input_path = open_file()
    if input_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if output_path:
            decrypt_image(input_path, output_path)

# GUI 
root = tk.Tk()
root.title("Image Encryptor/Decryptor")
root.geometry("300x200")

encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_action)
encrypt_button.pack(pady=20)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_action)
decrypt_button.pack(pady=20)

root.mainloop()
