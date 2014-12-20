

class Animal:
    
    __hungry = "Yes"
    __name = "No Name"
    __owner = "No Owner"
        
    def __init__(self):
        pass
    
    
    def set_owner(self, newOwner):
        self.__owner = newOwner
        return
    
    def get_owner(self):
        return self.__owner
    
    def noise(self):
        print('errr')
        self.__hiddenmethod()
        return

    def __hiddenmethod(self):
        print("Hard to find")
        return



def main():
    dog = Animal()
    print dog.get_owner()
    dog.set_owner("Sue")
    print dog.get_owner()

    dog.noise()

if __name__ == '__main__': main()
    