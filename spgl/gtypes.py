'''
This module defines classes for representing points, dimensions, and rectangles.
'''
import platform

class GPoint:
	'''
	This class contains real-valued x and y fields. It is used to represent a 
	location on the graphics plane.
	'''
	def __init__(self, x=0.0, y=0.0):
		'''
		Initializes a GPoint object with the specified x and y coordinates. If the
		coordinates are not supplied the default values of these fields are 0.0
		
		@type x: float
		@param x: x coordinate
		@type y: float
		@param y: y coordinate
		@rtype: void
		'''
		self.x = x
		self.y = y
	
	def __eq__(self, other):
		'''
		Defines equality for GPoints, namely the x and y values are identical
		for the compared objects.
		
		@type other: GPoint
		@param other: object to be compared
		@rtype: boolean
		'''
		if(other == None): return False
		return self.x == other.x and self.y == other.y
	
	def __ne__(self, other):
		'''
		Defines non-equality for GPoints, negation of equality.
		
		@type other: GPoint
		@param other: object to be compared
		@rtype: boolean
		'''
		return not(self.__eq__(other))
	
	def getX(self):
		'''
		Returns the x component of the point.
		
		@rtype: float
		'''
		return self.x
		
	def getY(self):
		'''
		Returns the y component of the point.
		
		@rtype: float
		'''
		return self.y
	
	def toString(self):
		'''
		Converts the GPoint to a string in the form 
		M{"(x, y)"}
		
		@rtype: string
		'''
		return "(" + str(self.x) + ", " + str(self.y) + ")"
		

class GDimension:
	'''
	This class contains real-alued witdth and height fields. It is used to indicate
	the size of a graphical system
	'''
	def __init__(self, width=0.0, height=0.0):
		'''
		Initializes a GDimension object with the specified width and height values. 
		If the values are not supplied the defaul values of these fields are 0.0
		
		@type width: float
		@param width: width dimension
		@type height: float
		@param height: height dimension
		@rtype: void
		'''
		self.width = width
		self.height = height
		
	def __eq__(self, other):
		'''
		Defines equality for GDimensions, namely the height and width values are 
		identical for the compared objects
		
		@type other: GDimension
		@param other: object to be compared
		@rtype: boolean
		'''
		if(other == None): return False
		return self.width == other.width and self.height == other.height
		
	def __ne__(self, other):
		'''
		Defines inequality for GDimensions, negation of equality
		
		@type other: GDimension
		@param other: object to be compared
		@rtype: boolean
		'''
		return not(self.__eq__(other))
		
	def getWidth(self):
		'''
		Returns the width component of the GDimension.
		
		@rtype: float
		'''
		return self.width
	
	def getHeight(self):
		'''
		Returns the height component of the GDimension.
		
		@rtype: float
		'''
		return self.height
	
	def toString(self):
		'''
		Converts the GDimension to a string in the form 
		M{"(width, height)"}
		
		@rtype: string
		'''
		return "(" + str(width) + ", " + str(height) + ")"
	
	
class GRectangle:
	'''
	This type contains real-valued x, y, width, and height fields. It is used to
	represent the bounding box of a graphical object
	'''
	def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0):
		'''
		Initializes a GRectangle object with the specified fields. If these 
		parameters are not supplied hte default values are set to 0.0
		
		@type x: float
		@param x: x coordinate of upper left corner
		@type y: float
		@param y: y coordinate of upper left corner
		@type width: float
		@param width: width of rectangle
		@type height: float
		@param height: height of rectangle
		@rtype: void
		'''
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		
	def __eq__(self, other):
		'''
		Defines equality for GRectangles, namely the x, y, height, and width values 
		are	identical for the compared objects
		
		@type other: GRectangle
		@param other: object to be compared
		@rtype: boolean
		'''
		if(other == None): return False
		return self.x == other.x and \
			self.y == other.y and \
			self.width == other.width and \
			self.height == other.height
		
	def __ne__(self, other):
		'''
		Defines inequality for GRectangles, negation of equality
		
		@type other: GRectangle
		@param other: object to be compared
		@rtype: boolean
		'''
		return not(self.__eq__(other))
	
	def getX(self):
		'''
		Returns the x component of the upper left corner.
		
		@rtype: float
		'''
		return self.x
		
	def getY(self):
		'''
		Returns the x component of the upper left corner.
		
		@rtype: float
		'''
		return self.y	
			
	def getWidth(self):
		'''
		Returns the width component of the GRectangle.
		
		@rtype: float
		'''
		return self.width
	
	def getHeight(self):
		'''
		Returns the width component of the GRectangle.
		
		@rtype: float
		'''
		return self.height
		
	def isEmpty(self):
		'''
		Returns if the rectangle is empty.
		
		@rtype: boolean
		'''
		return width <= 0 or height <= 0
	
	def contains(self, pt=None, x=None, y=None):
		'''
		Returns true if the rectangle contains the given point, which may be 
		specified either as a GPoint or distinct coordinates
		
		@type pt: GPoint
		@param pt: GPoint to check, will override x and y
		@type x: float
		@param x: x coordinate of point to check
		@type y: float
		@param y: y coordinate of point to check
		@rtype: boolean
		'''
		if(pt != None or (x != None and y != None)):
			if(pt != None):
				x = pt.getX()
				y = pt.getY()
			return x >= self.x and \
				y >= self.y and \
				x < self.x + self.width and \
				y < self.y + self.height
		return False
	
	def toString(self):
		'''
		Converts the GRectangle to a string in the form 
		M{"(x, y, width, height)"}
		
		@rtype: string
		'''
		return "(" + str(x) + ", " + str(y) \
				+ ", " + str(width) + ", " + str(height) + ")"
		
if __name__ == '__main__':
	print
	print "Testing gtypes.py"
	print 
	print "--------------------------------------------------"
	print 
	
	print "Create GPoint default values"
	gp1 = GPoint()
	x = gp1.getX()
	y = gp1.getY()
	tostring = gp1.toString()
	gp2 = GPoint()
	eq = (gp1 == gp2)
	ne = (gp1 != gp2)
	if(x != 0.0 or y != 0.0 or tostring != "(0.0, 0.0)" or eq != True or ne != False):
		print "FAILED"
	print "PASSED"
	print
	
	print "Create GPoint non-default values"
	gp1 = GPoint(5, -2.5)
	x = gp1.getX()
	y = gp1.getY()
	tostring = gp1.toString()
	gp2 = GPoint(5, -2.5)
	eq = (gp1 == gp2)
	ne = (gp1 != gp2)
	if(x != 5 or y != -2.5 or tostring != "(5, -2.5)" or eq != True or ne != False):
		print "FAILED"
	print "PASSED"
	print
	