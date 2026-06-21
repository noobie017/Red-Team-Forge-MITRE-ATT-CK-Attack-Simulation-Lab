### MITRE ATT&CK T1547.001- Simulating Persistence via Windows Registry Run Keys 

### Overview
This documents a successful hands-on implementation of an adversarial persistence mechanism within a sandboxed Windows 10 enterprise environment.
Operating under a low-privilege domain user context (`jcruz`), a registry-based backdoor was established via a remote Meterpreter session. 
The implementation was verified through both visual host-based actions and centralized log analysis within Splunk.

The primary objective of this exercise was to simulate a standard adversarial technique—leveraging the Current User Registry Hive—to achieve 
execution persistence across system reboots without requiring local or domain administrative privileges.

---

### Technical Concept: User Hive Persistence
Unlike system-wide persistence mechanisms (such as Windows Services or Local Machine Run Keys) that mandate local administrative privileges (`NT AUTHORITY\SYSTEM` or `Administrators`), 
the `HKEY_CURRENT_USER` (HKCU) registry hive is entirely accessible to the logged-in user. 

Adversaries abuse the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` path because the Windows subsystem implicitly trusts and executes any string commands populated here 
immediately following user authentication. This technique effectively mirrors the legitimate startup behaviors of common consumer software (e.g., Steam, Discord) to blend into baseline system activity.

---

### Lab Architecture & Environment
* **Attacking Host:** Kali Linux (Rolling Release) operating Metasploit Framework (`msfconsole`).
* **Target Endpoint:** Windows 10 Enterprise (Active Directory Domain Joined to an offline Domain Controller).
* **User Context:** `ADPRO\jcruz` (Standard Domain User / Non-Administrative).
* **SIEM Monitoring:** Splunk Enterprise capturing host telemetry forwarded via Sysmon.

---

## Execution code 

meterpreter > shell
C:\Users\jcruz\Downloads>

C:\Users\jcruz\Downloads> reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "Duckpersistence" /t REG_SZ /d "C:\Users\jcruz\Pictures\Duck.jpeg" /f

The operation completed successfully.
