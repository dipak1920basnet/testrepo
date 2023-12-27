import sys
# Check for error
if len(sys.argv) <2:
    sys.exit("Too many arguments")
"""
    # print("Too few arguments")
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    # print("Too many arguments")
    sys.exit("Too many arguments")
# Print name tags
print("Hello my name is ",sys.argv[1])
"""
for name in sys.argv:
    print(f"My name is {name}")


print() 

# SLicing sys.argv
for name in sys.argv[1:]:
    print(f"My name is {name}")