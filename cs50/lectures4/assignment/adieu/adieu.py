import inflect
import sys
p = inflect.engine()
li = []
# try:
#     while True:
#         try:
#             mylist = input("Name: ")
#             li.append(mylist)
#         except EOFError:
#             # if mylist == "" or mylist == "^D":
#                 break

#     print(f"Adieu, adieu, to{p.join(tuple(li))}")
# except EOFError:
#     sys.exit()
try:
    while True:
        try:
            get_name = input("Name: ")
            # if len(get_name) < 0:
            #     continue
        except EOFError:
            break
        # except pydantic_core._pydantic_core.ValidationError:
        #     continue
        else:
            li.append(get_name)
except KeyboardInterrupt:
    # sys.exit()
    pass
# except EOFError:
#     pass
# else:
#     li.append(get_name)
except Exception as e:
    # sys.exit()
    pass
# except ValidationError:
#     pass
print(f"Adieu, adieu, to {p.join(tuple(li))}")
