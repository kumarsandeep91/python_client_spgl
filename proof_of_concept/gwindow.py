import math
import gtypes
import gobjects
import platform

__COLOR_TABLE__ =  {}
__ID__ = -1

class GWindowData:
	def __init__(self, 
				 windowWidth=0, 
				 windowHeight=0,
				 visible=False,
				 windowTitle="",
				 windowColor="",
				 top=None):
		
		global __ID__
		self.windowWidth = windowWidth
		self.windowHeight = windowHeight
		self.windowTitle = windowTitle
		self.windowColor = windowColor
		self.visible = visible
		self.top = top
		self.ID = __ID__
		__ID__ = __ID__ - 1
		
	def __eq__(self, other):
		return self.windowWidth == other.windowWidth and \
			   self.windowHeight == other.windowHeight and \
			   self.visible == other.visible and \
			   self.windowTitle == other.windowTitle and \
			   self.windowColor == other.windowColor and \
			   self.top == other.top
	
	def __ne__(self, other):
		return not(self.__eq__(other))

		
class GWindow:

	DEFAULT_WIDTH = 500
	DEFAULT_HEIGHT = 500

	def __init__(self, gwd=None, width=None, height=None, visible=True):
		if(gwd != None):
			self.gwd = gwd
			return
		
		if(width == None): width=GWindow.DEFAULT_WIDTH
		if(height == None): height=GWindow.DEFAULT_HEIGHT
		self.__initGWindow(width, height, visible)
		
	def __initGWindow(self, width, height, visible):
		self.gwd = GWindowData(width, height, visible)
		self.gwd.top = gobjects.GCompound()
		
		platform.Platform().createGWindow(self, width, height, self.gwd.top)
		
		self.setColor("BLACK")
		self.setVisible(visible)
	
	def __eq__(self, other):
		return self.gwd == other.gwd
	
	def __ne__(self, other):
		return self.gwd != other.gwd
	
	def close(self):
		platform.Platform().close(self)
		platform.Platform().deleteGWindow(self)
	
	def requestFocus(self):
		# TODO pp.requestFocus(self)
		dummy = 1
	
	def clear(self):
		self.gwd.top.removeAll()
		# TODO pp.clear(self)
	
	def setVisible(self, flag):
		self.gwd.visible = flag
		# TODO pp.setVisible(self, flag)
	
	def isVisible(self):
		return self.gwd.visible
	
	def drawLine(self, p0=None, p1=None,
				 x0=None, y0=None, x1=None, y1=None):
		if(p0 != None and p1 != None):
			x0 = p0.getX()
			y0 = p0.getY()
			x1 = p1.getX()
			y1 = p1.getY()
		
		if(x0 == None or y0 == None or x1 == None or y1 == None): return
			
		line = GLine(x0, y0, x1, y1)
		line.setColor(self.gwd.color)
		self.draw(line)
				 
	def drawPolarLine(self, r, theta, p0=None, x0=None, y0=None):
		if(p0 != None):
			x0 = p0.getX()
			y0 = p0.getY()
		
		if(x0 == None or y0 == None): return None
		
		x1 = x0 + r * math.cos(math.radians(theta))
		y1 = y0 - r * math.sin(math.radians(theta))
		self.drawLine(x0=x0, y0=y0, x1=x1, y1=y1)
		return GPoint(x1, y1)

	def drawOval(self, bounds=None, 
				 x=None, y=None, width=None, height=None):
		if(bounds != None):
			x = bounds.getX()
			y = bounds.getY()
			width = bounds.getWidth()
			height = bounds.getHeight()
			
		if(x == None or y == None or width == None or height == None): return
		
		oval = GOval(x, y, width, height)
		oval.setColor(self.gwd.color)
		oval.setFilled(True)
		self.draw(oval)
				 
	def fillOval(self, bounds=None, 
				 x=None, y=None, width=None, height=None):
		if(bounds != None):
			x = bounds.getX()
			y = bounds.getY()
			width = bounds.getWidth()
			height = bounds.getHeight()
			
		if(x == None or y == None or width == None or height == None): return
		
		oval = GOval(x, y, width, height)
		oval.setColor(self.gwd.color)
		oval.setFilled(True)
		self.draw(oval)
					  
	def drawRect(self, bounds=None, 
				 x=None, y=None, width=None, height=None):
		if(bounds != None):
			x = bounds.getX()
			y = bounds.getY()
			width = bounds.getWidth()
			height = bounds.getHeight()
			
		if(x == None or y == None or width == None or height == None): return
		
		rect = GRect(x, y, width, height)
		rect.setColor(self.gwd.color)
		self.draw(rect)
	
	def fillRect(self, bounds=None, 
				 x=None, y=None, width=None, height=None):
		if(bounds != None):
			x = bounds.getX()
			y = bounds.getY()
			width = bounds.getWidth()
			height = bounds.getHeight()
			
		if(x == None or y == None or width == None or height == None): return
		
		rect = GRect(x, y, width, height)
		rect.setColor(self.gwd.color)
		rect.setFilled(True)
		self.draw(rect)
				 
	def setColor(self, color=None, rgb=None):
		if(color != None):
			rgb = convertColorToRGB(color)
		
		if(rgb == None): return
		
		self.gwd.color = convertRGBToColor(rgb)
	
	def getColor(self):
		return self.gwd.color
	
	def getWidth(self):
		return self.gwd.windowWidth
	
	def getHeight(self):
		return self.gwd.windowHeight
	
	def repaint(self):
		# TODO pp.repaint(self)
		dummy = 1
	
	def setWindowTitle(self, title):
		self.gwd.windowTitle = title
		# TODO pp.setWindowTitle(self, title)
	
	def getWinodwTitle(self):
		return gwd.windowtitle
	
	def draw(self, gobj, x=None, y=None):
		if(x != None and y != None):
			gobj.setLocation(x=x, y=y)
		# TODO pp.draw(self, gobj)
	
	def add(self, gobj, x=None, y=None):
		if(x != None and y != None):
			gobj.setLocation(x=x, y=y)
		self.gwd.top.add(gobj)
	
	def remove(self, gobj):
		self.gwd.top.remove(gobj)
	
	def addToRegion(self, region, ginteractor=None, glabel=None):
		# TODO
		dummy = 1
	
	def removeFromRegion(self, region, ginteractor=None, glabel=None):
		# TODO
		dummy = 1
	
	def getObjectAt(self, x, y):
		count = self.gwd.top.getElementCount()
		for i in range(count):
			gobj = self.gwd.top.getElement(i)
			if(gobj.contains(x=x, y=y)): return gobj
		
		return None
	
	def setRegionAlignment(self, region, align):
		# TODO
		dummy = 1
	

def convertColorToRGB(colorName):
	if(colorName == ""): return -1
	if(colorName[0] == "#"):
		colorName = "0x" + colorName[1:]
		return int(colorName, base = 16)
		
	name = canonicalColorName(colorName)
	if(len(__COLOR_TABLE__) == 0): initColorTable()
	if(not name in __COLOR_TABLE__):
		# TODO Raise Error
		return
		
	return __COLOR_TABLE__[name]

def convertRGBToColor(rgb):
	hexString = hex(rgb)
	return "#" + hexString[2:].upper()
	
def exitGraphics():
	# TODO pp.exitGraphics()
	# EXIT
	dummy = 1
				 
def initColorTable():
	__COLOR_TABLE__["black"] = 0x000000
	__COLOR_TABLE__["darkgray"] = 0x595959
	__COLOR_TABLE__["gray"] = 0x999999
	__COLOR_TABLE__["lightgray"] = 0xBFBFBF
	__COLOR_TABLE__["white"] = 0xFFFFFF
	__COLOR_TABLE__["red"] = 0xFF0000
	__COLOR_TABLE__["yellow"] = 0xFFFF00
	__COLOR_TABLE__["green"] = 0x00FF00
	__COLOR_TABLE__["cyan"] = 0x00FFFF
	__COLOR_TABLE__["blue"] = 0x0000FF
	__COLOR_TABLE__["magenta"] = 0xFF00FF
	__COLOR_TABLE__["orange"] = 0xFFC800
	__COLOR_TABLE__["pink"] = 0xFFAFAF

def canonicalColorName(str):
	result = ""
	for char in str:
		if(not char.isspace() and char != "_"): result += char.lower()
	return result
	
	