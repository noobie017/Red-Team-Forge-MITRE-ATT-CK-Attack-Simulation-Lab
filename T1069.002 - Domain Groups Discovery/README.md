T1069.002 - Domain Groups Discovery (Controls Assessment)
This lab segment simulates an execution attempt of MITRE ATT&CK T1069.002 (Domain Groups Discovery) from a non-elevated user context (ADPRO\jcruz).
The objective of this exercise was to evaluate Active Directory structural mapping capabilities under restricted user privileges and to capture the resulting behavioral footprint using Splunk.

Simulation Parameters
Attacker Host: Kali Linux (192.168.10.250)

Target Host: Windows 10 Workstation (192.168.10.9)

Target Domain Context: ADPRO.local (Active / Domain Controller Online at 192.168.10.7)

Initial Access Shell: Metasploit Framework (Meterpreter Reverse TCP - Low Privilege)

Defensive Monitoring: Sysmon + Splunk Enterprise Forwarder

Sequence of Execution & Alternative Methodologies
Unlike user enumeration (net user /domain), which may face access restrictions (System Error 5) in hardened environments,
Active Directory natively allows authenticated domain accounts to query structural group organizations.

The following methodologies were implemented to contrast legacy tools against modern API enumeration:

Method A: Native Binary Execution (Standard Shell)
From an interactive command shell channel (shell) operating under the low-privilege ADPRO\jcruz context, the following native commands were executed:

1.Enumerate Global Domain Groups:
Queries the Domain Controller to pull a complete list of all global and security groups established in the domain:

DOS
net group /domain 

net group "Enterprise Admins" /domain

whoami /groups
