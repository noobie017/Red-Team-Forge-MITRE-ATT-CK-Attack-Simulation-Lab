
### T1566.001 - Spearphishing Lab

A controlled red team / adversary emulation lab exercise implementing **MITRE ATT&CK Technique T1566.001 (Spearphishing)** using Gmail and a custom phishing page.

> **Note**: Although titled T1566.001, this exercise primarily demonstrates **T1566.002 (Spearphishing Link)**.

---

### Objective

Simulate a realistic spearphishing campaign in an isolated lab environment by:
- Using Gmail as the email delivery service
- Sending emails via **Mutt** on Linux
- Hosting a simple credential-harvesting phishing page
- Documenting challenges and failure points

---

### Tools Used

| Tool              | Purpose                        |
|-------------------|--------------------------------|
| Gmail             | Email delivery service         |
| Mutt              | Command-line email client      |
| Python http.server / Apache | Hosting phishing page     |
| Custom HTML Page  | Credential harvester           |

---

### Lab Environment

- **OS**: Linux (Kali Linux / Ubuntu)
- **IP Address**: `192.168.10.250`
- **Phishing Site**: `http://192.168.10.250:8080`
- **Network**: Isolated lab network (recommended)
