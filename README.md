# Web-Hacking-Tools
A repository of tools for security testing and ethical hacking.

## ParallelCurl
ParallelCurl is a simple Bash script that allows you to perform multiple curl requests in parallel, with a range of values for a specific parameter in each request. This tool is especially useful for penetration testers and bug bounty hunters who need to test web applications with a large number of parameter values.

With ParallelCurl, you can easily generate multiple curl requests with a specific parameter value replaced by a range of values, and run them in parallel. This can help you discover vulnerabilities in web applications and APIs more efficiently, as you can test a large number of parameter values in a shorter amount of time.

To use ParallelCurl, simply provide a curl command in a text file, and specify the target string to be replaced, the start and end values for the replacement range, and whether to use a proxy. ParallelCurl will then generate and execute multiple curl requests in parallel, with the specified parameter values.

## Features
1. Replaces a specific string with a range of values in a cURL command to generate parallel HTTP requests
2. Supports adding a proxy to all requests through command-line arguments or by adding it to the cURL command in the input file
3. Executes all requests in parallel using background jobs for faster testing
4. Provides real-time output for each request, including the response status code and body
5. Supports saving response data to separate output files for each request

## Installation
To use ParallelCurl, simply clone this repository to your local machine:
git clone https://github.com/thejulfikar/ParallelCurl.git

## Usage

1. Create a cURL command with the string 111111 where you want to insert a range of values
2. Save the cURL command to a file, such as input.txt
3. Run the parallelcurl.sh script with the desired start and end values for the range of values to be replaced in the cURL command
4. Optionally, add the --proxy option followed by the proxy IP and port to add a proxy to all requests

  
Sit back and let ParallelCurl do its job!

  
  

# Responsible Disclosure Scraper
This is a Python script that searches Google for websites that may have responsible disclosure programs or vulnerability rewards and extracts any associated email addresses.

## Requirements
Python 3.x
googlesearch module
requests module

## You can install the required modules using pip:
1. pip install googlesearch
2. pip install requests

## Usage
1. Clone the repository or download the script and dorks file.
2. Open the dorks.txt file and add any custom search queries that you want to use, one per line. 
3. By default, the script includes a list of common keywords for identifying responsible disclosure programs and vulnerability rewards.
4. Run the script using the command:

python responsible_disclosure_scraper.py

5. The script will search Google for each query in dorks.txt and extract any email addresses associated with responsible disclosure programs or vulnerability rewards. Emails will be saved to the emails.txt file and URLs without email addresses will be saved to the no_emails.txt file.

Note: The script may take some time to run depending on the number of search queries in dorks.txt and the number of results returned by Google.

## Disclaimer
This script is intended for educational and ethical use only. Do not use this script to identify or exploit vulnerabilities without permission from website owners. The author is not responsible for any damages or legal consequences caused by the misuse of this script.


  

# Author

* [Muhammd Julfikar Hyder](https://twitter.com/thejulfikar) (@thejulfikar)
