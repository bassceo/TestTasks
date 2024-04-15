from math import sqrt 

class Point:
    def __init__(self):
        self.x = None
        self.y = None
        
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        return [self.x, self.y]
    
    def set_coordinates(self,x, y):
        self.x = x
        self.y = y
    
    def distane_to(self,point):
        try:
            return sqrt( (point.x-self.x)**2 + (point.y-self.y)**2 )
        except:
            return 0


# p1 = Point(0,0)
# p2 = Point(5,5)

# print(p1.distane_to(p2))
# p2.set_coordinates(5,0)
# print(p1.distane_to(p2))