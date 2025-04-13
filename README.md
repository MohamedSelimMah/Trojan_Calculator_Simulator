# Trojan Calculator Simulator (GUI) - Educational Tool v1.5

**Author**: MohamedSelim  
**GitHub**: [ZeroOne](https://github.com/MohamedSelimMah)  
**License**: [MIT](LICENSE)  

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)  
*"Understanding malware through safe simulation"*

---

## 📖 Overview

**Trojan Calculator Simulator v1.5** is an enhanced version of the interactive educational tool that demonstrates Trojan horse principles through a functional GUI calculator. This version introduces more realistic "malicious" behavior simulations, such as file persistence and reboot detection, offering a better learning experience for cybersecurity fundamentals.

**Disclaimer**:  
⚠️ **This is a controlled simulation** containing zero actual malicious code. All "malicious" actions are fake file operations that leave your system completely unharmed.

---

## 🎯 Key Features (v1.5)

### Calculator Core
- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **GUI Interface**: Built with Tkinter for intuitive user interaction
- **Input Validation**: Robust error handling for:
  - Non-numeric inputs
  - Division by zero attempts
  - Empty fields

### Trojan Simulation
- 🕵️ **Stealth Mode**: Creates harmless `fake_file.txt` after each calculation
- 🔍 **Persistence Simulation**: Logs simulated persistence actions, mimicking a Trojan's behavior of adding itself to system startup
- 🚨 **Reboot Detection**: Logs when the system is simulated to restart (using a fake "restart_simu.txt" marker file)
- 📝 **Transparent Process**: Status messages show simulation details
- 📜 **Persistence Logs**: Log files track the simulated persistence and restart actions

### Educational Value
- 🧠 **Interactive Learning**: Real-time comparison between user actions and background simulation
- 📝 **Security Tips**: Contextual warnings about real-world Trojan behaviors
- 🔒 **Safe Environment**: All activities are fully contained and reversible

---

## 🛠️ How It Works

### User Interaction Flow
1. **Input**  
   - Enter numbers in designated fields
2. **Operation Selection**  
   - Choose from +, -, *, / via dropdown
3. **Calculation**  
   - Click "Calculate" to get the result
4. **Visual Feedback**  
   - Results displayed in the console

### Background Simulation
```python
# Sample simulation code (v1.5)

def Payload():
    with open("fake_file.txt", "w") as fake_file:
        fake_file.write("This is a fake file created by the Trojan simulator.")
    print("Done")
    simulate_pres()

def simulate_pres():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    with open("persistence_log.txt", "a") as log:
        log.write("\n[Simulated Persistence Triggered]\n")
        log.write("Pretending to add this program to system start.\n")
        log.write(f"Timestamp: {timestamp}\n")

def check_restart():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    if os.path.exists("restart_simu.txt"):
        with open("persistence_log.txt", "a") as log:
            log.write("\n[Restart Detected]\n")
            log.write(f"Timestamp: {timestamp}\n")
    else:
        with open("persistence_log.txt", "a") as log:
            log.write("\n[First time restart]\n")
            log.write(f"Timestamp: {timestamp}\n")

    with open("restart_simu.txt", "w") as f:
        f.write("Simulated reboot marker")
```
- Creates a fake file `fake_file.txt` after each calculation.
- Simulates persistence by logging system start-up behavior.
- Detects simulated system restarts and logs them in `persistence_log.txt`.

---

## 🚀 Installation

```bash
# Clone repository
git clone https://github.com/ZeroOne/TrojanCalculatorSimulator.git

# Navigate to directory
cd TrojanCalculatorSimulator

# Run with Python
python3 trojan_calculator_simulator.py
```

**Requirements**:  
- Python 3.7+
- Tkinter (included in standard Python)

---

## 📜 Version Information

### v1.5 Release Notes
- **Persistence Simulation**: Simulates adding the program to system startup with logging
- **Reboot Detection**: Detects and logs simulated system restart actions
- **Enhanced File Operations**: Creates additional log files for better tracking
- **Improved User Interface**: Refined error handling and feedback mechanisms

### Planned Upgrades (v2.0)
```diff
+ Addition of keylogger simulation for educational purposes
+ Multi-platform support
+ Historical activity viewer
```

---

## 💡 Educational Scenarios

1. **Demo 1**: Perform calculation → Create fake file
2. **Demo 2**: Simulate persistence by logging to `persistence_log.txt`
3. **Demo 3**: Simulate system restart detection and logging

---

## 🛑 Critical Reminder

**This tool is strictly for**:  
✅ Educational purposes  
✅ Security awareness training  
✅ Safe lab environments  

**Never use for**:  
❌ Actual penetration testing  
❌ Malicious activities  
❌ Production systems  

---

## 🤝 Contributing

We welcome contributions! Please follow our [Contribution Guidelines](CONTRIBUTING.md) and:
- 🔍 Submit bug reports via Issues
- 💡 Suggest features using GitHub Discussions
- ✨ Send pull requests for enhancements

---

## 📚 Learning Resources

1. [MITRE ATT&CK Framework](https://attack.mitre.org/)
2. [OWASP Top 10](https://owasp.org/www-project-top-ten/)
3. [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

*Version 1.5 - Designed with ❤️ for the cybersecurity community*  
*"Knowledge is the best antivirus"* 🔐

---

