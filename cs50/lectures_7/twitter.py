url = input("URL: ").strip()
# print(url)
username = url.removeprefix("https://twitter.com/")
print(f"Username:{username}")
