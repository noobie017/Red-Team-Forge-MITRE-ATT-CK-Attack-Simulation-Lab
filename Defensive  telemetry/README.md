### Blue Team Detection & Defensive Telemetry

Welcome to the Defensive Telemetry and Detection Engineering directory of the **Red-Team-Forge** laboratory. 
This section documents the exact behavioral footprints, log analysis, and threat hunting strategies developed by analyzing adversarial simulations inside a closed Security Operations Center (SOC) environment.

Rather than relying purely on static signature alerts (which can be easily bypassed), 
the focus here is on **behavioral analysis** utilizing Microsoft Sysmon and Windows Event logs ingested into a Splunk Enterprise instance.

---

### Lab Infrastructure & Telemetry Stack
* **SIEM Platform:** Splunk Enterprise (Local Instance)
* **Endpoint Logging:** Microsoft Sysmon (System Monitor) v15+ & Windows Security Event Logs
* **Log Forwarder:** Splunk Universal Forwarder
* **Attack Platform:** Kali Linux 2026.x (Metasploit Framework / Meterpreter C2)
* **Target Environment:** Windows 10 Enterprise (Host: `target-pc.adpro.local`)

---

### Core Detection Playbooks

### 1. Adversarial Process Injection & Spawning
* **MITRE ATT&CK Mapping:** [T1059 - Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)
* **Scenario:** An attacker utilizes an active Meterpreter memory-resident session to inject into the Windows API and spawn a native application (e.g., `execute -f msedge.exe`) to blend in with normal background activity.
* **The Behavioral Footprint:** When interactive processes are launched via a C2 agent, they bypass the traditional command-line shell (`cmd.exe` or `powershell.exe`).
This results in an anomalous **Parent-Child process lineage** where the threat binary is listed directly as the creator, often accompanied by a stripped or missing `CommandLine` string.
