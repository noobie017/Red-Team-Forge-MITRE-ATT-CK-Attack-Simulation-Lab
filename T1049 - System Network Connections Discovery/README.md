# T1049 - System Network Connections Discovery

## Technical Overview
Adversaries may attempt to get a listing of network connections to or from the compromised system to map out the network topology. 
This technique allows threat actors to identify active network configurations, established sessions, and potential high-value internal targets (such as Domain Controllers or file servers) that the host is actively communicating with.

In this simulation, discovery is executed via native Windows command-line tools, PowerShell, and remote exploitation frameworks (Meterpreter) to analyze the differences in defensive telemetry generation.

---

## Simulation Procedures

### Method 1: Windows Command Line (Native)
Executes a basic network status query using standard Windows binaries.
CMD
netstat -ano


### Method 2: PowerShell (Living off the Land)
Queries the network subsystem directly via PowerShell script blocks, filtering exclusively for active network connections to avoid unnecessary noise.

PowerShell
Get-NetTCPConnection -State Established

### Method 3: Meterpreter (Memory-Only Execution)
Executed from an active Kali Linux session. This method queries network connections via direct API calls within the memory space of the injected process, bypassing standard process creation logging.

Bash
meterpreter > netstat
