__metaclass__ = type

class Animal:
    
    __hungry = "Yes"
    __name = "No Name"
    __owner = "No Owner"
        
    def __init__(self, **kvargs):
        self._attributes = kvargs
    
    def set_attributes(self, key, value):
        self._attributes[key] = value
        return
    
    def get_attributes(self,key):
        return self._attributes.get(key, None)
    
    def set_owner(self, newOwner):
        self.__owner = newOwner
        return
    
    def get_owner(self):
        return self.__owner
    
    def noise(self):
        print('errr')
        return
    
    def move(self):
        print('The animal moves forward')
        return
    
    def eat(self):
        print('Crunch, Crunch')
        return

class Dog(Animal):
    
    def __init__(self, **kvargs):
        super(Dog,self).__init__()
        self._attributes = kvargs
    
    def noise(self):
        print('Woof, Woof')
        Animal.noise(self)

class Cat(Animal):
    def __init__(self, **kvargs):
        super(Cat,self).__init__()
        self._attributes = kvargs
    
    def noise(self):
        print('Meow, Meow')
        return
    
    def noise2(self):
        print('Purr, Purr')
        return
    
class Dat(Dog, Cat):
    def __init__(self, **kvargs):
        super(Dat,self).__init__()
        self._attributes = kvargs
    
    def move(self):
        print('Chases its tail')
        return
    
    
    
def playWithAnimal(Animal):
    Animal.noise()
    Animal.eat()
    Animal.move()
    print(Animal.get_attributes('__name'))
    print(Animal.get_attributes('__owner'))
    Animal.set_attributes('clean', 'Yes')
    print(Animal.get_attributes('clean'))
    print("\n")
    

def main():
    jake = Dog(__name='Jake',__owner='Paul')
    sophie = Cat(__name='Sophie',__owner='Sue')
    playWithAnimal(sophie)
    playWithAnimal(jake)
    japhie = Dat(__name = 'Japhie', __owner='Sue')
    japhie.move()
    japhie.noise()
    japhie.noise2()
    print(japhie.get_attributes('__name'))
    print issubclass(Cat,Animal)
    print Cat.__bases__
    print sophie.__class__
    print sophie.__dict__
    
    
if __name__ == '__main__': main()
    