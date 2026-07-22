# T1560.002 - Archive Collected Data: Password Protected Zip/RAR

## Description
This technique involves compressing collected data and protecting it with a password before exfiltration. It helps reduce file size and adds a layer of protection during transfer.

**MITRE ATT&CK Technique:** [T1560.002 - Archive Collected Data: Password Protected Zip/RAR](https://attack.mitre.org/techniques/T1560/002/)

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Access Level:** Administrator (via Impacket PsExec)
- **Objective:** Collect, compress, and password-protect data for exfiltration

---

## Execution Steps

### 1. Data Collection & Archiving (On Target)

cmd
powershell -c "Compress-Archive -Path C:\Users\jcruz\Desktop -DestinationPath C:\Windows\Temp\stolen.zip"

2. Password-Protected Archive (Advanced)cmd

powershell -c "$zip = 'C:\Windows\Temp\stolen_protected.zip'; Compress-Archive -Path C:\Users\jcruz\Desktop -Destin

ResultsStatus: Successful
Successfully collected data from the user’s Desktop.
Created a compressed archive (stolen.zip).
Demonstrated the ability to password-protect archived data before exfiltration.



