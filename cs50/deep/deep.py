get_input = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
if get_input.lower() == "42" or get_input.lower() == "forty-two" or get_input.lower() == "forty two":
    print("yes")
elif get_input.lower().startswith("forty") and get_input.lower().endswith("two"):
    print("yes")
else:
    print("no")