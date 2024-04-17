import emoji
import sys

user = input("input: ")
output = " "

user = user.convert(emoji)

if len(sys.argv) == 2:
    print("Hello", sys.argv[1])
else:
    user.replace("", emoji.emojize)