import re
email = input("What's your email?").strip()
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^[a-zA-Z-0-9_\.]+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
    