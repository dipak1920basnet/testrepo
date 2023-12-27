import msvcrt 
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    
k = []
while True:
    try:
        get_order = input("Item:").title()
        order = msvcrt.getch()
        if order == b'\x04':
            
            break
        else:
            k.append(menu[get_order])
    except KeyError:
        continue
    else:    
        l = 0
        for i in k:
            l += i
        print(f"Total:${round(l,2)}")

# char = msvcrt.getch()
#         if char == b'\x04':  # Ctrl + D
#             print("\nCtrl + D pressed. Exiting...")
#             break

