# import msvcrt

# def main():
#     print("Press Ctrl + D to exit.")
    
#     while True:
#         char = msvcrt.getch()
#         if char == b'\x04':  # Ctrl + D
#             print("\nCtrl + D pressed. Exiting...")
#             break
#         else:
#             print(f"You pressed: {char.decode()}")

# if __name__ == "__main__":
#     main()







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
print("Press Ctrl + Z to exit.")

# while True:
#     try:
#         char = msvcrt.getch()
#         if char == b'\x1a':  # Ctrl + Z on Windows
#             print("\nCtrl + Z pressed. Exiting...")
#             break
#         get_order = input("Item:").title()
#         k.append(menu[get_order])
#     except KeyError:
#         continue
#     else:    
#         total = sum(k)
#         print(f"Total: ${total:.2f}")


# while True:
#     try:
#         get_order = input("Item:\n").title()
#         order = msvcrt.getch()
#         if order == b'\x04':
            
#             break
#         else:
#             k.append(menu[get_order])
#     except KeyError:
#         continue
#     else:    
#         l = 0
#         for i in k:
#             l += i
#         print(f"Total:${round(l,2)}")



while True:
    try:
        get_order = input("Item:\n").title()
        k.append(menu[get_order])
    except KeyError:
        continue
    except EOFError:
        break
    else:    
        l = 0
        for i in k:
            l += i
        print(f"Total:${round(l,2)}")


