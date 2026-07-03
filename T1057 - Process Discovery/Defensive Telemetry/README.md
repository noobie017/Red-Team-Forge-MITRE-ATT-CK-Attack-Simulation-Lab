### spl 

index=* source="WinEventLog:Microsoft-Windows-Sysmon/Operational" 
| search (Image="*\\tasklist.exe") OR (CommandLine="*Get-Process*")
| table _time, host, Image, ParentImage, CommandLine
