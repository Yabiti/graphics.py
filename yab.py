from pyfiglet import Figlet
import sys

figlet = Figlet()
figlet.getFonts()

if len(sys.argv) == 0:
    print(figlet.renderText(s))
elif len(sys.argv) == 2:
    print(figlet.renderText(s))

else:
    sys.exit("Error")