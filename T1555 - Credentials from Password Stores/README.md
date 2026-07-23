# T1555 - Credentials from Password Stores

## Description
This technique involves searching for and extracting credentials stored in password stores, such as browsers, Windows Credential Manager, or other applications on the compromised system.

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Access Level:** Administrator (via Impacket PsExec)
- **Objective:** Enumerate and extract stored credentials

---

## Execution Steps

### 1. Windows Credential Manager

cmd
cmdkey /list

2. Browser Credential Locations (Chrome Example)cmd

dir "C:\Users\jcruz\AppData\Local\Google\Chrome\User Data\Default" /b

3. Wallet / Other Stored Credentialscmd

powershell -c "Get-ChildItem -Path 'C:\Users\jcruz\AppData\Roaming\Microsoft\Wallets' -Recurse"

ResultsStatus: Partially Successful
Successfully enumerated stored credentials using cmdkey /list.
Identified WindowsLive generic credential.
Located potential browser credential storage paths.
Demonstrated enumeration of password stores on the target system.



