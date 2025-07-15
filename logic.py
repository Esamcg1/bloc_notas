import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


class SimpleTextEditor():
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_open_file = ''

    def save_file(self):
        if not self.current_open_file:
            new_file_path = filedialog.asksaveasfilename()          
            
            if new_file_path:
                self.current_open_file = new_file_path
            else:
                return
                
        with open(self.current_open_file, 'w') as file:
            file.write(self.text_area.get("1.0", tk.END))

    def close_window(self):
        if messagebox.askokcancel("Salir", "¿Desea salir?"):
            self.root.destroy()
    
    def new_file(self):
        self.text_area.delete("1.0", tk.END)  # Clear the text area
        self.current_open_file = ''

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.text_area.delete("1.0", tk.END)  # Clear the text area
            with open(filename, 'r') as file:
                self.text_area.insert("1.0", file.read())
            self.current_open_file = filename
