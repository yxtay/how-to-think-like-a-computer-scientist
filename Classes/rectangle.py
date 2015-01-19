from test import *

class Point(object):

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return "(x = %d, y = %d)" % (self.x, self.y)

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)
 
    def reflect_x(self):
        return Point(-self.x, self.y)
        
    def slope_from_origin(self):
        return float(self.y) / self.x
        
    def slope_from_point(self, other):
        return float(self.y - other.y) / (self.x - other.x)
        
    def get_line_to_point(self, other):
        slope = self.slope_from_point(other)
        intercept = self.y - self.x * slope 
        return (slope, intercept)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

        
class Rectangle(object):

    def __init__(self, blPoint, initW, initH):
        self.bottomleft = blPoint
        self.width = initW
        self.height = initH
        
    def __str__(self):
        return "rectangle at %s, with width = %d, height = %d" \
            % (self.bottomleft, self.width, self.height)
            
    def getWidth(self):
        return self.width
        
    def getHeight(self):
        return self.height
        
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.width + self.height)

    def transpose(self):
        self.width, self.height = self.height, self.width
    
    def contains(self, point):
        x1 = self.bottomleft.getX()
        y1 = self.bottomleft.getY()
        x2 = x1 + self.width
        y2 = y1 + self.height
        return x1 <= point.getX() and point.getX() < x2 \
            and y1 <= point.getY() and point.getY() < y2
        
    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
        
    def getCorners(self):
        blPoint = self.bottomleft
        tlPoint = Point(blPoint.getX(), blPoint.getY() + self.height)
        brPoint = Point(blPoint.getX() + self.width, blPoint.getY())
        trPoint = Point(brPoint.getX(), tlPoint.getY())
        return [blPoint, tlPoint, trPoint, brPoint]
        
    def overlaps(self, other):
        return any([self.contains(point) for point in other.getCorners()]) \
            or any([other.contains(point) for point in self.getCorners()])
        
        
r = Rectangle(Point(4, 5), 6, 5)
print(r)
print(r.getWidth())
print(r.getHeight())

r = Rectangle(Point(0, 0), 10, 5)
print(r.area())
print(r.perimeter())

print(r.getWidth())
print(r.getHeight())
r.transpose()
print(r.getWidth())
print(r.getHeight())

r = Rectangle(Point(0, 0), 10, 5)
print(r.contains(Point(0, 0)), True)
print(r.contains(Point(3, 3)), True)
print(r.contains(Point(3, 7)), False)
print(r.contains(Point(3, 5)), False)
print(r.contains(Point(3, 4.99999)), True)
print(r.contains(Point(-3, -3)), False)

print(r.diagonal())

r1 = Rectangle(Point(4, 5), 6, 5)
r2 = Rectangle(Point(0, 0), 10, 5)
for p in r1.getCorners():
    print(p)
for p in r2.getCorners():
    print(p)
    
print(r1.overlaps(r2))