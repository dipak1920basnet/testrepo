while True:
    get_fraction = input("Fraction:")
    try:
        first , last = get_fraction.split("/")
        if int(first) > int(last):
            continue
        else:
            fuel_percentages=(int(first)/int(last))*100
    except ValueError or ZeroDivisionError:
        continue
    else:
        if fuel_percentages <0:
            pass
        elif fuel_percentages <= 1:
            print("E")
            break
        elif fuel_percentages >=99:
            print("F")
            break
        else:
            print(f"{int(fuel_percentages)}%")
            break


