from test import Person
class Man(Person):
    
    def __init__(self, name, age, gender):
        self.name, self.age = Person.info()
        self.gender = gender
        
    def info_man(self):
        print(self.name , self.age, self.gender)    
        
    
obj = Man("egor", 25, "Male")    
p = Person("moshe", 55)