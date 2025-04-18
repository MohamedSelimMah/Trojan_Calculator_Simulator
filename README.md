
# Trojan Calculator Simulator (GUI) - Educational Tool v2.5

**Author**: MohamedSelim  
**GitHub**: [ZeroOne](https://github.com/MohamedSelimMah)  
**License**: [MIT](LICENSE)  

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)  
---

## 📖 Overview

**Trojan Calculator Simulator v2.5** is a fully interactive educational tool that demonstrates Trojan horse behavior in a safe, simulated GUI environment. Version 2.5 introduces simulated **file encryption/decryption**, an improved **keylogger**, and enhanced logging of fake persistence techniques.

**Disclaimer**:  
⚠️ **This is a safe simulation only. No actual malicious behavior occurs.**  
All effects are purely educational and non-destructive — no real files are harmed or accessed without user consent.

---

## 🎯 Key Features (v2.5)

### Calculator Core
- ✅ **Basic Operations**: Addition, Subtraction, Multiplication, Division
- 🖥️ **GUI Interface**: Built using Tkinter for intuitive interaction
- 🚫 **Input Validation**: Handles:
  - Invalid input
  - Division by zero
  - Empty fields

### Trojan Behavior Simulation
- 🕵️ **Stealth Actions**: Creates harmless `fake_file.txt` after each calculation
- 🔁 **Persistence Simulation**: Logs fake startup registration in `persistence_log.txt`
- 🔄 **Reboot Detection**: Detects reruns using a marker file (`restart_simu.txt`)
- 🔡 **Simulated Keylogger**: Captures typed keys in `keylog_sim.txt` while the GUI is active
- 🔐 **File Locking Simulation** *(NEW!)*: Encodes selected files using Base64 (mimics ransomware)
- 🔓 **File Unlocking** *(NEW!)*: Prompts for a fake decryption key to restore locked files
- 📜 **Activity Logs**: All actions logged for user review

### Educational Value
- 🎓 **Hands-on Learning**: See how Trojan behaviors might operate
- 🔒 **Safe Sandbox**: All effects are local, visible, and reversible
- 💡 **Cyber Awareness**: Ideal for training sessions and ethical hacking education

---

## 🛠️ How It Works

### User Interaction
1. Input two numbers.
2. Select an operation (+, -, ×, ÷).
3. Click **Calculate**.
4. A fake payload is triggered: logs, fake files, keylogs, and more.
5. Optionally, "lock" or "unlock" files using the file selector.

### Simulation Flow

```python
def Payload():
    with open("fake_file.txt", "w") as fake_file:
        fake_file.write("This is a fake file created by the Trojan simulator.")
    simulate_persistence()

def simulate_persistence():
    with open("persistence_log.txt", "a") as log:
        log.write("\n[Simulated Persistence Triggered]\n")

def check_restart():
    if os.path.exists("restart_simu.txt"):
        with open("persistence_log.txt", "a") as log:
            log.write("\n[Restart Detected]\n")
    else:
        with open("persistence_log.txt", "a") as log:
            log.write("\n[First Time Launch Detected]\n")
    with open("restart_simu.txt", "w") as f:
        f.write("Simulated reboot marker")

def log_keystroke(event):
    with open("keylog_sim.txt", "a") as log:
        log.write(event.char)
```

Additional simulated functions include:

```python
def lock_file(file_path):
    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read())
    with open(file_path, "wb") as f:
        f.write(encoded)

def unlock_file(file_path, key):
    if key == "letmein":
        with open(file_path, "rb") as f:
            decoded = base64.b64decode(f.read())
        with open(file_path, "wb") as f:
            f.write(decoded)
    else:
        print("Incorrect key. Simulated decryption failed.")
```

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/ZeroOne/TrojanCalculatorSimulator.git

# Navigate into the folder
cd TrojanCalculatorSimulator

# Run the simulator
python3 trojan_calculator_simulator.py
```

**Requirements**:  
- Python 3.7+
- Tkinter (included in standard Python distributions)

---

## 📜 Version Information

### v2.5 Highlights
- 🔐 **File Encryption Simulation**: Base64 encodes selected files
- 🔓 **File Decryption Simulation**: Unlocks files using a predefined fake key (`letmein`)
- 🧠 **Keylogger Enhancements**: More responsive and logs all keystrokes in the active window
- 📁 **Robust Persistence Simulation**: Smarter detection of simulated reboots
- 🪟 **Improved GUI & UX**: Clean layout, better messaging, thread-safe updates

---

## 📌 Educational Scenarios

Use the simulator to demonstrate common Trojan tactics in a controlled setting:

| Scenario                  | Simulated Behavior                                             |
|---------------------------|----------------------------------------------------------------|
| **Basic Calculation**     | Performs operation + drops fake file + logs persistence       |
| **Key Press Simulation**  | Captures keystrokes to `keylog_sim.txt`                       |
| **First Launch**          | Logs startup in `persistence_log.txt`                         |
| **App Re-run**            | Logs a fake reboot using a marker file                        |
| **File Locking**          | Encodes file content as if encrypted by ransomware            |
| **File Unlocking**        | Requires fake key (`letmein`) to decode simulated file        |

---

## 🛑 Critical Reminder

**This tool is strictly for**:  
✅ Education  
✅ Ethical hacking workshops  
✅ Cybersecurity awareness sessions  

**Do NOT use for**:  
❌ Real-world exploitation  
❌ Penetration testing without consent  
❌ Malware deployment or obfuscation  

---

## 🤝 Contributing

Contributions are welcome!  
You can help by:
- 🐛 Reporting bugs
- 💡 Recommending improvements
- 📖 Translating for non-English audiences
