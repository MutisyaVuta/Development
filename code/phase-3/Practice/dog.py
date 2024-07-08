class Dog:
    species = "Canis familiaris"
    def __init__(self,name, age):
        self.name = name
        self.age = age

    #Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def _speaks(self, sound):
        return f"{self.name} says {sound}"

