tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("Backslash (\\)")
print("Single-quote (\')")
print('Double-quote (\")')
print("ASCII bell (BEL):\a")
print("ASCII backspace (BS):\b")
print("ASCII formfeed (FF):\f")
print("ASCII linefeed (LF):\n")
print("ASCII carriage return (CR):\r")
print("ASCII horizontal tab (TAB):\t")
print("ASCII vertical tab (VT):\v")
print("Unicode 5929 (天):\u5929")
print("Unicode 00005172 (兲):\U00005172")
print("Octal 65 (5):\65")
print("Hex 41 (A):\x41")

print("Double-quote with %%r: %r" % "\"")
print("Double-quote with %%s: %s" % "\"")
print("Single-quote with %%r: %r" % "\'")
print("Single-quote with %%s: %s" % "\'")

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print("%s\r" % i, end = ' ')
