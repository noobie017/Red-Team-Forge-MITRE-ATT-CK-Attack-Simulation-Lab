### 📬 Mail Delivery Architecture: Lab Simulation vs. Production Internet

In a real-world scenario, sending an unauthenticated spoofed email to a public `@gmail.com` inbox over the internet fails due to fundamental domain security frameworks (**SPF, DKIM, DMARC**).
To replicate initial access controls safely in an isolated lab, we leverage a **local loopback interception technique**.



#### Technical Comparison

| Feature | Real-World Internet Attack | Our Local Lab Simulation |
| :--- | :--- | :--- |
| **Target Address** | Real Public Inbox (`user@gmail.com`) | Simulated Inbox Target (`Cruzjdela293@gmail.com`) |
| **Routing Mechanism** | Public DNS MX Records resolve to Google Mail Servers | `mutt` configuration hardcoded to local IP address relay |
| **Authentication Checks** | Strict validation of SPF, DKIM cryptographic signatures, and DMARC alignment | Completely bypassed by custom Python socket script accepting all payloads |
| **Data Scope** | Data crosses public internet infrastructure | Network data strictly bound to local host host-only / NAT lab subnet |

---

### Simulated Delivery Workflow Summary

1. **The Sender:** The `mutt` client attempts to transmit an email destined for an external target.
2. **The Relay Interception:** Instead of consulting global DNS root zones for Google’s infrastructure, `mutt` connects directly to our listening daemon hosted at `192.168.10.250:25`.
3. **The Fake Handshake:** The custom Python script mimics standard ESMTP response codes (`220`, `250 OK`, `354 Go ahead`), tricking the client into executing a full transaction.
4. **Telemetry Acquisition:** The script dumps the complete plaintext payload (SMTP Headers, Subject, and Phishing URIs) locally to the standard output (`stdout`) for analytical evaluation.
