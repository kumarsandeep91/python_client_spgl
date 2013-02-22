# Proof of concept for senior project

import subprocess
import time
import gwindow

def startupMain():
	args = ["java", "-jar", "spl.jar", "python.exe"]
	backend = subprocess.Popen(args, \
							   shell=False, \
	                           stdin=subprocess.PIPE, \
							   stdout=subprocess.PIPE, \
							   stderr=subprocess.STDOUT)
	
	created = backend.poll()
	print  created
	
	command = 'GCompound.create("0xabcdef")'
	backend.stdin.write(command+"\n")
	backend.stdin.flush()
	print "Command entered"
	
	time.sleep(1)
	
	command = 'GWindow.create("0x123456", 200, 200, "0xabcdef")'
	backend.stdin.write(command+"\n")
	backend.stdin.flush()
	print "Command entered"

	backend.stdin.write('GRect.create("rect1", 25, 25)\n')
	backend.stdin.write('GObject.setFilled("rect1", true)\n')
	backend.stdin.write('GCompound.add("0xabcdef", "rect1")\n')
	
	#do work
	raw_input("pause - hit enter to continue")
	
	backend.kill()
	
print gwindow.convertRGBToColor(1)
	
startupMain()
