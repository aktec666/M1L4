# class Figure():

#     def __init__(self):
#         pass

#     def perimetr(self):
#         pass

#     def draw(self):
#         pass
    

class Triangle():
    
    def __init__(self, a,b,c):
         self.a = a
         self.b = b
         self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

class Rectangle():
    
    def __init__(self, a,b):
         self.a = a
         self.b = b

    def perimetr(self):
        return (self.a + self.b) * 2
        
t = [Triangle(3, 4, 5),  Rectangle(10, 20)]
for x in t:
    print(x.perimetr())
