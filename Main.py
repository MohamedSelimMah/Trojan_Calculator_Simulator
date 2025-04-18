import tkinter as tk
from tkinter import messagebox
import logging
import threading

# Set up logging for important actions

class CalculatorApp:
    def __init__(self, root):
        """Initialize the main calculator GUI."""
        self.root = root
        self.root.title("QuickCalc")
        self.root.geometry("400x500")
        self.root.config(bg="#1e1e1e")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        """Set up the display and calculator buttons."""
        # Result display
        display_frame = tk.Frame(self.root, bg="#1e1e1e")
        display_frame.pack(fill="both", padx=20, pady=20)
        result_label = tk.Label(display_frame, textvariable=self.result_var, font=("Segoe UI", 24), bg="#1e1e1e", fg="white")
        result_label.pack(fill="both", expand=True, padx=10, pady=10)

        # Buttons for calculator operations
        buttons_frame = tk.Frame(self.root, bg="#1e1e1e")
        buttons_frame.pack(fill="both", expand=True)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            row_frame = tk.Frame(buttons_frame, bg="#1e1e1e")
            row_frame.pack(fill="both", expand=True)
            for button_text in row:
                button = tk.Button(row_frame, text=button_text, font=("Segoe UI", 18), width=5, height=2,
                                   command=lambda text=button_text: self.on_button_click(text))
                button.pack(side="left", expand=True)

    def on_button_click(self, char):
        """Handle button click event for calculator."""
        current_text = self.result_var.get()
        if char == "=":
            try:
                result = eval(current_text)  # Calculate the result
                self.result_var.set(result)
                logging.info(f"Calculated result: {current_text} = {result}")
                threading.Thread(target=self.simulate_background_tasks, daemon=True).start()
            except Exception as e:
                self.result_var.set("Error")
                logging.error(f"Calculation error: {e}")
        else:
            self.result_var.set(current_text + char)



if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
