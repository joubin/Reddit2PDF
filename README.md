#[Lets get some reading material for the flight](/post.php?post=OffLineReader.md)

I got married last weekend and this weekend I'm going to be on a 6 hour flight to Kauai, Hawaii 🌴🌴🌴

As much as I love my iPad, nothing can replace writing on the margins of white paper. My first plan was to write a crawler to get white papers off of university pages that I'd like to apply to for my graduate work. But given that I just got married, I found it to be in poor taste to spend a bunch of time programming. But I still needed reading material for the flight (no wifi) so I decided to write a small script to generate pdfs for me. 


Thanks to [/r/netsec](https://www.reddit.com/r/netsec) and [/r/programming](https://www.reddit.com/r/programming) for their amazing posts.

The code base is entirely in python. I wrote and executed this on both my Mac and Ubuntu server. The install script will install most of the required tools with the exception of [wkhtmltopdf](http://wkhtmltopdf.org/) which needs to be installed manually.

The main method simply get the top `N` posts from a selected sub and generates a pdf from it. 

Let me know what you think!


##Example:

### Output:
<pre>
02:48:47 - joubin@datahomejabbariio:[~/Documents/Git/Reddit2PDF]: python Main.py 
328 :: CVE-2015-3245 and CVE-2015-3245: local exploit that lets users change ...
41 :: Introducing KeychainEditor for iOS
0 :: Determining the Right CND Tool for a Job
46 :: IBM Mainframe (z/OS) Shellcode, Egghunters and Encoders (Exploit Dev).
47 :: Bypassing GMX Virus Scanning using Conflicting MIME Boundaries
22 :: Gaming Meets OSINT: Using Python to Help Solve Her Story
17 :: A tale of Pirpi, Scanbox & CVE-2015-3113
295 :: I wrote a detailed HowTo on "Privacy & Security Conscious Browsing" an...
144 :: Hacking Team: a zero-day market case study
182 :: Georgia Tech Releases No Cost Malware DNS Data Feed
23 :: RECON 2015 slides
16 :: Android Broadcast Security
284 :: OS X 10.10 DYLD_PRINT_TO_FILE Local Privilege Escalation Vulnerability
53 :: RECON 2015: Exploiting Out-of-Order-Execution
25 :: Bypassing AOL Mail Virus Scanning with Conflicting Content-Transfer-Enc...
31 :: How to fuzz a server with American Fuzzy Lop
561 :: MS15-078, Remote Code Execution in all versions of Windows. No patch f...
62 :: Collection of Hacking ezines
24 :: One Perfect Bug: Exploiting Type Confusion in Flash
3 :: x86 Exploitation 101: â€œHouse of Spiritâ€ â€“ Friendly stack overflow
233 :: The Public Comments on the Proposed Wassenaar Rule to Limit Export of ...
264 :: The Case of Insecure MongoDB Defaults and 600TB of Data
59 :: A gentle introduction to Berkeley packet filters for network traffic an...
267 :: RedStar OS Watermarking
231 :: OpenSSH keyboard-interactive authentication brute force vulnerability ...
0 :: Why You Don't Need 2 Factor Authentication
18 :: OWASP Application Security Verification Standard Project 3.0
674 :: Computer Systems Security | MIT OpenCourseWare
37 :: out with the old, in with the less - OpenBSD replacing sudo with doas
10 :: Frida: Putting the open back into closed software
14 :: Project Zero: Significant Flash exploit mitigations are live in v18.0.0...
</pre>

### Result:
![image](http://i.imgur.com/TwTpo1t.png)

2015-21-7




