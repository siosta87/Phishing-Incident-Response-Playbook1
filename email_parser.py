{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww15220\viewh15600\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import re\
import argparse\
from email import policy\
from email.parser import BytesParser\
\
def extract_indicators(email_path):\
    print(f"[*] Analyzing email file: \{email_path\}\\n")\
    \
    with open(email_path, 'rb') as fp:\
        msg = BytesParser(policy=policy.default).parse(fp)\
        \
    print(f"[+] Subject: \{msg['subject']\}")\
    print(f"[+] From: \{msg['from']\}")\
    print(f"[+] To: \{msg['to']\}")\
    print(f"[+] Date: \{msg['date']\}")\
    print("-" * 50)\
    \
    body = ""\
    if msg.is_multipart():\
        for part in msg.walk():\
            content_type = part.get_content_type()\
            if content_type == "text/plain" or content_type == "text/html":\
                try:\
                    body += part.get_payload(decode=True).decode()\
                except Exception:\
                    pass\
    else:\
        body = msg.get_payload(decode=True).decode()\
        \
    # Find URLs\
    urls = re.findall(r'https?://(?:[-\\w.]|(?:%[\\da-fA-F]\{2\}))+', body)\
    unique_urls = list(set(urls))\
    \
    print(f"[!] Extracted URLs (\{len(unique_urls)\} found):")\
    for url in unique_urls:\
        # Defang URL to make it safe to print\
        defanged = url.replace("http://", "hxxp://").replace("https://", "hxxps://").replace(".", "[.]")\
        print(f"  - \{defanged\}")\
        \
    # Find Attachments\
    print("-" * 50)\
    print("[!] Attachments:")\
    attachments_found = False\
    for part in msg.walk():\
        if part.get_content_disposition() == 'attachment':\
            filename = part.get_filename()\
            print(f"  - File Name: \{filename\}")\
            print(f"    Content Type: \{part.get_content_type()\}")\
            attachments_found = True\
            \
    if not attachments_found:\
        print("  - No attachments found.")\
\
if __name__ == "__main__":\
    # Example command line usage:\
    parser = argparse.ArgumentParser(description="Extract simple IOCs from .eml files")\
    parser.add_argument("email_file", help="Path to raw .eml file")\
    args = parser.parse_args()\
    extract_indicators(args.email_file)\
}