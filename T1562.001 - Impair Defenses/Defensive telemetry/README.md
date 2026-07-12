SPL ---- index=* (psexec OR impacket OR "svcctl" OR "CreateService" OR "OpenService" OR "WMI" OR "RPC")
| table _time, ComputerName, User, ProcessName, CommandLine, ParentProcessName, SourceIP
| sort -_time
