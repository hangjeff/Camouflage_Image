
import tkinter as tk
from tkinter import filedialog
import os


class Zip(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # Objects on the Frame
        label = tk.Label(self, text="Merge Image with Zip")
        label.pack(pady=10, padx=10)
        
        Btn_Image = tk.Button(self, text="Browse Image", command=browse_image)
        Btn_Image.pack(pady=5)

        Btn_Zip = tk.Button(self, text="Browse Zip", command=browse_zip)
        Btn_Zip.pack(pady=5)
        
        Btn_Merge = tk.Button(self, text="Merge Files", command=merge_files,
                                bg = 'lightgreen')
        Btn_Merge.pack(pady=5)
        
        Btn_Back = tk.Button(self, text="Go to Home Page",
                            command=lambda: controller("HomePage"),
                            bg = "lightblue")
        Btn_Back.pack(pady=5)

def merge_files():
    global image_path, zip_path
    if image_path and zip_path:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
        with open(zip_path, 'rb') as zip_file:
            zip_data = zip_file.read()
        
        with open("new.png", 'wb') as output_file:
            output_file.write(img_data)
            output_file.write(zip_data)
        
        print("Files merged successfully!")
    else:
        print("Please select both image and zip files.")

def browse_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    print("Image selected:", image_path)

def browse_zip():
    global zip_path
    zip_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip;*.7z;*.rar")])
    print("Zip file selected:", zip_path)
