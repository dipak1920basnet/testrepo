l = []
while True:
    try:
        get = str(input())
        l.append(get)
    except EOFError:
        break
for i in l:
    print(i)
    

# try:
#     lines = []
#     while True:
#         line = input()
#         if line == "▬" or line == "♦":
#             break
#         lines.append(line)
# except EOFError:
#     pass

# text = '\n'.join(lines)
# uppercase_text = text.upper()
# print(uppercase_text)
