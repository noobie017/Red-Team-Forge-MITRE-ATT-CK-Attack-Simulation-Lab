MITRE ATT&CK T1087.001 - Account Discovery: Local Account (Controls Assessment)

This lab segment simulates an execution attempt of MITRE ATT&CK T1087.001 (Account Discovery: Local Account) within a dedicated Active Directory (AD) laboratory environment. The objective of this exercise was twofold: to validate the target endpoint's defensive detection capabilities and to evaluate how security controls behave under specific operational constraints.

Simulation Parameters
Attacker Host: Kali Linux (192.168.10.250)

Target Host: Windows 10 Workstation (192.168.10.9)

Target Domain Context: ADPRO.local

Initial Access Shell: Metasploit Framework (Meterpreter Reverse TCP)

Defensive Monitoring: Sysmon + Splunk Enterprise Forwarder

Sequence of Execution & Technical Troubleshooting
The target objective was to interface with the local Security Accounts Manager (SAM) configuration database using native utility binaries and PowerShell scripting extensions to harvest active system profiles.

The following timeline details the execution steps, architectural roadblocks encountered, and troubleshooting methodologies applied:

1. Initial Context Discovery
Upon establishing a command and control (C2) channel to the target workstation, context enumeration was performed via the meterpreter interface to drop into an interactive shell environment matching the target's download path context: C:\Users\jcruz\Downloads>.

2. Native Binary Query Execution
To simulate a fast, low-overhead administrative reconnaissance technique, the legacy system administration command structure was invoked. This utility queries the system directly to output an index of all existing local machine profiles:

DOS
net user
3. Advanced Scripting Enumeration
To evaluate deeper script auditing and bypass local execution restriction constraints, an explicit object-oriented commandlet structure was passed to the PowerShell subsystem. This command targets specific structural attributes—specifically Name, Enabled status, and profile descriptions:

DOS
powershell -ExecutionPolicy Bypass -Command "Get-LocalUser | Select-Object Name, Enabled, D
