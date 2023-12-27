Amount_Due = 50
while True:
    print(f"Amount_Due:{Amount_Due}")
    x = int(input("Insert Coin: "))
    y = [25,10,5]
    if x not in y:
        pass
    else:
        Amount_Due = Amount_Due - x
        if Amount_Due <= 0 :
            print(f"Change Owed: {-Amount_Due}")
            break
        else:
            continue