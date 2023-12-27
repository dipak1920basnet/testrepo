import re 
url = input("URL:").strip()
# username= re.sub(r"^(http|https)://twitter\.com","",url)
username= re.sub(r"^https?://(www\.)?twitter\.com","",url)
print(f"Username:{username}")