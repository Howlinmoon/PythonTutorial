
listEx = [4,5,6]
stringEx = "Random String"

print 4 in listEx

print 2 in listEx

print "String" in stringEx
print "dummy" in stringEx


X = 1

while X <= 30:
    print X,
    X += 1

listCustNum = [0,1,2]
listCustName = ['Bob Smith', 'Helen Jones', 'Mark Summers']
listCustAge = [23,70,45]

for i in listCustNum:
    print "%s is %d" % (listCustName[i], listCustAge[i])


for i in listEx:
    print i

for i in range(1,31):
    print i,
print

print "only odd numbers between 1 and 30"

for oddNumbers in range(1,31):
    if (oddNumbers%2) == 0:
        continue
    elif oddNumbers == 25:
        break
    else:
        print oddNumbers,

