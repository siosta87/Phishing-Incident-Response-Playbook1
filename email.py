import email
from email import policy
from email.parser import BytesParser

def parse_email_headers(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
    
    print(f"From: {msg['from']}")
    print(f"To: {msg['to']}")
    print(f"Subject: {msg['subject']}")
    print(f"Date: {msg['date']}")
    print(f"Message-ID: {msg['message-id']}")
    
    print('\nAll Headers:')
    for header, value in msg.items():
        print(f"{header}: {value}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        parse_email_headers(sys.argv[1])
    else:
        print("Please provide the path to an email file.")
