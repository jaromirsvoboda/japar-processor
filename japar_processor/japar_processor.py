import tkinter as tk
from tkinter import filedialog
from .jo_parser import JoParser
import json
import sys

class JaparProcessor:
    def __init__(self, file_path=None):
        self.root = tk.Tk()
        self.root.title("Japar Processor")

        self.open_button = tk.Button(self.root, text="Open JO File", command=self.open_file)
        self.open_button.pack()

        self.text_area = tk.Text(self.root)
        self.text_area.pack()

        if file_path:
            self.load_file(file_path)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JO files", "*.jo")])
        if file_path:
            self.load_file(file_path)
    
    def load_file(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, content)
        JoParser.parse(content)
        

    def run(self):
        self.root.mainloop()
