
# def addNumbers(numOne=1, numTwo=1):
#     return numOne + numTwo

def addNumbers(*args):
    finalValue = 0
    
    if args:
        for i in args:
            finalValue += i
        return finalValue
    else:
        return "Please provide numbers"

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


def main():
    print addNumbers(50,60)
    print addNumbers(1,2,3,4,5,6,7,8,9,10)
    createDict(Name='Jim', age=50, YearBorn=1964)
    print factorial(4)

    print addNumbers()

    print factorial(6)
    
def createDict(**kvargs):
    for i in kvargs:
        print i, kvargs[i]
    return


if __name__ == '__main__': main()
