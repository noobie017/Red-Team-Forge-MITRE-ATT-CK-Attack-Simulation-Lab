This repository contains documentation and analyzed log artifacts for detecting Windows local reconnaissance mechanisms (specifically account discovery) within a Security Operations Center (SOC) simulation environment.

 Lab Overview
The goal of this exercise was to simulate an adversary performing post-exploitation internal reconnaissance (MITRE ATT&CK T1087.001 - Local Account Discovery) from an active compromise shell, and to successfully track the resulting forensic footprint using Splunk.

Attacker Infrastructure: Kali Linux (192.168.10.250) running Metasploit Framework (msfconsole).

Target Environment: Windows 10 client (target-pc.adpro.local) operating under the ADPRO domain context.

Logging Solutions: Windows Security Event Auditing and Microsoft Sysmon.

🛠️ Execution & Simulation
Once interactive access was established via a reverse TCP handler session, a native command shell was spawned to inspect host profiles. Two distinct enumeration vectors were executed:
