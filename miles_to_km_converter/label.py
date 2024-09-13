import tkinter as tk

class Lab(tk.Label):
    def __init__(self, parent, text, column, row, padx=0, pady=0):
        super().__init__(parent, text=text)  # Pass the parent and text to Label
        self.grid(column=column, row=row, padx=padx, pady=pady)  # Set grid layout
