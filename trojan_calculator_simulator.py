import os
import base64
import time
import threading
import logging
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

FAKE_KEY = "letmein"
LOCKED_FILES_LOG = "locked_files.txt"
LOG_FILE = "trojan_simulator.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def perform_calculation() -> None:
    """Perform the arithmetic operation selected by the user."""
    try:
        num1, num2 = float(entry1.get()), float(entry2.get())
        operator = selected_operator.get()

        result = {
            "+": num1 + num2,
            "-": num1 - num2,
            "*": num1 * num2,
            "/": num1 / num2 if num2 != 0 else float("inf")
        }.get(operator)

        if result == float("inf"):
            raise ZeroDivisionError

        result_label.config(text=f"Result: {result}")
        status_label.config(text="Status: Calculation successful.")
        logging.info(f"Calculated: {num1} {operator} {num2} = {result}")

        threading.Thread(target=execute_payload, daemon=True).start()

    except ValueError:
        result_label.config(text="Error: Invalid input.")
        status_label.config(text="Status: Error")
        logging.error("Invalid numeric input.")
    except ZeroDivisionError:
        result_label.config(text="Error: Division by zero.")
        status_label.config(text="Status: Error")
        logging.error("Attempted division by zero.")


def execute_payload() -> None:
    create_fake_file()
    simulate_persistence()
    encrypt_selected_file()


def create_fake_file() -> None:
    try:
        with open("fake_file.txt", "w") as f:
            f.write("This file simulates malicious behavior.")
        logging.info("Created fake file.")
    except Exception as e:
        logging.error(f"Failed to create fake file: {e}")


def simulate_persistence() -> None:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("persistence_log.txt", "a") as log:
            log.write(f"\n[Simulated Persistence] {timestamp}\n")
        logging.info("Simulated persistence logged.")
    except Exception as e:
        logging.error(f"Persistence simulation failed: {e}")


def check_first_run_or_restart() -> None:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("persistence_log.txt", "a") as log:
            log.write(
                f"\n[{'Restart' if os.path.exists('restart_simu.txt') else 'First Launch'}] {timestamp}\n"
            )
        with open("restart_simu.txt", "w") as marker:
            marker.write("Simulated system reboot marker")
        logging.info("Startup state tracked.")
    except Exception as e:
        logging.error(f"Error during startup tracking: {e}")


def log_keystroke(event: tk.Event) -> None:
    try:
        with open("keylog_sim.txt", "a") as log:
            log.write(event.char)
        logging.info(f"Key logged: {event.char}")
    except Exception as e:
        logging.error(f"Failed to log key: {e}")


def encrypt_selected_file() -> None:
    file_path = filedialog.askopenfilename(title="Select a file to lock")
    if not file_path:
        return

    try:
        with open(file_path, "rb") as file:
            content = base64.b64encode(file.read())
        with open(file_path, "wb") as file:
            file.write(content)

        with open(LOCKED_FILES_LOG, "a") as log:
            log.write(file_path + "\n")

        logging.warning(f"Locked file: {file_path}")
        messagebox.showwarning("File Locked", f"{os.path.basename(file_path)} has been locked.")
    except Exception as e:
        logging.error(f"Failed to lock file: {e}")


def unlock_encrypted_files() -> None:
    if not os.path.exists(LOCKED_FILES_LOG):
        return

    with open(LOCKED_FILES_LOG) as log:
        locked_files = [line.strip() for line in log if os.path.exists(line.strip())]

    if not locked_files:
        return

    key = simpledialog.askstring("Unlock Files", "Enter decryption key:")
    if key != FAKE_KEY:
        messagebox.showerror("Incorrect Key", "Files remain locked.")
        return

    for file_path in locked_files:
        try:
            with open(file_path, "rb") as file:
                decoded = base64.b64decode(file.read())
            with open(file_path, "wb") as file:
                file.write(decoded)
            logging.info(f"Unlocked: {file_path}")
        except Exception as e:
            logging.error(f"Failed to unlock {file_path}: {e}")

    os.remove(LOCKED_FILES_LOG)
    messagebox.showinfo("Files Unlocked", "All files have been unlocked.")


check_first_run_or_restart()

window = tk.Tk()
window.title("Trojan Calculator Simulator v2.5")
window.geometry("420x400")
window.bind("<Key>", log_keystroke)

tk.Label(window, text="First Number").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Second Number").grid(row=0, column=1, padx=10, pady=10)

entry1 = tk.Entry(window)
entry1.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

selected_operator = tk.StringVar(value="+")
tk.OptionMenu(window, selected_operator, "+", "-", "*", "/").grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(window, text="Calculate", command=perform_calculation).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

status_label = tk.Label(window, text="Status: Ready", fg="blue")
status_label.grid(row=5, column=0, columnspan=2, pady=5)

tk.Button(window, text="Unlock Files", command=unlock_encrypted_files).grid(row=6, column=0, columnspan=2, pady=10)

window.mainloop()
