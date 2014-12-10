import exceptions


class Dog:
    __secret = 2

def main():
    try:
        zeroDivision = Undefined/0
    except (NameError, ZeroDivisionError), e:
        print "You can't divide by zero!"
        print e
    else:
        print zeroDivision
    finally:
        print "This will always print regardless"
        

if __name__ == '__main__': main()