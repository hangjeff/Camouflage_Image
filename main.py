
import tkinter as tk
import os
from text import Text
from zip import Zip


# PageApp() manages page navigation
class PageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Merge Image and File")
        self.geometry("350x200")
        
        # Container has a Frame to hold all pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.pages = {}
        
        for Page in (HomePage, Zip, Text):
            page_name = Page.__name__
            page = Page(parent = self.container, controller = self)
            self.pages[page_name] = page
            page.grid(row = 0, column = 0, sticky=  "nsew")
            
        self.show_page("HomePage")
        
    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()
        
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text = "Home Page")
        label.pack(pady = 10, padx = 125)
        
        Btn_Zip = tk.Button(self, text = "Merge Image with Zip file",
                            command = lambda: controller.show_page("Zip"))
        Btn_Zip.pack(padx=5, pady=5)
        Btn_Text = tk.Button(self, text = "Merge Image with Text file",
                            command = lambda: controller.show_page("Text"))
        Btn_Text.pack(padx=5, pady=5)            


if __name__ == '__main__':
    app = PageApp()
    app.mainloop()