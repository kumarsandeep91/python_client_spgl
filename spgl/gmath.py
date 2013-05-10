'''
This file exports several functions for working with graphical gemoetry along with
the mathematical constants PI and E
'''
import math
import gtypes

PI = 3.14159265358979323846
'''
The mathematical constant pi, which is the ratio of the circumference of a circle to 
its diameter
'''

E = 2.71828182845904523536
'''
The mathematical constant e, which is the base of the natural logarithm
'''

def toDegrees(radians):
	'''
	Converts an angle from radians to degrees.
	
	@type radians: float
	@param radians: radians
	@rtype: float
	@return: degrees
	'''
	return radians * 180 / PI

def toRadians(degrees): 
	'''
	Converts an angle from degrees to radians.
	
	@type degrees: float
	@param degrees: degrees
	@rtype: float
	@return: radians
	'''
	return degrees * PI / 180

def sinDegrees(angle): 
	'''
	Returns the trigonometric sine of angle, which is expressed in degrees
	
	@type angle: float
	@param angle: degrees
	@rtype: float
	'''
	return math.sin(toRadians(angle))

def cosDegrees(angle): 
	'''
	Returns the trigonometric cosine of angle, which is expressed in degrees
	
	@type angle: float
	@param angle: degrees
	@rtype: float
	'''
	return math.cos(toRadians(angle))

def tanDegrees(angle):
	'''
	Returns the trigonometric tangent of angle, which is expressed in degrees
	
	@type angle: float
	@param angle: degrees
	@rtype: float
	'''
	return math.tan(toRadians(angle))

def vectorDistance(pt = None, x = None, y = None): 
	'''
	Computes the distance between the origin and the specified point.
	
	@type pt: GPoint
	@param pt: GPoint to compute distance to, will override x and y parameters
	@type x: float
	@param x: x value of point
	@type y: float
	@param y: y value of point
	@rtype: float
	'''
	if(pt != None):
		x = pt.getX()
		y = pt.getY()
	return math.sqrt(x * x + y * y)

def vectorAngle(pt = None, x = None, y = None): 
	'''
	Returns the angle in degrees from the origin to the specified point. This 
	functoin takes account of the fact that the graphics coordinate system is flipped
	in the y direction from the traditional Cartesian plane.
	
	@type pt: GPoint
	@param pt: GPoint to angle to, will override x and y parameters
	@type x: float
	@param x: x value of point
	@type y: float
	@param y: y value of point
	@rtype: float
	@return: degrees
	'''
	if(pt != None):
		x = pt.getX()
		y = pt.getY()
	if(x == 0 and y == 0): return 0
	return toDegrees(math.atan2(-y, x))

