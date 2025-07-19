def  fun(a:int, b:int, *args,**kwargs):
    # if not args:
    #     return 0 
    d1 = kwargs
    extraSm=a-b -kwargs.get('n', 0)
    return extraSm
 
print(fun(b=5, a=2, n=3,m=5)) 


#Inheritance

class Animal:
    def sound(self):
        print("some generic sound")
 
class Dog(Animal):
    def bark(self):
        print("Woof Woof")
        
class Cat(Animal):
    def meow(self):
        print("Meowww")
        
        
        
c= Cat()
c.sound()        
c.meow()