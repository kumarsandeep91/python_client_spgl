# Proof of concept for senior project
import subprocess
import time
import gwindow
import gobjects
import gtypes

class Platform:

	BACKEND = None

	def __init__(self):
		if(Platform.BACKEND == None):
			self.startupMain()
		
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
		

  # TODO pp.remove(gobj)
  # TODO pp.setSize(self, width, height)
  # TODO pp.setVisible(self, flag)
  # TODO pp.contains(self, x, y)
  # TODO pp.setFilled(self, flag)
  # TODO pp.getBounds(self)
  
  # TODO pp.setLineWidth(self, lineWidth)
  # TODO pp.setColor(self, self.color)
  # TODO pp.scale(self, sx, sy)
  # TODO pp.rotate(self, sx, sy)
  # TODO pp.setFillColor(self, color)
  # TODO pp.sendForward(gobj)
  # TODO pp.sendToFront(gobj)
  # TODO pp.sendBackward(gobj)
  # TODO pp.sendToBack(gobj)
  # TODO pp.close(self)
  # TODO pp.deleteGWindow(self)
  # TODO pp.requestFocus(self)
  # TODO pp.clear(self)
  # TODO pp.repaint(self)
  # TODO pp.setWindowTitle(self, title)
  # TODO pp.draw(self, gobj)

	def putPipe(self,command):
		Platform.BACKEND.stdin.write(command+"\n")
		Platform.BACKEND.stdin.flush()
	
	def startupMain(self):
		args = ["java", "-jar", "spl.jar", "python.exe"]
		backend = subprocess.Popen(args, \
								   shell=False, \
	                               stdin=subprocess.PIPE, \
								   stdout=subprocess.PIPE, \
								   stderr=subprocess.STDOUT)
								   
		Platform.BACKEND = backend
	
		#backend.kill()

