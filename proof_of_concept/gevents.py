import platform
import gwindow
from enum import enum

# TODO error if not valid for all subtypes?
# TODO implement gtimer and ginteractor!

EventClassType = enum(  NULL_EVENT   = 0x000, \
						ACTION_EVENT = 0x010, \
						KEY_EVENT    = 0x020, \
						TIMER_EVENT  = 0x040, \
						WINDOW_EVENT = 0x080, \
						MOUSE_EVENT  = 0x100, \
						CLICK_EVENT  = 0x200, \
						ANY_EVENT    = 0x3F0)
						
EventType = enum(   WINDOW_CLOSED    = EventClassType.WINDOW_EVENT + 1, \
					WINDOW_RESIZED   = EventClassType.WINDOW_EVENT + 2, \
					ACTION_PERFORMED = EventClassType.ACTION_EVENT + 1, \
					MOUSE_CLICKED    = EventClassType.MOUSE_EVENT + 1, \
					MOUSE_PRESSED    = EventClassType.MOUSE_EVENT + 2, \
					MOUSE_RELEASED   = EventClassType.MOUSE_EVENT + 3, \
					MOUSE_MOVED      = EventClassType.MOUSE_EVENT + 4, \
					MOUSE_DRAGGED    = EventClassType.MOUSE_EVENT + 5, \
					KEY_PRESSED      = EventClassType.KEY_EVENT + 1, \
					KEY_RELEASED     = EventClassType.KEY_EVENT + 2, \
					KEY_TYPED        = EventClassType.KEY_EVENT + 3, \
					TIMER_TICKED     = EventClassType.TIMER_EVENT + 1)

ModifierCodes = enum(	SHIFT_DOWN     = 1 << 0, \
						CTRL_DOWN      = 1 << 1, \
						META_DOWN      = 1 << 2, \
						ALT_DOWN       = 1 << 3, \
						ALT_GRAPH_DOWN = 1 << 4, \
						BUTTON1_DOWN   = 1 << 5, \
						BUTTON2_DOWN   = 1 << 6, \
						BUTTON3_DOWN   = 1 << 7)
						
KeyCodes = enum(BACKSPACE_KEY = 8, \
				TAB_KEY = 9, \
				ENTER_KEY = 10, \
				CLEAR_KEY = 12, \
				ESCAPE_KEY = 27, \
				PAGE_UP_KEY = 33, \
				PAGE_DOWN_KEY = 34, \
				END_KEY = 35, \
				HOME_KEY = 36, \
				LEFT_ARROW_KEY = 37, \
				UP_ARROW_KEY = 38, \
				RIGHT_ARROW_KEY = 39, \
				DOWN_ARROW_KEY = 40, \
				F1_KEY = 112, \
				F2_KEY = 113, \
				F3_KEY = 114, \
				F4_KEY = 115, \
				F5_KEY = 116, \
				F6_KEY = 117, \
				F7_KEY = 118, \
				F8_KEY = 119, \
				F9_KEY = 120, \
				F10_KEY = 121, \
				F11_KEY = 122, \
				F12_KEY = 123, \
				DELETE_KEY = 127, \
				HELP_KEY = 156)
				
class GEvent:
	def __init__(self):
		self.eventClass = EventClassType.NULL_EVENT
		self.eventType = None
		self.valid = False
		self.modifiers = 0
		
	def getEventClass(self):
		return self.eventClass
		
	def getEventType(self):
		return self.eventType
		
	def getEventTime(self):
		return self.eventTime
		
	def getModifiers(self):
		return self.modifiers
		
	def toString(self):
		return "GEvent(NULL)";
		
	def isValid(self):
		return self.valid
		
	def setEventTime(self, time):
		self.eventTime = time
		
	def setModifiers(self, modifiers):
		self.modifiers = modifiers
		
class GWindowEvent(GEvent):
	def __init__(self, type = None, gw = None):
		self.valid = False
		if(type != None and gw != None):
			self.eventClass = EventClassType.WINDOW_EVENT
			self.eventType = type
			self.gwd = gw.gwd
			self.valid = True
	
	def getGWindow(self):
		return gwindow.GWindow(gwd = self.gwd)
		
	def toString(self):
		if(not self.valid): return "GWindowEvent(?)"
		result = "GWindowEvent:"
		if(self.eventType == EventType.WINDOW_CLOSED): result += "WINDOW_CLOSED"
		elif(self.eventType == EventType.WINDOW_RESIZED): result += "WINDOW_RESIZED"
		result += "()"
		return result

class GActionEvent(GEvent):
	def __init__(self, type = None, source = None, actionCommand = None):
		self.valid = False
		if(type != None and source != None and actionCommand != None):
			self.eventClass = EventClassType.ACTION_EVENT
			self.eventType = type
			self.source = source
			self.actionCommand = actionCommand
			valid = True
			
	def getSource(self):
		return self.source
		
	def getActionCommand(self):
		return self.actionCommand
		
	def toString(self):
		if(not valid): return "GActionEvent(?)"
		result = "GActionEvent:ACTION_PERFORMED(" + self.actionCommand + ")"
		return result
		
class GMouseEvent(GEvent):
	
	def __init__(self, type = None, gw = None, x = None, y = None):
		self.valid = False
		if(type != None and gw != None and x != None and y != None):
			self.eventClass = EventClassType.MOUSE_EVENT
			self.eventType = type
			self.gwd = gw.gwd
			self.x = x
			self.y = y
			self.valid = True
			
	def getGWindow(self):
		return gwindow.GWinodw(gwd = self.gwd)
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def toString(self):
		if(not valid): return "GMouseEvent(?)"
		result = "GMouseEvent:"
		if(self.eventType == EventType.MOUSE_PRESSED): result += "MOUSE_PRESSED"
		elif(self.eventType == EventType.MOUSE_RELEASED): result += "MOUSE_RELEASED"
		elif(self.eventType == EventType.MOUSE_CLICKED): result += "MOUSE_CLICKED"
		elif(self.eventType == EventType.MOUSE_MOVED): result += "MOUSE_MOVED"
		elif(self.eventType == EventType.MOUSE_DRAGGED): result += "MOUSE_DRAGGED"
		result += "(" + str(self.x) + ", " + str(self.y) + ")"
		return result
		
class GKeyEvent(GEvent):
	def __init__(self, type = None, gw = None, keyChar = None, keyCode = None):
		self.valid = False
		if(type != None and gw != None and keyChar != None and keyCode != None):
			self.eventClass = EventClassType.KEY_EVENT
			self.eventType = type
			self.gwd = gw.gwd
			self.keyChar = keyChar
			self.keyCode = keyCode
			self.valid = True
			
	def getGWindow(self):
		return gwindow.GWindow(gwd)
		
	def getKeyChar(self):
		return self.keyChar
		
	def getKeyCode(self):
		return self.keyCode
		
	def toString(self):
		if(not valid): return "GKeyEvent(?)"
		result = "GKeyEvent:"
		ch = None
		if(self.eventType == EventType.KEY_PRESSED): 
			result += "KEY_PRESSED"
			ch = self.keyCode
		elif(self.eventType == EventType.KEY_RELEASED):
			result += "KEY_RELEASED"
			ch = self.keyCode
		elif(self.eventType == EventType.KEY_TYPED):
			result += "KEY_TYPED"
			ch = self.keyChar
			
		if(ch != None and string.printable.find(ch) != -1):
			result += "('" + ch + "')"
		elif(ch != None):
			result += "('\\" + oct(ord(ch)) + "')"
		
		return result
	
class GTimerEvent(GEvent):
	def __init__(self, type = None, timer = None):
		valid = False
		if(type != None and timer != None):
			self.eventClass = EventClassType.TIMER_EVENT
			self.eventType = type
			self.gtd = timer.gtd
			valid = True
			
	def getGTimer(self):
		dummy = 1
		# TODO return gtimer.GTimer(gtd)
		
	def toString():
		if(not valid): return "GTimerEvent(?)"
		return "GTimerEvent:TIMER_TICKED()"
	
def waitForClick():
	waitForEvent(EventClassType.CLICK_EVENT)
	
def waitForEvent(mask = EventClassType.ANY_EVENT):
	dummy = 1
	#pp->waitForEvent(mask)

def getNextEvent(mask = EventClassType.ANY_EVENT):
	dummy = 1
	#pp->waitForEvent(mask)

if __name__ == '__main__':
	a = EventClassType.NULL_EVENT
	print a
	b = GEvent()
	print b.eventClass
	print b.getEventType()