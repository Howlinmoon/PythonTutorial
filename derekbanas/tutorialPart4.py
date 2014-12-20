from _elementtree import Comment

#yourAge = int(raw_input("How old are you: "))
yourAge = 54
if (yourAge > 0) and (yourAge < 120):
    if (yourAge == 50):
        print "Same as me!"
    elif (yourAge > 50):
        print "Older than me"
    else:
        print "Younger than me"
else:
    print "Don't lie about your age"


""" Comment
more Comment
still more Comment
"""
x , y = 1 , 0

a = 'y is less than x' if (y < x) else 'x is less then or equal to y'
print a

