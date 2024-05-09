import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display input and output
        self.entry = tk.Entry(self.master, width=30, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Buttons for numerical input
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('√', 5, 0), ('^', 5, 1), ('log', 5, 2), ('sin', 5, 3),
            ('cos', 6, 0), ('tan', 6, 1), ('AC', 6, 2)
        ]

        for (text, row, col) in buttons:
            tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 14), command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == 'AC':
            self.entry.delete(0, tk.END)
        elif char == '√':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == 'log':
            try:
                result = math.log(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char in ['sin', 'cos', 'tan']:
            try:
                result = getattr(math, char)(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)

def main():
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
