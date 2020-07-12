import sys

print('\n'.join(sys.path))

Names = ['Pete Davis','Richard Dunn','Jessica Rabbit','Mike Miers']
print(Names)

for x in Names:
    print(x)

dict = {'jeff':37,'pete':54,'amy':54}

for x in dict:
    print(x + ' ' + str(dict[x]))
