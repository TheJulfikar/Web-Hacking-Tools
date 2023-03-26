from googlesearch import search
import requests
import re

# input file containing the Google dorks
input_file = "dorks.txt"

# output files
emails_file = "emails.txt"
no_emails_file = "no_emails.txt"

# list of keywords to identify websites that may have a responsible disclosure program
keywords = ["bounty", "reward", "hall of fame", "responsible disclosure", "security contacts", "security.txt", "vulnerability", "bug bounty", "bug hunter", "bugcrowd", "hackerone", "intigriti", "synack", "yeswehack", "hackenproof", "cobalt", "zerocopter", "responsible reporting", "responsible vulnerability disclosure", "responsible vulnerability reporting", "security response", "security vulnerability bounty", "security vulnerability reward", "vulnerability reward program", "vulnerability rewards program", "vulnerability disclosure policy", "security vulnerability disclosure", "security vulnerability disclosure program", "vulnerability disclosure program", "responsible disclosure program", "vulnerability reporting program", "bug bounty program", "security bounty program", "security disclosure program", "security vulnerability disclosure policy", "security vulnerability reporting program", "security bug bounty program", "security vulnerability bug bounty program", "security vulnerability disclosure reward", "vulnerability disclosure reward", "security vulnerability disclosure bounty", "vulnerability disclosure bounty", "security vulnerability reward program", "security vulnerability rewards program", "vulnerability rewards", "security rewards program", "vulnerability bounty", "vulnerability program", "responsible disclosure bounty", "responsible vulnerability bounty", "responsible disclosure reward", "responsible vulnerability reward", "security vulnerability hall of fame", "security vulnerability swag", "vulnerability swag"]

# loop through the dorks in the input file
with open(input_file, "r") as f:
    for dork in f:
        dork = dork.strip()
        print(f"Processing {dork}")

        # search for the dork using Google search
        urls = search(dork)

        # loop through the URLs found in the search results
        for u in urls:
            try:
                # check if the URL is paying bounty for vulnerability reports
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
                response = requests.get(u, headers=headers, timeout=10)

                if any(keyword in response.text.lower() for keyword in keywords):
                    # extract the email address for vulnerability reports
                    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
                    email = re.search(email_regex, response.text)
                    if email:
                        # write the URL and email to the emails file
                        with open(emails_file, "a") as f1:
                            f1.write(f"{u}\t{email.group()}\n")
                    else:
                        # write the URL to the no_emails file
                        with open(no_emails_file, "a") as f2:
                            f2.write(f"{u}\n")
            except requests.exceptions.Timeout:
                # skip URLs that time out
                print(f"Timed out: {u}")
                continue
