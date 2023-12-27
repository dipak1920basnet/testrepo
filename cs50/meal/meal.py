def main():
    get_time = input("> ")
    x = convert(get_time)
    if x.startswith("7"):
        print("breakfast time")
    elif x.startswith("12"):
        print("lunch time")
    elif x.startswith("18"):
        print("dinner time")
def convert(time):
    hours, minute = time.split(":")
    total_hours = int(hours) + int(minute)/60
    return str(total_hours)
if __name__ == "__main__":
    main()