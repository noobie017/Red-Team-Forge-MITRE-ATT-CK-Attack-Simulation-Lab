### Core Splunk Search Queries

To locate the execution of the attack within Splunk, the following search strings were deployed against the log indexes:

#### 1. Tracking the Creation Event (Windows Security Log)
This query hunts for the explicit registration of a new task by targeting the built-in Windows Security event sub-tree.
```splunk
index=win_security EventCode=4698 TaskName="*TimedTelemetry*"
