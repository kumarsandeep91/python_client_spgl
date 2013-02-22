import platform

# TODO: Ostream operator << and hashCode method for all 3?

class GPoint:
	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __ne__(self, other):
		return not(self.__eq__(other))
	
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
	
	def toString(self):
		# TODO cna't concat
		return "(" + self.x + ", " + self.y + ")"
		

class GDimension:
	def __init__(self, width=0.0, height=0.0):
		self.width = width
		self.height = height
		
	def __eq__(self, other):
		return self.width == other.width and self.height == other.height
		
	def __ne__(self, other):
		return not(self.__eq__(other))
		
	def getWidth(self):
		return self.width
	
	def getHeight(self):
		return self.height
	
	def toString(self):
		# TODO cna't concat
		return "(" + width + ", " + height + ")"
	
	
class GRectangle:
	def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		
	def __eq__(self, other):
		return self.x == other.x and \
			self.y == other.y and \
			self.width == other.width and \
			self.height == other.height
		
	def __ne__(self, other):
		return not(self.__eq__(other))
	
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y	
			
	def getWidth(self):
		return self.width
	
	def getHeight(self):
		return self.height
		
	def isEmpty(self):
		return width <= 0 or height <= 0
	
	def contains(self, pt=None, x=None, y=None):
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
		# TODO cnat concat
		return "(" + x + ", " + y + ", " + width + ", " + height + ")"
		
