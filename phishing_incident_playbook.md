{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww14660\viewh10200\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Phishing Incident Response Playbook\
\
## Objective\
Define a standardized, repeatable workflow for security analysts to detect, analyze, contain, and recover from email-based phishing attacks, specifically targeting credential harvesting and malicious attachments.\
\
---\
\
## Workflow Overview\
\
---\
\
## Phase 1: Preparation\
Establishing policies, tools, and defenses before an incident occurs to minimize impact and facilitate rapid response.\
\
### 1. Technical Controls & Hardening\
*   **Email Authentication:** Enforce SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail), and DMARC (Domain-based Message Authentication, Reporting, and Conformance) policies with a reject/quarantine disposition.\
*   **Spam & Content Filtering:** Configure secure email gateways (SEGs) to flag external emails, block high-risk attachment extensions (e.g., `.exe`, `.scr`, `.vbs`, `.js`, password-protected zip files without scanning), and rewrite URLs.\
*   **Endpoint Defense:** Ensure Endpoint Detection and Response (EDR) agents are fully updated, configured to block malicious execution, and reporting logs to a central SIEM.\
\
### 2. Analytical Readiness\
*   **Tool Checklist:** Secure Sandbox (e.g., Any.Run, Cuckoo), Threat Intelligence APIs (e.g., VirusTotal, URLVoid), Mailbox Admin Center, SIEM console.\
*   **Reporting Mechanism:** Implement a "Report Phishing" button in employee email clients to facilitate easy ingestion of suspected emails.\
\
---\
\
## Phase 2: Detection & Triage\
Identifying potential phishing incidents through user reports or automated alerts.\
\
### 1. Ingestion Channels\
*   **User Reports:** Emails forwarded to the designated Security Operations Center (SOC) mailbox (e.g., `abuse@company.com`).\
*   **Automated Alerts:** High-volume inbound email anomalies, bulk mail triggers, or threat intelligence feeds matching active campaigns.\
\
### 2. Initial Classification & Triage\
Categorize the phishing email into one of the following buckets:\
1.  **Credential Harvesting:** Emails containing links to spoofed login portals designed to steal credentials.\
2.  **Malicious Attachment:** Emails containing payloads (malware, ransomware, macro-enabled documents).\
3.  **Business Email Compromise (BEC):** Social engineering/spoofing to initiate unauthorized wire transfers or sensitive data disclosure (no direct link/payload).\
4.  **Spam / False Positive:** Non-malicious bulk marketing or safe emails.\
\
---\
\
## Phase 3: Analysis\
Deep-dive investigation to understand the scope and nature of the threat.\
\
### 1. Header Analysis\
Analyze the raw email header (`.eml` or `.msg` file) to verify sender authenticity:\
*   **Return-Path vs. From Address:** Check for mismatches.\
*   **DKIM & SPF Results:** Confirm if the email passed authentication (`spf=pass`, `dkim=pass`).\
*   **Message-ID:** Inspect for abnormal domains or formatting.\
*   **Hop Analysis:** Track the path the message took via the `Received:` headers to find the true originating IP.\
\
### 2. URL & Payload Analysis\
*   **Static URL Analysis:** Safely defang the URL (e.g., change `http://` to `hxxp://`) to prevent accidental clicking. Check against reputation engines (e.g., VirusTotal).\
*   **Dynamic URL Analysis:** Open the link within an isolated browser or sandbox environment to observe redirect chains and detect credential harvesting login fields.\
*   **Attachment Analysis:**\
    *   Calculate file hashes (MD5, SHA-256) of the attachment.\
    *   Search hashes in Threat Intelligence databases.\
    *   Submit suspicious files to a secure sandbox to observe process creation, registry modifications, and outbound network traffic.\
\
### 3. Scope Assessment\
Determine how many users received the email:\
*   Run a message trace across the mail server using the Subject line, Sender address, or Sender IP.\
*   Identify if any recipients opened the attachment or clicked the link (cross-reference proxy/DNS logs with the malicious domains/IPs).\
\
---\
\
## Phase 4: Containment\
Preventing the threat from spreading or causing further damage.\
\
### 1. Network & Mailbox Isolation\
*   **Email Recall/Purge:** Programmatically delete or quarantine the malicious email from all target mailboxes using server-level administrative scripts.\
*   **URL/IP Blocking:** Update the secure gateway, DNS server, or proxy configurations to block outbound access to the identified malicious URLs and IPs.\
*   **Firewall Rules:** Block traffic to/from originating malicious IP addresses.\
\
### 2. Host-Level Containment (If Malware Executed)\
*   **Isolate Affected Hosts:** Disconnect compromised endpoints from the local network/Wi-Fi via the EDR console to prevent lateral movement.\
*   **Revoke Sessions:** Force-expire active user sessions across all SaaS and internal enterprise applications (e.g., Microsoft 365, Google Workspace).\
\
---\
\
## Phase 5: Eradication\
Eliminating the root cause of the incident and all remnants of the threat.\
\
### 1. Threat Removal\
*   **Account Remediation:** Reset passwords and revoke OAuth tokens/permissions for all users who interacted with credential harvesting links.\
*   **Host Cleanup:** Run EDR-guided remediation scans or re-image affected machines to ensure absolute malware eradication.\
*   **Spam Filter Updates:** Add the sender's domain, IP address, and payload hashes to the blocklist in the secure email gateway.\
\
---\
\
## Phase 6: Recovery & Post-Incident Activity\
Restoring affected assets to normal production and leveraging the incident to improve future response.\
\
### 1. Recovery\
*   **Restore Endpoint Access:** Reconnect cleaned systems to the production network.\
*   **Monitor Activity:** Implement continuous monitoring (for at least 48-72 hours) on affected user accounts for anomalous login locations, MFA modification attempts, and outbound forwarding rules creation.\
\
### 2. Post-Incident Review (Lessons Learned)\
*   **Root Cause Analysis (RCA):** Determine how the email bypassed security controls (e.g., why did the gateway fail to block it?).\
*   **Policy & Rules Optimization:** Refine mail gateway rules, SPF policies, or SIEM correlation rules based on new indicators.\
*   **User Training:** Enroll users who fell victim to the phishing attack in targeted security awareness training.\
}