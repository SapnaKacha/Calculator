import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Sapna's Calculator")
        self.root.geometry("310x390")
        self.root.config(bg="Grey")
        self.root.resizable(False,False)
       

        self.display = tk.Entry(self.root, font=("Times New Roman", 18), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.display.config(bg="white")

        # Button definitions
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+', 
            'sqrt','^2','sin','cos'
        ]

        # Create and place buttons
        row_val = 1
        col_val = 0
        for button in self.buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, font=("Times New Roman", 14), width=6, height=2,
                           command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col, padx=4, pady=4)

    def on_button_click(self, char):
        current_text = self.display.get()

        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = eval(current_text)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == 'sqrt':
            try:
                result = math.sqrt(float(current_text))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == '^2':
            try:
                result = float(current_text) ** 2
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == 'sin':
            try:
                result = math.sin(math.radians(float(current_text)))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == 'cos':
            try:
                result = math.cos(math.radians(float(current_text)))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, char)

# Create the main window
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()