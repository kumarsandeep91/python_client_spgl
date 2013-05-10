'''
The platform module is resonsible for initalizing the connection to the java back end
as well as sending and receiving interprocess communcations. This module should not
be referenced by applications using the SPGL
'''
import subprocess
import time
import gwindow
import gtimer
import gevents
from gevents import EventClassType
from gevents import EventType
from gevents import ModifierCodes
from gevents import KeyCodes
import gobjects
import gtypes
import strlib
import Queue
import re
import sys
import os

class Platform:

	SOURCE_TABLE = None
	TIMER_TABLE = None
	WINDOW_TABLE = None
	BACKEND = None
	EVENT_QUEUE = None

	def __init__(self):
		if(Platform.BACKEND == None):
			self.startupMain()
			Platform.EVENT_QUEUE = Queue.Queue()
			Platform.SOURCE_TABLE = {}
			Platform.TIMER_TABLE = {}
			Platform.WINDOW_TABLE = {}
		
	def createGCompound(self, gobj):
		command = "GCompound.create(\"" + gobj.ID + "\")"
		
		self.putPipe(command)
		
	def createGWindow(self, gw, width, height, topCompound):
		command = "GWindow.create(\"" + str(gw.gwd.ID) + "\", " + str(width) + \
				  ", " + str(height) + ", \"" + str(topCompound.ID) + "\")"
		Platform.WINDOW_TABLE[gw.gwd.ID] = gw.gwd
		self.putPipe(command)
	
	def createGRect(self, gobj, width, height):
		command = "GRect.create(\"" + gobj.ID + "\", " + str(width) + \
				   ", " + str(height) + ")"
		self.putPipe(command)
		
	def setLocation(self, gobj, x, y):
		command = "GObject.setLocation(\"" + gobj.ID + "\", " + str(x) + \
				   ", " + str(y) + ")"		
		self.putPipe(command)
	
	def setFilled(self, gobj, flag):
		if(flag): flag = "true"
		else: flag = "false"
		command = "GObject.setFilled(\"" + gobj.ID + "\", " + flag + ")"		
		self.putPipe(command)
		
	def add(self, compound, gobj):
		command = "GCompound.add(\"" + str(compound.ID) + "\", \"" + \
				   gobj.ID + "\")"		
		self.putPipe(command)
	
	def remove(self, gobj):
		command = "GObject.remove(\"" + gobj.ID + "\")"		
		self.putPipe(command)
		
	def setColor(self, gobj, color):
		command = "GObject.setColor(\"" + gobj.ID + "\", \"" + color + "\")"		
		self.putPipe(command)
		
	def setFillColor(self, gobj, color):
		command = "GObject.setFillColor(\"" + gobj.ID + "\", \"" + color + "\")"		
		self.putPipe(command)
		
	def close(self, gw):
		command = "GWindow.close(\"" + str(gw.gwd.ID) + "\")"		
		self.putPipe(command)
		
	def deleteGWindow(self, gw):
		command = "GWindow.delete(\"" + str(gw.gwd.ID) + "\")"		
		self.putPipe(command)
		
	def requestFocus(self, gw):
		command = "GWindow.requestFocus(\"" + str(gw.gwd.ID) + "\")"		
		self.putPipe(command)
		
	def clear(self, gw):
		command = "GWindow.clear(\"" + str(gw.gwd.ID) + "\")"		
		self.putPipe(command)
		
	def repaint(self, gw):
		command = "GWindow.repaint(\"" + str(gw.gwd.ID) + "\")"		
		self.putPipe(command)
		
	def setVisible(self, flag, gobj = None, gw = None):
		if(gw != None):
			command = "GWindow.setVisible(\"" + str(gw.gwd.ID) + "\", " + \
						str(flag).lower() + ")"			
			self.putPipe(command)
		elif(gobj != None):
			command = "GObject.setVisible(\"" + gobj.ID + "\", " + \
						str(flag).lower() + ")"			
			self.putPipe(command)
			
	def createGRoundRect(self, gobj, width, height, corner):
		command = "GRoundRect.create(\"" + gobj.ID + "\", " + str(width) + \
					", " + str(height) + ", " + str(corner) + ")"
		self.putPipe(command)
			
	def createG3DRect(self, gobj, width, height, raised):
		command = "G3DRect.create(\"" + gobj.ID + "\", " + str(width) + \
					", " + str(height) + ", " + raised + ")"
		self.putPipe(command)
		
	def setRaised(self, gobj, raised):
		command = "G3DRect.setRaised(\"" + gobj.ID + "\", " + raised + ")"
		self.putPipe(command)
		
	def createGLabel(self, gobj, label):
		command = "GLabel.create(\"" +gobj.ID+ "\", \"" + label + "\")"
		self.putPipe(command)
		
	def createGLine(self, gobj, x1, y1, x2, y2):
		command = "GLine.create(\"" +gobj.ID+ "\", " + str(x1) + ", " + str(y1) \
					+ ", " + str(x2) + ", " + str(y2) + ")"
		self.putPipe(command)
		
	def setStartPoint(self, gobj, x, y):
		command = "GLine.setStartPoint(\"" +gobj.ID+ "\", " + \
					str(x) + ", " + str(y) + ")"
		self.putPipe(command)

	def setEndPoint(self, gobj, x, y):   
		command = "GLine.setEndPoint(\"" +gobj.ID+ "\", " + \
					str(x) + ", " + str(y) + ")"
		self.putPipe(command)

	def createGArc(self, gobj, width, height, start, sweep):   
		command = "GArc.create(\"" +gobj.ID+ "\", " + \
					str(width) + ", " + str(height) + \
					", " + str(start) + ", " + str(sweep) + ")"
		self.putPipe(command)

	def setStartAngle(self, gobj, angle):
		command = "GArc.setStartAngle(\"" +gobj.ID+ "\", " + str(angle) + ")"
		self.putPipe(command)

	def setSweepAngle(self, gobj, angle):
		command = "GArc.setSweepAngle(\"" +gobj.ID+ "\", " + str(angle) + ")"
		self.putPipe(command)

	def createGImage(self, gobj,  filename):
		if(filename[0] != "/" and filename[1:3] != ":\\"):
			filename = os.getcwd() + os.sep + filename
		for i in range(len(filename)):
			if(filename[i] == "\\"):
				filename = filename[:i] + "/" + filename[i+1:]
		
		command = "GImage.create(\"" +gobj.ID+ "\", \"" + filename + "\")"
		self.putPipe(command)
		result = self.getResult()
		if (not result.startswith("GDimension(")): raise Exception(result)
		return self.scanDimension(result) 

	def createGPolygon(self, gobj):   
		command = "GPolygon.create(\"" +gobj.ID+ "\")"
		self.putPipe(command)

	def addVertex(self, gobj, x, y):   
		command = "GPolygon.addVertex(\"" +gobj.ID+ "\", " + \
					str(x) + ", " + str(y) + ")"
		self.putPipe(command)

	def createGOval(self, gobj, width, height):   
		command = "GOval.create(\"" +gobj.ID+ "\", " + \
					str(width) + ", " + str(height) + ")"
		self.putPipe(command)
			
	def setSize(self, gobj, width, height):
		command = "GObject.setSize(\"" + gobj.ID + "\", " + \
					str(width) + ", " + str(height) + ")"
		self.putPipe(command)
					
	def getBounds(self, gobj):
		command = "GObject.getBounds(\"" + gobj.ID + "\")"
		self.putPipe(command)
		result = self.getResult()
		if (not result.startsWith("GRectangle(")): raise Exception(result)
		return self.scanRectangle(result)
		
	def setLineWidth(self, gobj, lineWidth):
		command = "GObject.setLineWidth(\"" + gobj.ID + "\", " + str(lineWidth) + ")"
		self.putPipe(command)
		
	def contains(self, gobj, x, y):
		command = "GObject.contains(\"" + gobj.ID + "\", " + \
					str(x) + ", " + str(y) + ")"
		self.putPipe(command)
		return (self.getResult() == "true")
		
	def setFrameRectangle(self, gobj, x, y, width, height):
		command = "GArc.setFrameRectangle(\"" + gobj.ID + "\", " + \
					str(x) + ", " + str(y) + ", " + \
					str(width) + ", " + str(height) + ")"
					
	def setFont(self, gobj, font):
		command = "GLabel.setFont(\"" + gobj.ID + "\", \"" + font + "\")"
		self.putPipe(command)
		
	def setLabel(self, gobj, str):
		command = "GLabel.setLabel(\"" + gobj.ID + "\", \"" + \
					strlib.writeQuotedString(str) + "\")"
		self.putPipe(command);
		
	def getFontAscent(self, gobj):
		command = "GLabel.getFontAscent(\"" + gobj.ID + "\")"
		self.putPipe(command)
		return float(self.getResult())
		
	def getFontDescent(self, gobj):
		command = "GLabel.getFontDescent(\"" + gobj.ID + "\")"
		self.putPipe(command)
		return float(self.getResult())
		
	def getGLabelSize(self, gobj):
		command = "GLabel.getGLabelSize(\"" + gobj.ID + "\")"
		self.putPipe(command)
		return self.scanDimension(self.getResult())
		
	def createTimer(self, timer, delay):
		Platform.TIMER_TABLE[timer.gtd.ID] = timer.gtd
		command = "GTimer.create(\"" + timer.gtd.ID + "\", " + str(delay) + ")"
		self.putPipe(command)
		
	def startTimer(self, timer):
		command = "GTimer.startTimer(\"" + timer.gtd.ID + "\")"
		self.putPipe(command)
		
	def stopTimer(self, timer):
		command = "GTimer.stopTimer(\"" + timer.gtd.ID + "\")"
		self.putPipe(command)
		
	def setWindowTitle(self, gw, title):
		command = "GWindow.setTitle(\"" + gw.gwd.ID + "\", " + \
			strlib.writeQuotedString(title) + ")"
		self.putPipe(command)
		
	def getScreenWidth(self):
		command = "GWindow.getScreenWidth()"
		self.putPipe(command)
		return float(self.getResult())
		
	def getScreenHeight(self):
		command = "GWindow.getScreenHeight()"
		self.putPipe(command)
		return float(self.getResult())
		
	def exitGraphics(self):
		command = "GWindow.exitGraphics()"
		self.putPipe(command)
		
	def draw(self, gw, gobj):
		command = "GWindow.draw(\"" + gw.gwd.ID + "\", \"" + gobj.ID + "\")"
		self.putPipe(command)
		
	def createSound(self, sound, filename):
		if(filename[0] != "/" and filename[1:3] != ":\\"):
			filename = os.getcwd() + os.sep + filename
		for i in range(len(filename)):
			if(filename[i] == "\\"):
				filename = filename[:i] + "/" + filename[i+1:]
				
		command = "Sound.create(\"" + sound.ID + "\", \"" + filename + "\")"
		self.putPipe(command)
		print self.getResult()
		
	def deleteSound(self, sound):
		command = "Sound.delete(\"" + sound.ID + "\")"
		self.putPipe(command)
		
	def playSound(self, sound):
		command = "Sound.play(\"" + sound.ID + "\")"
		self.putPipe(command)
		
	def clearConsole(self):
		command = "JBEConsole.clear()"
		self.putPipe(command)
		
	def setConsoleFont(self, font):
		command = "JBEConsole.setFont(\"" + font + "\")"
		self.putPipe(command)
		
	def setConsoleSize(self, width, height):
		command = "JBEConsole.setSize(" + str(width) + ", " + str(height) + ")"
		self.putPipe(command)
		
	def scale(self, gobj, sx, sy):
		command = "GObject.scale(\"" + gobj.ID + "\", " + \
					str(sx) + ", " + str(sy) + ")"
		self.putPipe(command)
		
	def rotate(self, gobj, theta):
		command = "GObject.rotate(\"" + gobj.ID + "\", " + str(theta) + ")"
		self.putPipe(command)
		
	def setActionCommand(self, gobj, cmd):
		command = "GInteractor.setActionCommand(\"" + gobj.ID + "\", " + \
					strlib.writeQuotedString(cmd) + ")"
		self.putPipe(command)
		
	def getSize(self, gobj):
		command = "GInteractor.getSize(\"" + gobj.ID + "\")"
		self.putPipe(command)
		return self.scanDimension(self.getResult())
		
	def createGButton(self, gobj, label):
		Platform.SOURCE_TABLE[gobj.ID] = gobj
		command = "GButton.create(\"" + gobj.ID + "\", " + \
					strlib.writeQuotedString(label) + ")"
		self.putPipe(command)
		
	def createGCheckBox(self, gobj, label):
		Platform.SOURCE_TABLE[gobj.ID] = gobj
		command = "GCheckBox.create(\"" + gobj.ID + "\", " + \
					strlib.writeQuotedString(label) + ")"
		self.putPipe(command)
		
	def isSelected(self, gobj):
		command = "GCheckBox.isSelected(\"" + gobj.ID + "\")"
		self.putPipe(command)
		result = self.getResult().strip()
		print result
		return result == "true"
		
	def setSelected(self, gobj, state):
		command = "GCheckBox.setSelected(\"" + gobj.ID + "\", " + \
					str(state).lower() + ")"
		self.putPipe(command)
		
	def createGSlider(self, gobj, min, max, value):
		Platform.SOURCE_TABLE[gobj.ID] = gobj
		command = "GSlider.create(\"" + gobj.ID + "\", " + str(min) + ", " + \
					str(max) + ", " + str(value) + ")"
		self.putPipe(command)
		
	def getValue(self, gobj):
		command = "GSlider.getValue(\"" + gobj.ID + "\")"
		self.putPipe(command)
		return int(self.getResult())
		
	def setValue(self, gobj, value):
		command = "GSlider.setValue(\"" + gobj.ID + "\", " + str(value) + ")"
		self.putPipe(command) 
	
	def createGTextField(self, gobj, nChars):
		Platform.SOURCE_TABLE[gobj.ID] = gobj
		command = "GTextField.create(\"" + gobj.ID + "\", " + str(nChars) + ")"
		self.putPipe(command)
		
	def getText(self, gobj):
		command = "GTextField.getText(\"" + gobj.ID + "\")"
		self.putPipe(command)
		return self.getResult()
		
	def setText(self, gobj, str):
		command = "GTextField.setText(\"" + gobj.ID + "\", " + \
					strlib.writeQuotedString(str) + ")"
		self.putPipe(command)
		
	def createGChooser(self, gobj):
		Platform.SOURCE_TABLE[gobj.ID] = gobj
		command = "GChooser.create(\"" + gobj.ID + "\")"
		self.putPipe(command)
		
	def addItem(self, gobj, item):
		command = "GChooser.addItem(\"" + gobj.ID + "\", " + \
					strlib.writeQuotedString(item) + ")"
		self.putPipe(command)
		
	def getSelectedItem(self, gobj):
		command = "GChooser.getSelectedItem(\"" + gobj.ID + "\")"
		self.putPipe(command)
		return self.getResult()
		
	def setSelectedItem(self, gobj, item):
		command = "GChooser.setSelectedItem(\"" + gobj.ID + "\", " + \
					strlib.writeQuotedString(item) + ")"
		self.putPipe(command)

	def sendForward(self, gobj):
		command = "GObject.sendForward(\"" + gobj.ID + "\")"
		self.putPipe(command)

	def sendToFront(self, gobj):
		command = "GObject.sendToFront(\"" + gobj.ID + "\")"
		self.putPipe(command)

	def sendBackward(self, gobj):
		command = "GObject.sendBackward(\"" + gobj.ID + "\")"
		self.putPipe(command)

	def sendToBack(self, gobj):
		command = "GObject.sendToBack(\"" + gobj.ID + "\")"
		self.putPipe(command)
		
	def setRegionAlignment(self, gw, region, align):
		command = "GWindow.setRegionAlignmnet(\"" + gw.gwd.ID + "\", \"" + \
					region, "\", \"" + align + "\")"
		self.putPipe(command)
		
	def addToRegion(self, gw, gobj, region):
		command = "GWindow.addToRegion(\"" + gw.gwd.ID + "\", \"" + \
					gobj.ID + "\", \"" + region + "\")"
		self.putPipe(command)
		
	def removeFromRegion(self, gw, gobj, region):
		command = "GWindow.removeFromRegion(\"" + gw.gwd.ID + "\", \"" + \
					gobj.ID + "\", \"" + region + "\")"
		self.putPipe(command)
			
	def openFileDialog(self, title, mode, path):
		command = "File.openFileDialog(" + strlib.writeQuotedString(title) \
					+ ", \"" + mode + "\", \"" + path + "\")"
		
		self.putPipe(command)
		result = self.getResult().strip()
		return result
		
	def getNextEvent(self, mask):
		if(Platform.EVENT_QUEUE.empty()):
			self.putPipe("GEvent.getNextEvent(" + str(mask) + ")")
			self.getResult();
			if(Platform.EVENT_QUEUE.empty()):
				return gevents.GEvent()
		return Platform.EVENT_QUEUE.get()
		
	def waitForEvent(self, mask):
		while(Platform.EVENT_QUEUE.empty()):
			self.putPipe("GEvent.waitForEvent(" + str(mask) + ")")
			self.getResult()
		return Platform.EVENT_QUEUE.get()

	def parseEvent(self, line):
		try:
			tokens = re.findall(r"[-\w\.\(]+", line)
			if(tokens[0] == "mousePressed("):
				return self.parseMouseEvent(tokens[1:], EventType.MOUSE_PRESSED)
			elif(tokens[0] == "mouseReleased("): 
				return self.parseMouseEvent(tokens[1:], EventType.MOUSE_RELEASED)
			elif(tokens[0] == "mouseClicked("): 
				return self.parseMouseEvent(tokens[1:], EventType.MOUSE_CLICKED)
			elif(tokens[0] == "mouseMoved("): 
				return self.parseMouseEvent(tokens[1:], EventType.MOUSE_MOVED)
			elif(tokens[0] == "mouseDragged("): 
				return self.parseMouseEvent(tokens[1:], EventType.MOUSE_DRAGGED)
			elif(tokens[0] == "keyPressed("): 
				return self.parseKeyEvent(tokens[1:], EventType.KEY_PRESSED)
			elif(tokens[0] == "keyReleased("): 
				return self.parseMouseEvent(tokens[1:], EventType.KEY_RELEASED)
			elif(tokens[0] == "keyTyped("): 
				return self.parseKeyEvent(tokens[1:], EventType.KEY_TYPED)
			elif(tokens[0] == "actionPerformed("): 
				return self.parseActionEvent(tokens[1:], EventType.ACTION_PERFORMED)
			elif(tokens[0] == "timerTicked("): 
				return self.parseTimerEvent(tokens[1:], EventType.TIMER_TICKED)
			elif(tokens[0] == "windowClosed("): 
				return self.parseWindowEvent(tokens[1:], EventType.WINDOW_CLOSED)
			elif(tokens[0] == "windowResized("): 
				return self.parseWindowEvent(tokens[1:], EventType.RESIZED)
			elif(tokens[0] == "lastWindowClosed("): 
				print "Exited normally"
				sys.exit(0)
			else:
				dummy = 1
				# ignore for now
			return gevents.GEvent()
		except Exception as inst:
			print "EXCEPTION"
			print "type:"
			print type(inst)
			print "exception data:"
			print inst
			print "line:"
			print line
			return gevents.GEvent()
  
	def parseMouseEvent(self, tokens, type):
		id = tokens[0]
		tokens = tokens[1:]
		
		time = float(tokens[0])
		tokens = tokens[1:]
		
		modifiers = int(tokens[0])
		tokens = tokens[1:]
		
		x = float(tokens[0])
		tokens = tokens[1:]
		
		y = float(tokens[0])
		tokens = tokens[1:]
		
		e = gevents.GMouseEvent(type, \
								gwindow.GWindow(gwd = Platform.WINDOW_TABLE[id]), \
								x, \
								y)
		e.setEventTime(time)
		e.setModifiers(modifiers)
		return e
  
	def parseKeyEvent(self, tokens, type):
		id = tokens[0]
		tokens = tokens[1:]
		
		time = float(tokens[0])
		tokens = tokens[1:]
		
		modifiers = int(tokens[0])
		tokens = tokens[1:]
		
		keyChar = int(tokens[0])
		tokens = tokens[1:]
		
		keyCode = int(tokens[0])
		tokens = tokens[1:]
		
		e = gevents.GKeyEvent(type, \
								gwindow.GWindow(gwd = Platform.WINDOW_TABLE[id]), \
								keyChar, \
								keyCode)
		e.setEventTime(time)
		e.setModifiers(modifiers)
		return e
		
	def parseTimerEvent(self, tokens, type):
		id = tokens[0]
		tokens = tokens[1:]
		
		time = float(tokens[0])
		tokens = tokens[1:]
		
		e = gevents.GTimerEvent(type, gtimer.GTimer(Platform.TIMER_TABLE[id]))
		e.setEventTime(time)
		return e
		
	def parseWindowEvent(self, tokens, type):
		id = tokens[0]
		tokens = tokens[1:]
		
		time = float(tokens[0])
		tokens = tokens[1:]
		
		e = gevents.GWindowEvent(type, gwindow.GWindow(Platform.WINDOW_TABLE[id]))
		e.setEventTime(time)
		return e
		
	def parseActionEvent(self, tokens, type):
		id = tokens[0]
		tokens = tokens[1:]
		
		action = tokens[0]
		tokens = tokens[1:]
		
		time = float(tokens[0])
		tokens = tokens[1:]
		
		e = gevents.GActionEvent(type, Platform.SOURCE_TABLE[id], action)
		e.setEventTime(time)
		return e
		
	def scanDimension(self, str):
		tokens = re.findall(r"[-:\w\.]+", str)
		#skip "GDimension"
		tokens = tokens[1:]
		width = float(tokens[0])
		tokens = tokens[1:]
		height = float(tokens[0])
		return gtypes.GDimension(width, height)
		
	def scanRectangle(self, str):
		tokens = re.findall(r"[-:\w\.]+", str)
		#skip "GRectangle"
		tokens = tokens[1:]
		x = float(tokens[0])
		tokens = tokens[1:]
		y = float(tokens[0])
		tokens = tokens[1:]
		width = float(tokens[0])
		tokens = tokens[1:]
		height = float(tokens[0])
		return gtypes.GRectangle(x, y, width, height)
  
	def putPipe(self, command):
		print command
		Platform.BACKEND.stdin.write(command+"\n")
		Platform.BACKEND.stdin.flush()
	
	def getPipe(self):
		return Platform.BACKEND.stdout.readline()
		
	def getResult(self):
		while(True):
			line = self.getPipe()
			if(line.startswith("result:")): return line[7:]
			if(line.startswith("event:")):
				Platform.EVENT_QUEUE.put(self.parseEvent(line[6:]))
	
	
	def startupMain(self):
		# if spl.jar is in same dir as user program then use this line:
		spl_loc = os.getcwd() + "\\spl.jar"
		# if spl.jar is not in same dir as user program use this line:
		#spl_loc = os.path.dirname(os.path.realpath(__file__)) + "\\spl.jar"
		args = ["java", "-jar", spl_loc, "python.exe"]
		backend = subprocess.Popen(args, \
								   shell=False, \
	                               stdin=subprocess.PIPE, \
								   stdout=subprocess.PIPE, \
								   stderr=subprocess.STDOUT)
								   
		Platform.BACKEND = backend
