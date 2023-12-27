import re
email = input("Whats's your email?").strip()
# if re.search(r"^\w+@\w+\.edu$", email):
if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")  