from __builtin__ import True
import math
import pygame

dictEx = ({"Age":50, "Height":"5' 10", "Weight":210})

print dictEx

print dictEx.get("Height")

print dictEx.items()

print dictEx.keys()

print dictEx.values()

dictEx.pop("Height")

print dictEx

strName = "Bob"
floatAge = 35.4
charSex = "M"
intKids = 2
boolMarried = True

print "My name is", strName


print "%s is %.1f years old" % (strName, floatAge)
print "Sex: %c" % (charSex)
print "He has %d kids and said it\'s %s he is married'" % (intKids, boolMarried)

print '%.15f' % (math.pi)
print '%20.15f' % (math.pi)

#precisionPi = int(raw_input("How precise should pi be: "))
precisionPi = 25
print "Pi = %.*f" % (precisionPi, math.pi)


bigString = "Here is a long string I will be messing with"

print bigString[1:20:2]

print bigString.find('string')
print bigString.count('e')
print bigString.count('e',4)
print bigString.count('e',4,20)

copyStr = tuple(bigString)
print copyStr

print ''.join(copyStr)
print 'X'.join(copyStr)
print bigString.lower()
print bigString.upper()

print bigString.replace("long","small")

randomWhiteSpace = "       leading and trailing white space    "
print randomWhiteSpace
print randomWhiteSpace.strip()
print "pygame version:",pygame.ver

