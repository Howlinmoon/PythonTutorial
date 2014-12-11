import os

def retrieveFile():
    try:
        bestStudent = {}
        bestStudentStr = "The Best Students Ranked\n\n"
        
        f = open('studentgrades.txt')
        
    except(IOError), e:
        print "File not found",e
    else:
        for line in f:
            print "line: ",line
            name, grade = line.split()
            bestStudent[grade] = name
        f.close()
        
        for i in sorted(bestStudent.keys(), reverse=True):
            print (bestStudent[i] + 'scored a ' + i)
            bestStudentStr += bestStudent[i] + 'scored a ' + i + '\n'
        print "\n"
        
        print bestStudentStr 
        
        outToFile = open("studentrank.txt","w")
        outToFile.write(bestStudentStr)
        outToFile.close()
        
        print "Finished output"
        
    return


def directoryPlay():
    print os.listdir("/usr")
    
    print os.path.isdir("/usr/bin/python")
    print os.path.isfile("/usr/bin/python")

    dirList = os.listdir("/usr")
    
    for filename in dirList:
        if os.path.isdir("/usr/" + filename):
            print os.listdir("/usr/" + filename)
        else:
            continue
        

def main():
    retrieveFile()
    directoryPlay()
    
    

if __name__ == '__main__': main()