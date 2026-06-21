### Telemetry Proof (Splunk Capture)
Below is the verified Sysmon capture showing the malicious entry creation. Note the execution of `reg.exe` under the context of `ADPRO\jcruz` targeting the user's specific registry SID hive:
