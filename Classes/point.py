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

p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)

print(p)
print(q)
print(mid)
print(mid.getX())
print(mid.getY())
print(p.distanceFromOrigin())
print(q.distanceFromOrigin())

print(p.distanceFromPoint(q))

print(p.reflect_x())

print(p.slope_from_origin())
print(q.slope_from_origin())
print(Point(4, 10).slope_from_origin())

print(p.slope_from_point(q))
print(q.slope_from_point(p))
print(p.get_line_to_point(q))
print(q.get_line_to_point(p))
print(Point(4, 11).get_line_to_point(Point(6, 15)))

print(p)
p.move(2, 8)
print(p)