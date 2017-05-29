def append_number(end, step):
#    i = 0
    numbers = []

#    while i < end:
    for i in range(0,end,step):
        print("At the top i is %d" % i)
        numbers.append(i)

#        i = i + step
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    return numbers


print("The numbers: ")

for num in append_number(10, 2):
    print(num)
