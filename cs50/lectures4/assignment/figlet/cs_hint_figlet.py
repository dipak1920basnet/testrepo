from pyfiglet import Figlet
import sys
figlet = Figlet()
# figlet.getFonts()
figlet.setFont(font = sys.argv[1:])
print(figlet.renderText("Dipak"))