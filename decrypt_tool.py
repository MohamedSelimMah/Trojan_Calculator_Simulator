import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import shutil
from cryptography.fernet import Fernet, InvalidToken
from config import *


class DecryptionTool:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("File Recovery Tool")
        self.encryption_log = os.path.join(SIM_CACHE_PATH, "encryption_log.json")
        self.key_path = os.path.join(SIM_CACHE_PATH, "key.key")
        self.key = None
        self.cipher = None
        self.setup_ui()
        self.load_key()

    def load_key(self):
        try:
            if os.path.exists(self.key_path):
                with open(self.key_path, "rb") as f:
                    self.key = f.read()
                self.cipher = Fernet(self.key)
        except Exception as e:
            messagebox.showerror("Key Error", str(e))

    def setup_ui(self):
        main_frame = ttk.Frame(self.window, padding=20)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(main_frame, text="Decryption Key:").grid(row=0, column=0, sticky="w")
        self.key_entry = ttk.Entry(main_frame, width=50)
        self.key_entry.grid(row=0, column=1, pady=5)

        self.file_list = tk.Listbox(main_frame, selectmode="extended", height=15, width=80)
        self.load_file_list()
        self.file_list.grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Button(main_frame, text="Decrypt Selected",
                   command=self.attempt_decryption).grid(row=2, column=0, pady=10)
        ttk.Button(main_frame, text="Refresh List",
                   command=self.refresh_list).grid(row=2, column=1, pady=10)

    def refresh_list(self):
        self.file_list.delete(0, tk.END)
        self.load_file_list()

    def load_file_list(self):
        try:
            if os.path.exists(self.encryption_log):
                with open(self.encryption_log, "r") as f:
                    files = json.load(f)

                valid_files = []
                for item in files:
                    if all(os.path.exists(path) for path in [item["original"], item["backup"]]):
                        valid_files.append(item)
                        file_name = os.path.basename(item["original"])
                        file_type = "Image" if file_name.lower().endswith(
                            ('.png', '.jpg', '.jpeg', '.gif', '.bmp')) else "File"
                        self.file_list.insert("end", f"[{file_type}] {file_name}")

                # Update log with valid entries
                with open(self.encryption_log, "w") as f:
                    json.dump(valid_files, f, indent=4)
        except Exception as e:
            messagebox.showerror("Load Error", str(e))

    def attempt_decryption(self):
        try:
            if not self.validate_key():
                return

            selected = self.file_list.curselection()
            if not selected:
                messagebox.showwarning("Selection Error", "No files selected")
                return

            success_count = 0
            with open(self.encryption_log, "r") as f:
                files = json.load(f)

            remaining_files = []
            for idx, item in enumerate(files):
                if idx in selected:
                    if self.decrypt_file(item):
                        success_count += 1
                else:
                    remaining_files.append(item)

            # Update encryption log
            with open(self.encryption_log, "w") as f:
                json.dump(remaining_files, f, indent=4)

            messagebox.showinfo("Success",
                                f"Decrypted {success_count} files\n"
                                "Original files restored from backups")
            self.refresh_list()

        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))

    def validate_key(self):
        try:
            if self.key_entry.get().encode() != self.key:
                raise ValueError("Invalid decryption key")
            return True
        except Exception as e:
            messagebox.showerror("Validation Error", str(e))
            return False

    def decrypt_file(self, item):
        try:
            # Restore from backup
            shutil.copy2(item["backup"], item["original"])
            os.remove(item["backup"])
            return True
        except Exception as e:
            messagebox.showerror("File Error",
                                 f"Failed to decrypt {os.path.basename(item['original'])}: {str(e)}")
            return False


if __name__ == "__main__":

    app = DecryptionTool()
    app.window.mainloop()