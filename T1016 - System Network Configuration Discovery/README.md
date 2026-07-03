T1016 - System Network Configuration Discovery

This lab segment simulates an execution attempt of MITRE ATT&CK T1016 (System Network Configuration Discovery) within a restricted laboratory environment where the Active Directory (AD) Domain Controller is offline.
The objective of this exercise was twofold: to validate the target endpoint's defensive detection capabilities under a least-privilege operational constraint and to map the resulting network profiling behavioral footprint
using Splunk.

Simulation Parameters
Attacker Host: Kali Linux (192.168.10.250)

Target Host: Windows 10 Workstation (192.168.10.9)

Target Domain Context: ADPRO.local (Offline / Domain Controller Unreachable)

Initial Access Shell: Metasploit Framework (Meterpreter Reverse TCP)

Defensive Monitoring: Sysmon + Splunk Enterprise Forwarder

Sequence of Execution & Technical Troubleshooting
The target objective was to harvest internal IP routing paths, active interfaces, network adapter parameters, and DNS configurations from a non-elevated user context.

Two distinct methodology variations were executed to contrast their telemetry generation within the SIEM environment:

Method A: Native Binary Execution (Standard Shell)
Upon establishing an interactive command shell channel from the active Metasploit session (shell), system context enumeration verified that the runtime environment was limited to a standard, 
non-administrative user profile: ADPRO\jcruz. The following native Windows utilities were invoked to simulate standard host network profiling:

Local Network Interface and DNS Enumeration:

ipconfig /all

route print

netstat -ano
