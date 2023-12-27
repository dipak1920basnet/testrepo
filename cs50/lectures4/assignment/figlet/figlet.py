import sys
from pyfiglet import Figlet
import pyfiglet


def main():
    figlet = Figlet()
    # print(figlet.getFonts())
    try:
        if len(sys.argv) > 0:
            if sys.argv[1:] not in figlet.getFonts():
                print("Invalid usage")
                sys.exit()
            else:
                result = pyfiglet.figlet_format(get_input(), font=f"{sys.argv[1:]}")
        else:
            result = pyfiglet.figlet_format(get_input)
        print(f"{result}")
    except pyfiglet.FontNotFound as e:
        print("Invalid usage")
        sys.exit()


def get_input():
    return str(input("Input:"))
    
main()
