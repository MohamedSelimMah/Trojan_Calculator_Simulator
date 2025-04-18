import os
import time
import threading
import tkinter as tk
import logging

logging.basicConfig(
    filename='trojan_simulator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def perform_calculation():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = selected_oper.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result_lbl.config(text="Error! Division by zero.")
                return

        result_lbl.config(text="Result: " + str(result))
        status_lbl.config(text="Status: Calculation successful.")
        logging.info(f"Performed calculation: {num1} {operation} {num2} = {result}")

        threading.Thread(target=Payload, daemon=True).start()

    except ValueError as e:
        logging.error(f"Invalid input: {e}")
        result_lbl.config(text="Invalid input. Please enter valid numbers.")
        status_lbl.config(text="Status: Invalid input.")

def Payload():
    try:
        with open("fake_file.txt", "w") as fake_file:
            fake_file.write("This is a fake file created by the Trojan simulator.")
        logging.info("Fake file created.")
    except Exception as e:
        logging.error(f"Error creating fake file: {e}")

    simulate_persistence()

def log_keystroke(event):
    key = event.char
    try:
        if key:
            with open("keylog_sim.txt", 'a') as log:
                log.write(f"{key}")
            logging.INFO(f"Logged key: {key}")
    except Exception as e:
        logging.error(f"Error logging key: {e}")

def simulate_persistence():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        with open("persistence_log.txt", "a") as log:
            log.write("\n[Simulated Persistence Triggered]\n")
            log.write("Pretending to add this program to system start.\n")
            log.write(f"Timestamp: {timestamp}\n")
        logging.info("Persistence simulation written to log.")
    except Exception as e:
        logging.error(f"Persistence simulation failed: {e}")

def check_restart():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        if os.path.exists("restart_simu.txt"):
            with open("persistence_log.txt", "a") as log:
                log.write("\n[Restart Detected]\n")
                log.write(f"Timestamp: {timestamp}\n")
        else:
            with open("persistence_log.txt", "a") as log:
                log.write("\n[First Time Launch]\n")
                log.write(f"Timestamp: {timestamp}\n")

        with open("restart_simu.txt", "w") as f:
            f.write("Simulated reboot marker.")
        logging.info("Reboot marker created.")
    except Exception as e:
        logging.error(f"Reboot marker failed: {e}")

check_restart()

window = tk.Tk()
window.title("Trojan Calculator Simulator v1.5")
window.geometry("400x350")
window.bind("<Key>", log_keystroke)

tk.Label(window, text="Enter First Number").grid(row=0, column=0, padx=10, pady=(10, 0))
tk.Label(window, text="Enter Second Number").grid(row=0, column=1, padx=10, pady=(10, 0))

entry1 = tk.Entry(window)
entry1.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

selected_oper = tk.StringVar(window)
selected_oper.set("+")
oper_menu = tk.OptionMenu(window, selected_oper, "+", "-", "*", "/")
oper_menu.grid(row=2, column=0, columnspan=2, pady=10)

calcul_btn = tk.Button(window, text="Calculate", command=perform_calculation)
calcul_btn.grid(row=3, column=0, columnspan=2, pady=10)

result_lbl = tk.Label(window, text="Result: ")
result_lbl.grid(row=4, column=0, columnspan=2, pady=5)

status_lbl = tk.Label(window, text="Status: Ready", fg="blue")
status_lbl.grid(row=5, column=0, columnspan=2, pady=5)


window.mainloop()
