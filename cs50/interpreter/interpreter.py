# x = int(input())
# y = input()
# z = int(input())
# if y == "+":
#     print(float(x+z))
# elif y == "-":
#     print(float(x-z))
# elif y == "*":
#     print(float(x*z))
# elif y == "/":
#     print(float(x/z))

k = input()
if "+" in k:
    x,z = k.split("+")
    print(float(int(x)+int(z)))
elif "*" in k:
    x,z = k.split("*")
    print(float(int(x)*int(z)))
elif "-" in k:
    x,z = k.split("-")
    print(float(int(x)-int(z)))
elif "/" in k:
    x,z = k.split("/")
    print(float(int(x)/int(z)))


