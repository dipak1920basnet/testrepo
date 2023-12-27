def main():
    # name = get_name()
    # house = get_house()
    # name, house = get_student()
    student = get_student()
    # print(f"{name} from {house}")
    print(f"{student[0]} from {studnet[1]}")
# def get_name():
#     return input("Name: ")
# def get_house():
#     return input("House: ")
def get_student():
    name=input("Name: ")
    house=input("House: ")
    return (name, house)

if __name__ =="__main__":
    main()
