# T1059 / T1047 - Remote Process Creation

## Description
This technique demonstrates remote process creation on a Windows target from a Linux attacker machine. By using legitimate Windows binaries such as `calc.exe` and `notepad.exe`, 
we simulate how an attacker can remotely spawn processes on a compromised system.

**MITRE ATT&CK Techniques:**
- T1059 – Command and Scripting Interpreter
- T1047 – Windows Management Instrumentation (WMI)

---

## Lab Environment

- **Attacker Machine:** Kali Linux (`192.168.10.250`)
- **Target Machine:** Windows 10 Workstation (`192.168.10.9`)
- **Domain:** ADPRO
- **Credentials Used:** RedTeam
- **Objective:** Remotely create processes on the target system

---

## Execution Steps

### Method Used: Impacket Wmiexec

**Launch Calculator:**
bash
impacket-wmiexec RedTeam@192.168.10.9 "cmd.exe /c calc.exe"

Results Status: Successful Successfully created remote processes on the target machine.
calc.exe and notepad.exe were spawned using WMI.
Demonstrated the ability to execute arbitrary processes remotely with valid credentials.

