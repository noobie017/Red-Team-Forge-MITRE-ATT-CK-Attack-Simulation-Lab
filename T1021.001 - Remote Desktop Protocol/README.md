# T1133 / T1021.001 - External Remote Services: Remote Desktop Protocol (RDP)

## Description
This technique involves using Remote Desktop Protocol (RDP) to gain interactive graphical access to a target system. RDP is one of the most common methods for initial access and lateral movement in real-world attacks.

**MITRE ATT&CK Techniques:** 
- T1133 - External Remote Services  
- T1021.001 - Remote Services: Remote Desktop Protocol

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Method:** Enabled RDP + created dedicated admin account (`RedTeam`)

---

## Execution Steps Performed

1. Enabled RDP via Registry:
 cmd
   reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

2.Allowed RDP through Windows Firewall.

3.Created new admin user:
cmd
net user RedTeam P@ssw0rd123 /add
net localgroup administrators RedTeam /add

Attempted connection using:
xfreerdp - failed 
Remmina (GUI) - failed 

Results
Status: Partially Successful
Successfully enabled RDP service on target.
Successfully created new administrative user (RedTeam).
Confirmed RDP port (3389) is listening.
Failed to establish graphical RDP connection from Kali (Remmina & xfreerdp both failed with "Cannot connect to the RDP server").

Possible Reasons for Failure:Network-level firewall blocking inbound RDP
Domain authentication issues
Target-side security settings (Windows Defender, network profile)




