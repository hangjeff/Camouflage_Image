
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import chardet

class Text(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # Objects on the Frame
        label = tk.Label(self, text="Merge Image with Text")
        label.pack(pady=10, padx=10)
        
        Btn_Image = tk.Button(self, text="Browse Image", command=browse_image)
        Btn_Image.pack(pady=5)

        Btn_Text = tk.Button(self, text="Browse Text File", command=browse_file)
        Btn_Text.pack(pady=5)
        
        Btn_Merge = tk.Button(self, text="Merge Files", command=merge_files,
                                bg = 'lightgreen')
        Btn_Merge.pack(pady=5)
        
        Btn_Back = tk.Button(self, text="Go to Home Page",
                            command=lambda: controller("HomePage"),
                            bg = "lightblue")
        Btn_Back.pack(pady=5)

def merge_files():
    global image_path, text_path
    result = ''
    if image_path and text_path:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
        with open(text_path, 'rb') as text_file:
            text_data = text_file.read()
            result = chardet.detect(text_data)
            print("Encoding:", result['encoding'])
        with open("new.png", 'wb') as output_file:
            output_file.write(img_data)
            output_file.write(text_data.decode(result['encoding']).encode('utf-8'))
        
        print("Files merged successfully!")
    else:
        print("Please select both image and text files.")

def browse_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    print("Image selected:", image_path)

def browse_file():
    global text_path
    text_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    print("File selected:", text_path)