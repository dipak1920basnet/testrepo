def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # for i in range(2, len(s[2:-1])):
    #     if s[i].isdigit() and s[i+1:-1].isdigit():
    #         return True
    #     else:
    #         return False

    if 2>len(s)or len(s)>6:
        return False
    
    if s[0] != str(s[0]) and s[1] != str(s[1]):
        return False
    
    # for i in range(2, len(s[2:-1])):
    #     if s[i].isdigit() and s[i+1:-1].isdigit():
    #         return True
    for i in range(2, len(s[2:])):
        if s[i].isdigit() and s[i:].isdigit():
            return True
        

    # if s[:2] !=s[:2].isalpha():
    #     return False
    if s[2:].isdigit(): 
        return True
    elif s[2:-1].isalpha():
        return True
    else:
        return False
    # for i in range(2, len(s[2:-1])):
    #     if s[i].isdigit():
    #         if s[i:-1].isdigit():
    #             return True
    #         else:
    #             return False
main()