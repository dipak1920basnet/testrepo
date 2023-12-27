vowels = ["a","e","i","o","u"]
get_name = str(input("Input:"))
# li = ""
# for i in range(len(get_name)):
#     for j in range(len(vowels)):
#         if get_name[i] != vowels[j]:
#             li += get_name[i] 
            
# print(li)

hello = list(get_name)
# print(hello)
for i in range(len(hello)):
    for j in range(len(vowels)):
        if vowels[j] in hello:
            hello.remove(vowels[j])
# print(str(hello))
for i in hello:
    print(i,end="")