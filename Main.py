import tkinter as tk
from simulation_engine import SimulationEngine
from config import HACKED_FOLDER, DECRYPTION_KEY

class KeyPad(tk.Canvas):
    def __init__(self, window):
        super().__init__(master=window, background=window.cget("background"), highlightthickness=0, height=380)

        upper_text = ("C", "+/-", "%")
        operators = ("+", "-", "=", "x", "÷")
        keypad_text = (
            7, 8, 9,
            4, 5, 6,
            1, 2, 3,
            0, "", "."
        )

        self.buttons = []

        for row in range(5):
            for col in range(4):
                x, y = 20 + 75 * col, 20 + 75 * row
                if row == 0 and col < 3:
                    button_background = "#D0CECE"
                    button_text = upper_text[col]
                elif col == 3:
                    button_background = "#FFC000"
                    button_text = operators[row]
                else:
                    button_background = "#262626"
                    index = (row - 1) * 3 + col
                    button_text = keypad_text[index] if index < len(keypad_text) else ""

                if button_text not in ("",):
                    if button_text == 0:
                        # Special case for the 0 button (wider button)
                        button = self.create_rectangle(x, y, x + 135, y + 60, fill=button_background, width=0,
                                                       outline=button_background)
                        self.create_text(x + 67.5, y + 30, text=str(button_text), font=("Arial", 20), fill="white")
                    else:
                        button = self.create_oval(x, y, x + 60, y + 60, fill=button_background, width=0)
                        text_color = "black" if button_background == "#D0CECE" else "white"
                        self.create_text(x + 30, y + 30, text=str(button_text), font=("Arial", 20), fill=text_color)

                    # Store button info for hover effects
                    self.buttons.append((button, button_background))
                    self.tag_bind(button, "<Button-1>", lambda event, text=button_text: self.KeyPress(text))
                    self.hoverColor(button, button, button_background)

    def hoverColor(self, item, button, color):
        if color == "#D0CECE":
            hover_color = "#E7E6E6"
        elif color == "#FFC000":
            hover_color = "#FFD966"
        elif color == "#262626":
            hover_color = "#595959"
        else:
            hover_color = "white"

        self.tag_bind(item, "<Enter>", lambda event: self.itemconfigure(button, fill=hover_color))
        self.tag_bind(item, "<Leave>", lambda event: self.itemconfigure(button, fill=color))

    def KeyPress(self, text):
        if text == "C":
            calculationScreen.configure(text="0")
        elif text == "+/-":
            current = calculationScreen.cget("text")
            if current != "0":
                if current.startswith("-"):
                    calculationScreen["text"] = current[1:]
                else:
                    calculationScreen["text"] = "-" + current
        elif text == "%":
            try:
                calculationScreen["text"] = str(float(calculationScreen.cget("text")) / 100)
            except:
                calculationScreen["text"] = "0"
        elif text == "=":
            calculationScreen.equate()
        else:
            calculationScreen.appendText(str(text))

        # Adjust font size if text is too wide
        if calculationScreen.winfo_reqwidth() > 325:
            current_size = int(calculationScreen.cget("font").split()[-1])
            calculationScreen["font"] = ("Arial", max(20, current_size - 3))


class CalculationScreen(tk.Label):
    def __init__(self, window):
        super().__init__(master=window, text="0", background=window.cget("background"),
                         foreground="white", font=("Arial", 40), anchor="e", padx=20, pady=20)
        self.pack(fill="x", side="top")

    def appendText(self, text):
        operators = ("+", "-", "x", "÷")
        equation = self.cget("text")

        if equation == "0" and text not in operators and text != ".":
            self["text"] = text
        elif text in operators and equation[-1] in operators:
            self["text"] = f"{equation[:-1]}{text}"
        else:
            self["text"] += text

    def equate(self):
        try:
            expression = self.cget("text").replace("x", "*").replace("÷", "/")
            result = eval(expression)

            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)

            self["text"] = str(result)
        except:
            self["text"] = "Error"


window = tk.Tk()
window.title("Calculator")
window.geometry("325x550")
window.resizable(False, False)
window.configure(bg="#202020")

calculationScreen = CalculationScreen(window)
keypad = KeyPad(window)
keypad.pack(fill="both", expand=True, side="bottom", pady=(15, 0))

window.mainloop()