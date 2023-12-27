import cowsay
# cowsay.cow('Hello World')
# print(cowsay.get_output_string('trex','Hello (extinct) World'))
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    