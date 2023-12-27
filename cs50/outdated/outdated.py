months_name = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    li = []
    try:
        get_input = input("month/day/year:")
        month , day, year = get_input.split("/")
        # print(f"{year}")
        day = int(day)
        year = int(year)
        if month.isdigit():
            month = int(month)
            if year <0 or day <0 or day >31 or month <0 or month >12:
                continue
        else:
            if month not in months_name and month.isalpha():
                print("Please type from January to December or simply you can just type from 1-12")
        # if year <0 or day <0 or day >31 or month <0 or month >12:
        #     continue
        # if month.isalpha():
        #     month = month.title()
        if month in months_name:
            month = months_name.index(month.title())+1
            value = [year,month,day]
        else:
             value = [year,month,day]

        # joint = "-".join(str(value))
        # li.append(joint)
        li.append(value)
        li.sort()
    except ValueError:
        print("In month/day/year: format please!!")
        continue
    except EOFError:
        break
    else:
        print(f"{li[0][0]}-{li[0][1]}-{li[0][2]}")
# print(li)
        