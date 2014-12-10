from Cython.Compiler.Nodes import BreakStatNode
normalString = "text to be reversed"
reversedString = normalString[::-1]
print "The string now reversed: ",reversedString


for number in range(101):
        print number
        if number % 15 == 0:
            print "number",number,"is divisible by both - fizz buzz"
        elif number % 3 == 0:
            print "number",number,"is divisible by 3 - fizz"
        elif number % 5 == 0:
            print "number",number,"is divisible by 5 - buzz"
            


## drop 50th - Breaks - drop at 25th,  not break - drop from 75th,  keep using split

