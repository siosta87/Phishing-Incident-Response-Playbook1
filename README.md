# Phishing Incident Response Playbook and Email Header Reader

An educational incident-response documentation project with a small Python utility for inspecting raw email headers.

## Included files

- [phishing_incident_playbook.md](phishing_incident_playbook.md): written response playbook
- [email_headers.py](email_headers.py): reads an email file and prints its headers

## Run the header reader

Requires Python 3 with the standard-library email package. Use a saved lab email in .eml format.

```console
python email_headers.py sample.eml
```

The filename was changed from email.py to avoid shadowing Python's built-in email package. A sample.eml fixture is not currently included.

## What the script does

Prints From, To, Subject, Date, and Message-ID, followed by the complete parsed header list. The script reads a local file and does not send messages.

## Scope and limitations

- This is a learning project, not a validated production incident-response platform.
- The current script does not extract URLs, attachment hashes, or a complete IOC report.
- It does not verify SPF, DKIM, or DMARC results independently. Header values are evidence to assess, not proof of sender identity.
- File errors and malformed messages need stronger error handling.
- No automated tests or captured execution results are included.

## Related repository

The similarly named Phishing-Incident-Response-Playbook repository was an empty placeholder. This repository contains the actual playbook and Python utility.
