import tkinter as tk
from tkinter import filedialog
from .jo_parser import JoParser
from .checker import Checker, ElbowCheckResult
import json
import sys

class JaparProcessor:
    def __init__(self, file_path=None):
        self.root = tk.Tk()
        self.root.title("Japar Processor")
        self.root.geometry("800x600")

        self.open_button = tk.Button(self.root, text="Open JO File", command=self.open_file)
        self.open_button.grid(row=0, column=0, sticky='w')

        self.file_label = tk.Label(self.root, text="")
        self.file_label.grid(row=0, column=1, sticky='w')

        self.text_area = tk.Text(self.root)
        self.text_area.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        if file_path:
            self.process_file(file_path)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JO files", "*.jo")])
        if file_path:
            self.process_file(file_path)
    
    def process_file(self, file_path):
        self.file_label.config(text=file_path)
        with open(file_path, 'r') as file:
            content = file.read()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, content)
        parsed_elbows = JoParser.parse(content)
        elbow_results = Checker.check_elbows(parsed_elbows)
        self.print_elbow_results(elbow_results)
        
    def run(self):
        self.root.mainloop()

    def print_elbow_results(self, elbow_results: dict[str, list[ElbowCheckResult]]):
        self.text_area.delete("1.0", tk.END)
        output_lines = []
        for load_case_name, elbow_results_for_this_case in elbow_results.items():
            output_lines.append("Zatěžovací stav: " + load_case_name)
            for elbow_result in elbow_results_for_this_case:
                output_lines.append(elbow_result.output_line)
            output_lines.append("├────────┼────────────┼──────────────┼──────────┼─────────┼──────────┼─────────────┤\n")
        self.text_area.insert(tk.END, "\n".join(output_lines))
