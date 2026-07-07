T1059.001 - Graphical User Interface Intrusion Simulation
This lab segment simulates a post-exploitation action mapped to MITRE ATT&CK T1059.001 (PowerShell) to perform graphical user disruption. 
The objective of this exercise was to contrast headless execution failures against interactive desktop process execution (execute -i) and to document the behavioral differences in process creation logs.

Simulation Parameters
Attacker Host: Kali Linux (192.168.10.250)

Target Host: Windows 10 Workstation (192.168.10.9)

Active Session: Meterpreter Reverse TCP (Session 7)

Execution Context: Standard User (ADPRO\jcruz)

Payload Binary: powershell.exe calling .NET PresentationFramework

Execution Methodologies & Behavioral Analysis
During this exercise, two different execution frameworks were contrasted to analyze how Windows handles graphical user interface (GUI) elements from remote administrative sessions.

Method A: Headless Execution (Standard Shell Channel) — FAILED STATE
Attempting to run a GUI-based script directly inside a basic command-line channel causes the process to hang indefinitely. Because the shell channel does not possess a visible desktop session token, 
the message boxes spawn invisibly in the background, waiting for user interaction that cannot occur.

C:\Users\jcruz\Downloads> powershell -Command "Add-Type -AssemblyName PresentationFramework; 1..10 | ForEach-Object { [System.Windows.MessageBox]::Show('TOO SLOW!', 'ALERT', 'OK', 'Warning') }"
Result: Terminal freeze. Requires hard termination (Ctrl + C).


Method B: Interactive Memory Execution (Meterpreter Runtime) — SUCCESS STATE
To bypass the headless terminal limitation, Meterpreter’s native execute command was leveraged with the interactive (-i) flag. 
This explicitly commands Windows to channel the thread injection directly into the active graphical desktop session of the logged-in user, causing the windows to pop up visually.

meterpreter > execute -H -i -f powershell.exe -a "-Command \"Add-Type -AssemblyName PresentationFramework; 1..10 | ForEach-Object { [System.Windows.MessageBox]::Show('TOO SLOW!', 'ALERT', 'OK', 'Warning') }\""
