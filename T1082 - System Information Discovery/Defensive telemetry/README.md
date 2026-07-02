SPL detection command 

index=* source="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=4688 Image="*\\systeminfo.exe"
