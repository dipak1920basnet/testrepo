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
l = 0
while True:
    try:
        get_input = input("Item:").title()
        l +=  menu[get_input]
        print(f"Total:{round(l,2)}")
    except EOFError:
        break
    except KeyError:
        break
    
