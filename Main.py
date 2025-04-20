import tkinter as tk
from tkinter import messagebox, filedialog
import os
import json
from datetime import datetime
from config import *


# ================= SIMULATION ENGINE =================
class SimulationEngine:
    def __init__(self):
        self.encryption_log = os.path.join(SIM_CACHE_PATH, "encryption_log.json")
        self.keylog_file = os.path.join(SIM_CACHE_PATH, "keylog.txt")
        self.initialize_files()

    def initialize_files(self):
        """Ensure required files exist"""
        open(self.keylog_file, 'a').close()
        if not os.path.exists(self.encryption_log):
            with open(self.encryption_log, 'w') as f:
                json.dump([], f)

    def log_keystroke(self, key):
        """Log calculator button presses"""
        with open(self.keylog_file, "a") as f:
            f.write(f"{datetime.now()}: {key}\n")

    def simulate_attack(self, parent_window):
        """Safe file encryption simulation"""
        files = filedialog.askopenfilenames(
            title="Select files to simulate encryption (SAFE DEMO)",
            parent=parent_window
        )
        if not files:
            return False

        encrypted_files = []
        for path in files:
            try:
                filename = os.path.basename(path)
                sim_path = os.path.join(HACKED_FOLDER, f"{filename}.locked")

                with open(sim_path, "w") as f:
                    f.write(f"SAFE SIMULATION - Original: {path}\n")

                encrypted_files.append({
                    "original": path,
                    "simulated": sim_path,
                    "timestamp": str(datetime.now())
                })
            except Exception as e:
                continue

        with open(self.encryption_log, "w") as f:
            json.dump(encrypted_files, f)

        self.create_ransom_note()
        return True

    def create_ransom_note(self):
        """Create warning message"""
        note_path = os.path.join(HACKED_FOLDER, "READ_ME.txt")
        with open(note_path, "w") as f:
            f.write(f"""Your files have been encrypted! (Simulation)

To decrypt:
1. Run decrypt_tool.py
2. Use key: {DECRYPTION_KEY}
3. Select files to recover

This is a harmless educational demo.
Original files remain untouched.
""")


# ================= CALCULATOR GUI =================
class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.sim_engine = SimulationEngine()
        self.current_input = "0"
        self.setup_gui()
        self.bind_events()

    def setup_gui(self):
        self.window.geometry("325x550")
        self.window.configure(bg="#202020")
        self.window.resizable(False, False)

        # Main container frame
        main_frame = tk.Frame(self.window, bg="#202020")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Calculator display
        self.display = tk.Label(main_frame, text=self.current_input, bg="#202020", fg="white",
                                font=("Arial", 40), anchor="e")
        self.display.pack(fill="x", pady=(0, 20))

        # Button frame using grid
        button_frame = tk.Frame(main_frame, bg="#202020")
        button_frame.pack(fill="both", expand=True)

        # Calculator buttons
        buttons = [
            ('C', 0, 0, 1, 1, "#D0CECE", "black"),
            ('+/-', 0, 1, 1, 1, "#D0CECE", "black"),
            ('%', 0, 2, 1, 1, "#D0CECE", "black"),
            ('÷', 0, 3, 1, 1, "#FFC000", "white"),
            ('7', 1, 0, 1, 1, "#262626", "white"),
            ('8', 1, 1, 1, 1, "#262626", "white"),
            ('9', 1, 2, 1, 1, "#262626", "white"),
            ('×', 1, 3, 1, 1, "#FFC000", "white"),
            ('4', 2, 0, 1, 1, "#262626", "white"),
            ('5', 2, 1, 1, 1, "#262626", "white"),
            ('6', 2, 2, 1, 1, "#262626", "white"),
            ('-', 2, 3, 1, 1, "#FFC000", "white"),
            ('1', 3, 0, 1, 1, "#262626", "white"),
            ('2', 3, 1, 1, 1, "#262626", "white"),
            ('3', 3, 2, 1, 1, "#262626", "white"),
            ('+', 3, 3, 1, 1, "#FFC000", "white"),
            ('0', 4, 0, 1, 2, "#262626", "white"),
            ('.', 4, 2, 1, 1, "#262626", "white"),
            ('=', 4, 3, 1, 1, "#FFC000", "white")
        ]

        for (text, row, col, colspan, rowspan, bg, fg) in buttons:
            btn = tk.Button(button_frame, text=text, font=("Arial", 20),
                            bg=bg, fg=fg, borderwidth=0,
                            command=lambda t=text: self.on_button_press(t))
            btn.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan,
                     sticky="nsew", padx=2, pady=2)

        # Configure grid weights
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)

    def bind_events(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def on_button_press(self, text):
        """Handle calculator button presses"""
        self.sim_engine.log_keystroke(text)

        if text == 'C':
            self.current_input = "0"
        elif text == '=':
            try:
                self.current_input = str(eval(self.current_input.replace('×', '*')))
            except:
                self.current_input = "Error"
        else:
            if self.current_input == "0" or self.current_input == "Error":
                self.current_input = text
            else:
                self.current_input += text

        self.display.config(text=self.current_input[:15])  # Limit display length

    def on_window_close(self):
        if self.sim_engine.simulate_attack(self.window):
            messagebox.showwarning(
                "System Alert",
                f"Files simulated as encrypted!\n"
                f"Recovery key: {DECRYPTION_KEY}\n"
                f"Check {HACKED_FOLDER} for details."
            )
        self.window.destroy()


if __name__ == "__main__":
    app = CalculatorApp()
    app.window.mainloop()