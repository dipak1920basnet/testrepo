import re 
url = input("URL: ").strip()
# matches = re.search(f"^https?://(www\.)?twitter.com/(.+)$", url, re.IGNORECASE)

# if matches:= re.search(f"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
if matches:= re.search(f"^https?://(?:www\.)?twitter\.com/([a-z0-9_].+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
