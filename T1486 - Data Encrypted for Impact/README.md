# T1486 - Data Encrypted for Impact

## Description
This technique involves encrypting or locking files on a compromised system to deny access to the legitimate user. It is commonly associated with ransomware-style attacks and falls under the Impact tactic.


---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Access Level:** Administrator (via Impacket PsExec / WinRM)
- **Objective:** Lock or encrypt target files to deny user access

---

## Execution Steps

### 1. Identify Target Files

`cmd
dir C:\Users\jcruz\Desktop
