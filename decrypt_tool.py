import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from config import DECRYPTION_KEY, HACKED_FOLDER

class DecryptionTool:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("File Recovery Tool")
        self.encryption_log = os.path.join(os.path.dirname(__file__), "sim_cache", "encryption_log.json")
        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.window, padding=20)
        main_frame.pack(fill="both", expand=True)

        # Key Entry
        ttk.Label(main_frame, text="Decryption Key:").grid(row=0, column=0, sticky="w")
        self.key_entry = ttk.Entry(main_frame, width=40)
        self.key_entry.grid(row=0, column=1, pady=5)

        # File List
        self.file_list = tk.Listbox(main_frame, selectmode="multiple", height=6)
        self.load_file_list()
        self.file_list.grid(row=1, column=0, columnspan=2, pady=10)

        # Buttons
        ttk.Button(main_frame, text="Decrypt Selected",
                 command=self.attempt_decryption).grid(row=2, column=0, pady=10)
        ttk.Button(main_frame, text="Exit",
                 command=self.window.destroy).grid(row=2, column=1, pady=10)

    def load_file_list(self):
        try:
            with open(self.encryption_log, "r") as f:
                files = json.load(f)
                for item in files:
                    self.file_list.insert("end", os.path.basename(item["simulated"]))
        except Exception as e:
            messagebox.showerror("Error", f"Could not load encrypted files list: {str(e)}")

    def attempt_decryption(self):
        if self.key_entry.get() != DECRYPTION_KEY:
            messagebox.showerror("Error", "Invalid decryption key")
            return

        selected = self.file_list.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No files selected")
            return

        try:
            with open(self.encryption_log, "r") as f:
                files = json.load(f)

            success_count = 0
            for idx in selected:
                file_info = files[idx]
                if os.path.exists(file_info["simulated"]):
                    # Simulate decryption by deleting locked file
                    os.remove(file_info["simulated"])
                    success_count += 1

            messagebox.showinfo("Success",
                f"Simulated decryption of {success_count} files\n"
                "Original files were never modified")
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    app = DecryptionTool()
    app.window.mainloop()