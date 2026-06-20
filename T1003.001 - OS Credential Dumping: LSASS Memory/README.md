### MITRE ATT&CK T1003.001 - OS Credential Dumping: LSASS Memory (Controls Assessment)

This lab segment simulates an execution attempt of **MITRE ATT&CK T1003.001 (OS Credential Dumping: LSASS Memory)** within a dedicated Active Directory (AD) laboratory environment.
The objective of this exercise was twofold: to validate the target endpoint's defensive detection capabilities and to evaluate how security controls behave under specific operational constraints.

---

### Simulation Parameters
* **Attacker Host:** Kali Linux (`192.168.10.250`)  
* **Target Host:** Windows 10 Workstation (`192.168.10.9`)  
* **Target Domain Context:** `ADPRO.local`  
* **Initial Access Shell:** Metasploit Framework (Meterpreter Reverse TCP)  
* **Defensive Monitoring:** Sysmon + Splunk Enterprise Forwarder  

---

### Sequence of Execution & Technical Troubleshooting

The target objective was to interface with the Local Security Authority Subsystem Service (`lsass.exe`) process memory using Metasploit's post-exploitation toolkit (`kiwi` / `Mimikatz`) to harvest password hashes. 



The following timeline details the execution steps, architectural roadblocks encountered, and troubleshooting methodologies applied:

### 1. Initial Context Discovery
Upon establishing a command and control (C2) channel to the target workstation, context enumeration was performed via the meterpreter interface:
meterpreter
meterpreter > getuid
Server username: ADPRO\jcruz

### 2. Standard Privilege Elevation Failure
meterpreter > getsystem
[-] priv_elev_getsystem: Operation failed: All pipe instances are busy.

### 3. User Account Control (UAC) Bypass Attempt
msf exploit(multi/handler) > use exploit/windows/local/bypassuac_sdclt
msf exploit(windows/local/bypassuac_sdclt) > set SESSION 1
msf exploit(windows/local/bypassuac_sdclt) > exploit
[-] Exploit aborted due to failure: no-access: Not in admins group, cannot escalate with this module 

Constraint:
Due to host system RAM limitations preventing the simultaneous execution of all 4 virtual machines (Domain Controller, Splunk, Kali, and Windows 10 Workstation),
the Active Directory Domain Controller was powered down during this specific testing sequence.
Impact:
With the Domain Controller offline, the Windows 10 target operated solely on cached domain credentials. The operating system structurally hardened its access control lists (ACLs) and
prevented any cross-process pivoting or standard token manipulations by the unverified domain user.

Final Assessment Result: ATTACK FAILED
