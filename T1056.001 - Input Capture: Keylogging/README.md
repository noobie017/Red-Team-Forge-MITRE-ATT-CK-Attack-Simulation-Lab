T1056.001 - Input Capture: Keylogging (User-Space Hooking Simulation)
This lab segment simulates the stealthy capture of user keyboard inputs by deploying a user-space monitoring script within local application data directories.
The exercise contrasts the high visibility of running interactive command shells (cmd.exe) against executing unbuffered background processes via Meterpreter API handlers, 
highlighting how defensive engineers map execution artifacts to process telemetry.

Simulation Parameters
Attacker Host: Kali Linux (192.168.10.250)

Target Host: Windows 10 Workstation (192.168.10.9)

Target Profile: C:\Users\jcruz\ (Standard/Least Privilege User)

Target Data Store: Local AppData Roaming Path (windows_update.log)

Sequence of Execution
Instead of running an interactive shell channel which continuously spawns noisy command-line processes, the execution utilizes background process spawning and native virtual filesystem transfers to stage 
the monitoring script and retrieve the telemetry log.

Navigate to the Target Temporary Directory
Change the active working directory directly to the local application repository using environment variables to prepare for file staging:

Code snippet
