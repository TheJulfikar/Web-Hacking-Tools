# Web-Hacking-Tools
A repository of tools for security testing and ethical hacking.
ParallelCurl
ParallelCurl is a simple Bash script that allows you to perform multiple curl requests in parallel, with a range of values for a specific parameter in each request. This tool is especially useful for penetration testers and bug bounty hunters who need to test web applications with a large number of parameter values.

With ParallelCurl, you can easily generate multiple curl requests with a specific parameter value replaced by a range of values, and run them in parallel. This can help you discover vulnerabilities in web applications and APIs more efficiently, as you can test a large number of parameter values in a shorter amount of time.

To use ParallelCurl, simply provide a curl command in a text file, and specify the target string to be replaced, the start and end values for the replacement range, and whether to use a proxy. ParallelCurl will then generate and execute multiple curl requests in parallel, with the specified parameter values.

Installation
To use ParallelCurl, simply clone this repository to your local machine:

bash
Copy code
git clone https://github.com/<username>/ParallelCurl.git
Usage
Create a text file with your curl command, e.g. input.txt:

wasm
Copy code
curl https://example.com/api?param=111111 --data "data=hello"
Run the parallelcurl.sh script:

bash
Copy code
./parallelcurl.sh
Follow the prompts to specify the target string to be replaced, the start and end values for the replacement range, and whether to use a proxy.

Sit back and let ParallelCurl do its job!

License
ParallelCurl is released under the MIT License. Feel free to use, modify, and distribute this tool as you see fit.
