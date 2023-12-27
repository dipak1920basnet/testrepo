import random

count = 0
point = 0
def main():
    
    while True:
        try:
            k = get_level()
            if k == 1:

                for i in range(10):
                    generate_integer(9)
            elif k == 2:
                for i in range(10):
                    generate_integer(20)
            elif k == 3:
                for i in range(10):
                    generate_integer(30)
        except ValueError:
            continue
        else:
            break



def get_level():
    level = int(input("Level:"))
    return level
    
def generate_integer(level):
    x = random.randint(0,level)
    y = random.randint(0, level)
    result = x + y
    while True:
        global count
        count +=1
        try:
            # global count
            # count +=1
            get_result = int(input(f"{x} + {y} = "))
            if count == 3:
                print(f"{x} + {y} = {result}")
                break
        except ValueError:
            continue
        else:
            if get_result == result:
                global point
                point += 1
                break
            else:
                print("EEE")
                continue


if __name__ == "__main__":
    main()