import datetime

name = input("What's your name? ")
age = int(input("How old are you? "))
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

year = datetime.datetime.now().year
print("So, %s was born in %d, %s tall and %s heavy." % (
    name, year - age, height, weight))
print("So, %r was born in %r, %r tall and %r heavy." % (
    name, year - age, height, weight))
