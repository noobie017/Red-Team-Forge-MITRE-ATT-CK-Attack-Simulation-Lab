# T1005 - Data from Local System

## Description
This technique involves searching and collecting sensitive data from the local system after gaining access. Attackers commonly look for documents, credentials, configuration files, and other valuable information.

**MITRE ATT&CK Technique:** [T1005 - Data from Local System](https://attack.mitre.org/techniques/T1005/)

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Access Level:** Administrator (via Impacket PsExec)

---

## Execution Steps

### 1. File Discovery Commands

cmd
dir C:\Users /s /b | findstr /i "\.txt \.doc \.docx \.xls \.xlsx \.pdf \.db"
cmd

dir C:\ /s /b | findstr /i "password\|credential\|config\|login"

cmd

tree C:\Users\ /f > C:\Windows\Temp\filelist.txt

2. Copy Interesting Files (Example)cmd

copy C:\Users\jcruz\Desktop\*.txt C:\Windows\Temp\

Results
Successfully accessed the target with Administrator privileges.
Performed local file discovery using built-in Windows commands.
Copied selected files from user Desktop to a central temporary location (C:\Windows\Temp).
Identified structure of user directories and potential sensitive files.

Challenges:
Limited interesting files found during search (typical in clean lab environments).
Focused on common file extensions and keywords.


