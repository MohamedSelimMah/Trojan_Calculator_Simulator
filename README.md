# Trojan Calculator Simulator (GUI) - Educational Tool v1.0

**Author**: MohamedSelim  
**GitHub**: [ZeroOne](https://github.com/ZeroOne)  
**License**: [MIT](LICENSE)  

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)  
*"Understanding malware through safe simulation"*

---

## 📖 Overview

**Trojan Calculator Simulator v1.0** is an interactive educational tool that demonstrates Trojan horse principles through a functional GUI calculator. This version focuses on basic arithmetic operations paired with simulated benign malicious activity, providing a risk-free environment to learn cybersecurity fundamentals.

**Disclaimer**:  
⚠️ **This is a controlled simulation** containing zero actual malicious code. All "malicious" actions are fake file operations that leave your system completely unharmed.

---

## 🎯 Key Features (v1.0)

### Calculator Core
- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **GUI Interface**: Built with Tkinter for intuitive user interaction
- **Input Validation**: Robust error handling for:
  - Non-numeric inputs
  - Division by zero attempts
  - Empty fields

### Trojan Simulation
- 🕵️ **Stealth Mode**: Creates harmless `.simulated_trojan` files after each calculation
- 📁 **File Simulation**:
  - Generates fake logs with random data
  - Uses system timestamps for realism
  - Stores files in isolated `/simulated_activity` directory
- 🔍 **Transparent Process**: Status messages show simulation details

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
   - Click "Calculate" to get result
4. **Visual Feedback**  
   - Results displayed in green (valid) / red (error)

### Background Simulation
```python
# Sample simulation code (v1)
def create_simulated_file():
    filename = f"simulated_activity/{time.time()}_log.simulated_trojan"
    content = f"SIMULATED ACTIVITY @ {time.ctime()}\nFake data: {random.randint(0,1000)}"
    with open(filename, "w") as f:
        f.write(content)
```
- Creates timestamped text files
- Generates random "fake data" entries
- Automatic cleanup option available

---

## 🚀 Installation

```bash
# Clone repository
git clone https://github.com/ZeroOne/TrojanCalculatorSimulator.git

# Navigate to directory
cd TrojanCalculatorSimulator

# Run with Python
python3 trojan_calculator_gui.py
```

**Requirements**:  
- Python 3.7+
- Tkinter (included in standard Python)

---

## 📜 Version Information

### v1.0 Release Notes
- Initial release with core functionality
- Basic file simulation engine
- Fundamental GUI layout

### Planned Upgrades (v1.5-v2.0)
```diff
+ Advanced simulation features
+ Multi-platform support
+ Interactive tutorial mode
+ Historical activity viewer
+ Localization support
```

---

## 💡 Educational Scenarios

1. **Demo 1**: Perform calculation → Check `/simulated_activity` folder
2. **Demo 2**: Trigger input error → Observe security warning
3. **Demo 3**: Monitor system resources during operation

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

*Version 1.0 - Designed with ❤️ for the cybersecurity community*  
*"Knowledge is the best antivirus"* 🔐
