class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(self.name , self.age)
        return self.name, self.age
        
    def walk(self, dist):
        print(self.name + " is walking " + str(dist) + "kilometers")
        
    