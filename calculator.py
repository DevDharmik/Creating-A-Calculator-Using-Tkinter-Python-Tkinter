import tkinter as tk

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('400x500')
        master.config(bg='lightgreen')

        self.equation = tk.StringVar()
        self.entry_value = ''

        # Entry widget for displaying the expression
        self.entry = tk.Entry(master, textvariable=self.equation, font=('Arial Bold', 28), bd=10, insertwidth=4, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, pady=20)

        # Button configuration
        button_config = {
            'padx': 20,
            'pady': 20,
            'bd': 5,
            'relief': 'ridge',
            'font': ('Arial', 18)
        }

        # Button layout: (text, row, column, [colspan])
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2),
            ('C', 5, 0), ('=', 5, 1, 3)
        ]

        for (text, row, col, *rest) in buttons:
            colspan = rest[0] if rest else 1
            if text == '=':
                tk.Button(master, text=text, **button_config, bg='orange', command=self.solve).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky='nsew')
            elif text == 'C':
                tk.Button(master, text=text, **button_config, bg='red', command=self.clear).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            else:
                tk.Button(master, text=text, **button_config, command=lambda t=text: self.show(t)).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        # Configure row and column weights for resizing
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def show(self, value):
        """Update the entry with the pressed button's value."""
        if value == '.' and (self.entry_value and self.entry_value[-1] == '.'):
            return  # Prevent multiple decimal points in a number
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        """Clear the entry field."""
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        """Evaluate the expression and display the result."""
        try:
            # Replace '÷' and '×' with '/' and '*' for eval
            expression = self.entry_value.replace('÷', '/').replace('×', '*')
            result = eval(expression)
            self.equation.set(result)
            self.entry_value = str(result)  # Update entry with the result
        except Exception:
            self.equation.set("Error")

# Create and run the calculator application
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
