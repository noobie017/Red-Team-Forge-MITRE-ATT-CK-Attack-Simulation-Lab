### 
SPL 
index=* source="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1 
| search (Image="*\\ipconfig.exe") OR (Image="*\\route.exe") OR (Image="*\\netstat.exe")
| table _time, Computer, User, Image, ParentImage, CommandLine

