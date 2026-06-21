# Reconnaissance (MITRE ATT&CK T1595 - Active Scanning)

## Objective
The goal of this phase was to identify active hosts, open ports, and running services on the target system (`192.168.10.9`) to map out potential entry points and understand the target's configuration.

## Execution
An active service scan was conducted from the Kali Linux attack host against the target Windows machine using Nmap.

```bash
nmap -sV 192.168.10.9
