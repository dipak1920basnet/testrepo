import re 
email = input("What's your email?").strip()

# if re.search(".*@.*",email):
# if re.search(".*@.+", email) and email.endswith(".edu"):
# if re.search(".+@.+", email):
# if re.search(r".+@.+\.edu", email):
# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^.+@.+\.edu$", email):
# if re.match(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$",email):
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
    print("Valid")
else:
    print("InValid")
    