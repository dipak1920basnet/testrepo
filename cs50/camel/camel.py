get_input = input("camelCase: ")
for i in get_input:
    if i == i.upper():
        i = "_"+i.lower()
    print(i,end = "")
