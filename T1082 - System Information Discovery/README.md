MITRE ATT&CK T1082 - System Information Discovery (Controls Assessment)
This lab segment simulates an execution attempt of MITRE ATT&CK T1082 (System Information Discovery) within a restricted laboratory environment where the Active Directory (AD) Domain Controller is offline. The objective of this exercise was twofold: to validate the target endpoint's defensive detection capabilities under a least-privilege operational constraint and to map the resulting behavioral footprint using Splunk.

Simulation Parameters
Attacker Host: Kali Linux (192.168.10.250)

Target Host: Windows 10 Workstation (192.168.10.9)

Target Domain Context: ADPRO.local (Offline / Domain Controller Unreachable)

Initial Access Shell: Metasploit Framework (Meterpreter Reverse TCP)

Defensive Monitoring: Sysmon + Splunk Enterprise Forwarder

Sequence of Execution & Technical Troubleshooting
The target objective was to harvest detailed operating system properties, hardware configurations, and patch levels from a non-elevated user context without relying on active domain authentication.

The following timeline details the execution steps, architectural roadblocks encountered, and troubleshooting methodologies applied:

1. Initial Context Discovery
Upon establishing an interactive command shell channel from the active Metasploit session, system context enumeration verified that the runtime environment was limited to a standard, non-administrative user profile: ADPRO\jcruz. Because the Active Directory server was shut off, domain-level privilege escalation vectors were restricted.

2. Local System Architecture Query
To simulate a low-privilege host-mapping technique, a native utility binary was executed from the interactive shell. This command queries the local registry and system files directly to aggregate extensive OS configurations, product IDs, uptime statistics, and hotfix patch data:

DOS
systeminfo

hostname
