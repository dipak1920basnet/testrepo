def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    k = []
    for i in range(10):
        k.append(str(i))
    if 2>len(s) or len(s)>6:
        return False
    if s[0] != str(s[0]) and s[1] != str(s[1]):
        return False
    
    i = 1
    for i in range(len(str(s[2:-1]))):
        i += 1
        # if s[i] == int(s[i]):
            # if s[i+1] == str(s[i+1]):
            #     return False
            # else:
            #     return True
        # k = s.find(int(s[i]))
        # if (s[i] in k)(s[i+1] not in k):
        if (s[i+2] in k):
            # j = i+1
            # for j in range(len(str(s[i+1:-1]))):
            #     if (s[j] not in k):
            #         return False
            return False
        elif (s[i+3] in k):
            return False
        else:
            return True

    return True
main()




'''

def check_string(s):
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i+1].isalpha():
            return "invalid"
    return "valid"

input_string = input("Enter a string: ")
result = check_string(input_string)
print(result)



'''