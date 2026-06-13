**Red Team Forge: MITRE ATT&CK Attack Simulation Lab**

###
A hands-on, realistic home lab dedicated to learning and implementing real adversary techniques from the MITRE ATT&CK framework.
This lab is built for red teamers, penetration testers, and security professionals who want to move beyond theory and actually execute, refine,
and understand modern attack methods in a controlled Active Directory environment.


**Lab Objectives**
Deeply understand and implement MITRE ATT&CK techniques through practical execution
Build strong red teaming and adversary emulation skills
Learn how real attacks work at a technical level (Initial Access to Impact)
Master living-off-the-land, custom tooling, and evasion techniques
Develop professional attack playbooks and document lessons learned
Understand detections from the attacker’s perspective

**Key Features**
Realistic mini Active Directory environment
High-quality Sysmon telemetry (optional blue-team visibility)
Full attack lifecycle simulation using Atomic Red Team and custom tools
Focus on execution quality, OpSec, and evasion
Structured progression from basic to advanced adversary techniques

**Lab Architecture**
| Component              | Operating System          | Role |
|------------------------|---------------------------|------|
| **Attacker**           | Kali Linux                | Command & Control, attack platform |
| **Domain Controller**  | Windows Server 2022       | Active Directory Domain Controller |
| **Endpoint**           | Windows 10 (domain-joined)| Primary victim workstation |
| **Optional Endpoints** | Windows 10/11             | Lateral movement practice |
| **Monitoring (Optional)** | Ubuntu Server          | Splunk Enterprise + Sysmon telemetry |

