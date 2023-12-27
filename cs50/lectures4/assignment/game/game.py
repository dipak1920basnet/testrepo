import random as r
k = 0
level = 0
attempt = 0
def game():
    get_level = int(input("press 1 to 100 to select the level:"))
    return get_level
while True:
    try:
        level = game()
        k = r.randint(1,level)
        # print(k)
    except ValueError:
        print("Please enter from 1 to 100")
        continue
    else:
        if 100 < level <= 0:
            print(" Enter number from 1 to 100")
            continue
        else:
            while True:
                attempt += 1
                try:
                    guess_number = int(input("Guess Number: "))
                # if gess
                except ValueError:
                    continue
                else:
                    if guess_number == k:
                        print("Just right")
                        break
                    elif guess_number < k:
                        print("The nnumber is too low")
                        continue
                    elif guess_number > k:
                        print("The number is too high")    
                        continue    
    break
