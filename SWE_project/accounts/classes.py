#https://www.w3schools.com/python/python_classes.asp
class Shop:
    #constructor
    def __init__(self, name, location):
        # Attributes
        self.name = name
        self.location = location

    # Getter
    def get_name(self):
        return self.name
        
    # Setter
    def set_name(self, name):
        self.name = name
        
p1 = Person("John", 36)

print(p1.name)
print(p1.age) 