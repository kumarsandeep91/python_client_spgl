# Proof of concept for senior project
import subprocess
import time
import gwindow
import gobjects
import gtypes
import strlib
import Queue

class Platform:

	BACKEND = None
	EVENT_QUEUE = None

	def __init__(self):
		if(Platform.BACKEND == None):
			self.startupMain()
			Platform.EVENT_QUEUE = Queue.Queue()
		
	def createGCompound(self, gobj):
		command = "GCompound.create(\"" + str(gobj.ID) + "\")"
		print command
		self.putPipe(command)
		
	def createGWindow(self, gw, width, height, topCompound):
		command = "GWindow.create(\"" + str(gw.gwd.ID) + "\", " + str(width) + \
				  ", " + str(height) + ", \"" + str(topCompound.ID) + "\")"
		print command
		self.putPipe(command)
	
	def createGRect(self, gobj, width, height):
		command = "GRect.create(\"" + str(gobj.ID) + "\", " + str(width) + \
				   ", " + str(height) + ")"
		print command
		self.putPipe(command)
		
	def setLocation(self, gobj, x, y):
		command = "GObject.setLocation(\"" + str(gobj.ID) + "\", " + str(x) + \
				   ", " + str(y) + ")"
		print command
		self.putPipe(command)
	
	def setFilled(self, gobj, flag):
		if(flag): flag = "true"
		else: flag = "false"
		command = "GObject.setFilled(\"" + str(gobj.ID) + "\", " + flag + ")"
		print command
		self.putPipe(command)
		
	def add(self, compound, gobj):
		command = "GCompound.add(\"" + str(compound.ID) + "\", \"" + \
				   str(gobj.ID) + "\")"
		print command
		self.putPipe(command)
	
	def remove(self, gobj):
		command = "GObject.remove(\"" + str(gobj.ID) + "\")"
		print command
		self.putPipe(command)
		
	def setColor(self, gobj, color):
		command = "GObject.setColor(\"" + str(gobj.ID) + "\", \"" + color + "\")"
		print command
		self.putPipe(command)
		
	def setFillColor(self, gobj, color):
		command = "GObject.setFillColor(\"" + str(gobj.ID) + "\", \"" + color + "\")"
		print command
		self.putPipe(command)
		
	def close(self, gw):
		command = "GWindow.close(\"" + str(gw.gwd.ID) + "\")"
		print command
		self.putPipe(command)
		
	def deleteGWindow(self, gw):
		command = "GWindow.delete(\"" + str(gw.gwd.ID) + "\")"
		print command
		self.putPipe(command)
		
	def requestFocus(self, gw):
		command = "GWindow.requestFocus(\"" + str(gw.gwd.ID) + "\")"
		print command
		self.putPipe(command)
		
	def clear(self, gw):
		command = "GWindow.clear(\"" + str(gw.gwd.ID) + "\")"
		print command
		self.putPipe(command)
		
	def repaint(self, gw):
		command = "GWindow.repaint(\"" + str(gw.gwd.ID) + "\")"
		print command
		self.putPipe(command)
		
	def setVisible(self, flag, gw = None, gobj = None):
		if(gw != None):
			command = "GWindow.setVisible(\"" + str(gw.gwd.ID) + "\", " + \
						str(flag).lower() + ")"
			print command
			self.putPipe(command)
		elif(gobj != None):
			command = "GObject.setVisible(\"" + str(gobj.ID) + "\", " + \
						str(flag).lower() + ")"
			print command
			self.putPipe(command)
			
	def openFileDialog(self, title, mode, path):
		command = "File.openFileDialog(" + strlib.writeQuotedString(title) \
					+ ", \"" + mode + "\", \"" + path + "\")"
		print command
		self.putPipe(command)
		result = self.getResult().strip()
		print result
		return result
		
	def getNextEvent(self, mask):
		dummy = 1
		
	def waitForEvent(self, mask):
		dummy = 1
		
  # TODO pp.setSize(self, width, height)
  # TODO pp.contains(self, x, y)
  # TODO pp.getBounds(self)
  # TODO pp.setLineWidth(self, lineWidth)
  # TODO pp.scale(self, sx, sy)
  # TODO pp.rotate(self, sx, sy)
  # TODO pp.sendForward(gobj)
  # TODO pp.sendToFront(gobj)
  # TODO pp.sendBackward(gobj)
  # TODO pp.sendToBack(gobj)
  # TODO pp.setWindowTitle(self, title)
  # TODO pp.draw(self, gobj)

	def parseEvent(self, line):
		# TODO use shlex
		dummy = 1
  
	def putPipe(self,command):
		Platform.BACKEND.stdin.write(command+"\n")
		Platform.BACKEND.stdin.flush()
	
	def getPipe(self):
		return Platform.BACKEND.stdout.readline()
		
	def getResult(self):
		while(True):
			line = self.getPipe()
			if(line.startswith("result:")): return line[7:]
			if(line.startswith("event:")):
				Platform.EVENT_QUEUE.put(parseEvent(line[6:]))
	
	
	def startupMain(self):
		args = ["java", "-jar", "spl.jar", "python.exe"]
		backend = subprocess.Popen(args, \
								   shell=False, \
	                               stdin=subprocess.PIPE, \
								   stdout=subprocess.PIPE, \
								   stderr=subprocess.STDOUT)
								   
		Platform.BACKEND = backend
	
		#TODO backend.kill()

