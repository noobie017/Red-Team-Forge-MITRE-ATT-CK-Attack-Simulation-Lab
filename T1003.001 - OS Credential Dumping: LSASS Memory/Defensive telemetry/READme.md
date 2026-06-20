# Defensive Telemetry: Tracking Failed LSASS Exploitation Attempts

This documents the telemetry captured in Splunk during an attempted credential dumping attack (MITRE ATT&CK T1003.001). 
Although host security controls blocked access to LSASS, Sysmon successfully recorded distinct Indicators of Compromise (IoCs).

---

###Splunk Ingestion Proof

The following process creation events (Sysmon Event ID 1) were indexed on the Splunk server during the attack window:

---

### Telemetry Breakdown & Suspicious Activity

To a SOC analyst, these logs reveal a clear pattern of automated post-exploitation behavior:

### 1. Hidden Privilege Enumeration (`getsystem`)
* **Log:** `cmd.exe /c whoami /groups` executed under `ADPRO\jcruz`.
* **The Reality:** When `getsystem` was run in Metasploit, the framework secretly spawned this process in the background. It ran `whoami /groups` to
check if the compromised account belonged to the local Administrators group. 

### 2. Stealthy Framework Cleanup (`rmdir /s /q`)
* **Log:** `cmd.exe /q /c rmdir /s /q "C:\Users\jcruz\AppData\Local\Microsoft\OneDrive\..."`
* **The Reality:** The `/q` flag stands for **"Quiet Mode"** (suppressing user prompts) and `/s` forces directory tree deletion. 
Because the Metasploit modules failed to elevate privileges, the framework automatically executed these silent deletions to erase its staging files and evade detection.

---

### Key Takeaway
**A failed attack is still a visible attack.** Even though the OS protected the LSASS process, Metasploit's troubleshooting actions left a loud trail. 
Monitoring for unauthorized group enumeration and hidden directory wipes (`rmdir /q`) allows defenders to easily flag compromised standard user sessions.
