# From a list of URLs, extract only the domain names (e.g., 'python.org', 'github.com').
import re

urls = [
    "https://www.python.org",
    "http://github.com",
    "https://www.example.com/path/to/page",
    "ftp://ftp.example.com/file.txt"
]

domain_pattern = r"https?://(www\.)?([^/]+)"
domains = [re.search(domain_pattern, url).group(2) for url in urls if re.search(domain_pattern, url)]

print("Extracted domains:", domains)