# Trojan Calculator Simulator (GUI) - Educational Tool v2.0

**Author**: MohamedSelim  
**GitHub**: [ZeroOne](https://github.com/MohamedSelimMah)  
**License**: [MIT](LICENSE)  

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)  
---

## 📖 Overview

**Trojan Calculator Simulator v2.0** is a fully interactive educational tool that teaches Trojan horse behavior through a safe and controlled GUI environment. This simulator mimics "malicious" activities in a **non-destructive** way while providing real-time feedback through a calculator interface and simulation logs.

**Disclaimer**:  
⚠️ **This is a controlled simulation** containing zero actual malicious code. All "malicious" actions are fake file operations that leave your system completely unharmed.

---

## 🎯 Key Features (v2.0)

### Calculator Core
- ✅ **Basic Operations**: Addition, Subtraction, Multiplication, Division
- 🖥️ **GUI Interface**: Built using Tkinter for an intuitive experience
- 🚫 **Input Validation**: Handles:
  - Invalid numbers
  - Division by zero
  - Empty inputs

### Trojan Behavior Simulation
- 🕵️ **Stealth Actions**: Automatically creates harmless `fake_file.txt` after each calculation
- 🔁 **Persistence Simulation**: Logs fake startup registration in `persistence_log.txt`
- 🔄 **Reboot Detection**: Recognizes and logs simulated system restarts
- 🔡 **Simulated Keylogger** *(NEW!)*: Logs keystrokes typed while the window is active into `keylog_sim.txt`
- 📜 **Activity Logs**: Persistent files log all simulated behaviors

### Educational Value
- 🎓 **Hands-on Learning**: Connects user actions to behind-the-scenes behaviors in real-time
- 🔒 **Safe Playground**: All actions are sandboxed and reversible
- 💡 **Awareness-Oriented**: Reinforces knowledge of common Trojan techniques without harm

---

## 🛠️ How It Works

### User Interaction
1. Input two numbers.
2. Select operation (+, -, ×, ÷).
3. Click **Calculate**.
4. View result and simulation logs.

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
            log.write("\n[First time restart]\n")
    with open("restart_simu.txt", "w") as f:
        f.write("Simulated reboot marker")

def log_keystroke(event):
    with open("keylog_sim.txt", "a") as log:
        log.write(event.char)
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

### v2.0 Highlights
- ✅ **Keylogger Simulation**: Keystrokes typed during GUI use are captured into a local log file
- 🧠 **Educational Logging**: All simulated behaviors are clearly logged for review
- 📁 **Persistence Simulation Improvements**
- 🪟 **Improved GUI Experience**: Visual keylog feedback, better error messages

---

## 📌 Educational Scenarios

Use the simulator in controlled environments to demonstrate:

| Scenario                 | Behavior                                                    |
|--------------------------|-------------------------------------------------------------|
| **User Calculation**     | Performs operation + triggers fake file + logs persistence |
| **Key Press Simulation** | Logs keystrokes as if captured by malware                  |
| **First Run**            | Logs initial startup behavior                              |
| **Re-run App**           | Detects & logs "reboot" via marker file                    |

---

## 🛑 Critical Reminder

**This tool is only for**:  
✅ Education  
✅ Training environments  
✅ Cybersecurity awareness  

**Do not use for**:  
❌ Real malware creation  
❌ Penetration testing without consent  
❌ Production systems  

---

## 🤝 Contributing

Feel free to fork the project, submit PRs, or open issues.

Contribute by:
- 🐛 Reporting bugs
- 🧠 Suggesting new educational features
- ✨ Creating educational scenarios

See [CONTRIBUTING.md](CONTRIBUTING.md) for more info.

---

**Version 2.0 — Built for educators, learners, and curious minds**  
_"Knowledge is the best antivirus."_ 🔐

---
