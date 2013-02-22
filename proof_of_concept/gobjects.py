import gtypes
import gwindow
import platform

__ID__ = 0

class GObject:
	def __init__(self):
		global __ID__
		self.x = 0.0
		self.y = 0.0
		self.color = ""
		self.lineWidth = 1.0
		self.transformed = False
		self.visible = True
		self.parent = None
		self.ID = __ID__
		__ID__ = __ID__ + 1
	
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getLocation(self):
		return GPoint(self.x, self.y)
		
	def setLocation(self, pt=None, x=None, y=None):
		if(pt != None):
			x = pt.getX()
			y = pt.getY()
			
		if(x == None or y == None): return
		
		self.x = x
		self.y = y
		# HERE
		platform.Platform().setLocation(self, x, y)
		# TODO pp.setLocation(self, x, y)
		
	def move(self, dx, dy):
		self.setLocation(x=self.x + dx, y=self.y + dy)
		
	def getWidth(self):
		bounds = self.getBounds()
		if (bounds != None): return bounds.getWidth()
		return None
		
	def getHeight(self):
		bounds = self.getBounds()
		if (bounds != None): return bounds.getHeight()
		return None
		
	def getSize(self):
		bounds = self.getBounds()
		if(bounds != None): return GDimension(bounds.getWidth(), bounds.getHeight())
		return None
		
	def getBounds(self):
		return None
		
	def setLineWidth(self, lineWidth):
		self.lineWidth = lineWidth
		# TODO pp.setLineWidth(self, lineWidth)
		
	def getLineWidth(self):
		return self.lineWidth
		
	def setColor(self, color=None, rgb=None):
		if(color != None): 
			rgb = gwindow.convertColorToRGB(color)
			
		if(rgb == None): return
		
		self.color = gwindow.convertRGBToColor(rgb)
		# TODO pp.setColor(self, self.color)
		
	def getColor(self):
		return self.color
		
	def scale(self, sf=None, sx=None, sy=None):
		if(sf != None):
			sx = sf
			sy = sf
			
		if(sx == None or sy == None): return
		
		self.transformed = True
		# TODO pp.scale(self, sx, sy)
		
	def rotate(self, theta):
		self.transformed = True
		# TODO pp.rotate(self, sx, sy)
		
	def setVisible(self, flag):
		self.visible = flag
		# TODO pp.setVisible(self, flag)
		
	def isVisible(self):
		return self.visible
		
	def sendForward(self):
		parent = self.getParent()
		if(parent != None): parent.sendForward(self)
		
	def sendToFront(self):
		parent = self.getParent()
		if(parent != None): parent.sendToFront(self)
		
	def sendBackward(self):
		parent = self.getParent()
		if(parent != None): parent.sendBackward(self)
		
	def sendToBack(self):
		parent = self.getParent()
		if(parent != None): parent.sendToBack(self)
		
	def contains(self, pt=None, x=None, y=None):
		if(pt != None):
			x = pt.getX()
			y = pt.getY()
			
		if(x == None or y == None): return False
		
		if(self.transformed):
			return False # TODO pp.contains(self, x, y)
			
		bounds = self.getBounds()
		if(bounds == None): return False
		return bounds.contains(x=x, y=y)
		
	def getType(self):
		return None
	
	def toString(self):
		return None
		
	def getParent(self):
		return self.parent
		
	#TODO    const GObject & operator=(const GObject & src) { return *this; }
	#TODO GObject(const GObject & src) { }
	
class GRect(GObject):
	def __init__(self, width, height, x=None, y=None):
		GObject.__init__(self)
		self.create(width, height)
		if(x != None and y != None):
			self.setLocation(x=x, y=y)

	def create(self, width, height):
		self.x = 0.0
		self.y = 0.0
		self.width = width
		self.height = height
		self.fillFlag = False
		self.fillColor = ""
		# HERE
		platform.Platform().createGRect(self, width, height)
		# TODO pp.createGRect(self, width, height)
			
	def setSize(self, size=None, width=None, height=None):
		if(size != None):
			width = size.getWidth()
			height = size.getHeight()
			
		if(width == None or height == None): return
		
		if(transformed): 
			# TODO throw error?
			return
			
		self.width = width
		self.height = height
		# TODO pp.setSize(self, width, height)
		
	def setBounds(self, bounds=None, x=None, y=None, width=None, height=None):
		if(bounds != None):
			x = bounds.getX()
			y = bounds.getY()
			width = bounds.getWidth()
			height = bounds.getHeight()
			
		if(x == None or y == None or width == None or height == None): return
		
		self.setLocation(x=x, y=y)
		self.setSize(width=width, height=height)
		
	def getBounds(self):
		if(transformed): return None # TODO pp.getBounds(self)
		return GRectangle(self.x, self.y, self.width, self.height)
		
	def setFilled(self, flag):
		self.fillFlag = flag
		# HERE
		platform.Platform().setFilled(self, flag)
		# TODO pp.setFilled(self, flag)
		
	def isFilled(self):
		return self.fillFlag
		
	def setFillColor(self, color="", rgb=None):
		self.fillColor = color
		if(color != ""):
			rgb = gwindow.convertColorToRGB(color)
			
		if(rgb == None): return
		
		color = gwindow.convertRGBToColor(rgb)
		# TODO pp.setFillColor(self, color)
		
	def getFillColor(self):
		return self.fillColor
		
	def getType(self):
		return "GRect"
		
	def toString(self):
		# TODO cna't concat
		return "GRect(" + self.x + ", " + self.y + ", " + \
				self.width + ", " + self.height + ")"
				
	# TODO GRect::GRect() {
	#	 /* Called only by the GRoundRect and G3DRect subclasses */
	#}
	
class GCompound(GObject):
	def __init__(self):
		GObject.__init__(self)
		self.contents = []
		# HERE
		platform.Platform().createGCompound(self)
		# TODO pp.createGCompound(self)
		
	def add(self, gobj, x=None, y=None):
		if(x != None and y != None):
			gobj.setLocation(x=x, y=y)
			
		# HERE
		platform.Platform().add(self, gobj)
		# TODO pp.add(self, gobj)
		self.contents.append(gobj)
		gobj.parent = self
		
	def remove(self, gobj):
		index = self.findGObject(gobj)
		if(index != -1): self.removeAt(index)
		
	def removeAll(self):
		while(len(self.contents) > 0):
			self.removeAt(0)
			
	def getElementCount(self):
		return len(self.contents)
		
	def getElement(self, index):
		return self.contents[index]
		
	def getBounds(self):
		if(self.transformed): return None # TODO pp.getBounds(self)
		xMin = sys.float_info.max
		yMin = sys.float_info.max
		xMax = sys.float_info.min
		yMax = sys.float_info.min
		for i in range(len(self.contents)):
			bounds = self.contents[i].getBounds()
			xMin = min(xMin, bounds.getX())
			yMin = min(yMin, bounds.getY())
			xMax = max(xMax, bounds.getX())
			yMax = max(yMax, bounds.getY())
				
		return GRectangle(xMin, yMin, xMax - xMin, yMax - yMin)
	
	def contains(self, x, y):
		if(self.transformed): return None # TODO pp.contains(self, x, y)
		for i in range(len(self.contents)):
			if(self.contents[i].contains(x, y)): return True
		return False
		
	def getType(self):
		return "GCompound"
		
	def toString(self):
		return "GCompound(...)"
		
	def sendForward(self, gobj):
		index = self.findGObject(gobj)
		if(index == -1): return;
		if(index != len(self.contents)-1):
			self.contents.pop(index)
			self.contents.insert(index + 1, gobj)
			# TODO pp.sendForward(gobj)
		
	def sendToFront(self, gobj):
		index = self.findGObject(gobj)
		if(index == -1): return;
		if(index != len(self.contents)-1):
			self.contents.pop(index)
			self.contents.append(gobj)
			# TODO pp.sendToFront(gobj)
		
	def sendBackward(self, gobj):
		index = self.findGObject(gobj)
		if(index == -1): return;
		if(index != 0):
			self.contents.pop(index)
			self.contents.insert(index - 1, gobj)
			# TODO pp.sendBackward(gobj)
		
	def sendToBack(self, gobj):
		index = self.findGObject(gobj)
		if(index == -1): return;
		if(index != 0):
			self.contents.pop(index)
			self.contents.insert(0, gobj)
			# TODO pp.sendToBack(gobj)
	
	def findGObject(self, gobj):
		n = len(self.contents)
		for i in range(n):
			if(self.contents[i] == gobj): return i # TODO how to implement comparison?
		return -1
		
	def removeAt(self, index):
		gobj = self.contents[index]
		self.contents.pop(index)
		# HERE
		platform.Platform().remove(gobj)
		# TODO pp.remove(gobj)
		gobj.parent = None
'''
/*
 * Class: GLine
 * ------------
 * This graphical object subclass represents a line segment.  For
 * example, the following code adds lines that mark the diagonals
 * of the graphics window:
 *
 *<pre>
 *    int main() {
 *       GWindow gw;
 *       cout << "This program draws the diagonals on the window." << endl;
 *       gw.add(new GLine(0, 0, gw.getWidth(), gw.getHeight()));
 *       gw.add(new GLine(0, gw.getHeight(), gw.getWidth(), 0));
 *       return 0;
 *    }
 *</pre>
 */

class GLine : public GObject {

public:

/*
 * Constructor: GLine
 * Usage: GLine *gline = new GLine(x0, y0, x1, y1);
 * ------------------------------------------------
 * Constructs a line segment from its endpoints.  The point
 * (<code>x0</code>,&nbsp;<code>y0</code>) defines the start of the
 * line and the point (<code>x1</code>,&nbsp;<code>y1</code>) defines
 * the end.
 */

   GLine(double x0, double y0, double x1, double y1);

/*
 * Method: setStartPoint
 * Usage: line->setStartPoint(x, y);
 * ---------------------------------
 * Sets the initial point in the line to (<code>x</code>,&nbsp;<code>y</code>),
 * leaving the end point unchanged.  This method is therefore different from
 * <code>setLocation</code>, which moves both components of the line segment.
 */

   void setStartPoint(double x, double y);

/*
 * Method: getStartPoint
 * Usage: GPoint pt = line->getStartPoint();
 * -----------------------------------------
 * Returns the point at which the line starts.
 */

   GPoint getStartPoint() const;

/*
 * Method: setEndPoint
 * Usage: line->setEndPoint(x, y);
 * -------------------------------
 * Sets the end point in the line to (<code>x</code>,&nbsp;<code>y</code>),
 * leaving the start point unchanged.  This method is therefore different from
 * <code>setLocation</code>, which moves both components of the line segment.
 */

   void setEndPoint(double x, double y);

/*
 * Method: getEndPoint
 * Usage: GPoint pt = line->getEndPoint();
 * ---------------------------------------
 * Returns the point at which the line ends.
 */

   GPoint getEndPoint() const;

/* Prototypes for the virtual methods */

   virtual GRectangle getBounds() const;
   virtual bool contains(double x, double y) const;
   virtual std::string getType() const;
   virtual std::string toString() const;

protected:

/* Instance variables */

   double dx;                   /* The x displacement of the line */
   double dy;                   /* The y displacement of the line */

};

'''
