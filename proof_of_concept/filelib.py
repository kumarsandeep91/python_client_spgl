import platform
import os
if(os.name == "posix"): import pwd

def expandPathname(filename):
	if(filename == ""): return ""
	length = len(filename)
	if(os.name == "posix"):
		strPos = 1
		while(strPos < length \
			and filename[strPos] != "\\" \
			and filename[strPos] != "/"):
			strPos += 1
			
		homedir = None
		if(strPos == 1):
			homedir = os.getenv("HOME")
			if(homedir == None): homedir = pwd.getpwuid(os.getuid()).pw_dir
		else:
			pw = pwd.getpwnam(filename[1:strPos])
			if(pw == None): 
				dummy = 1 # TODO error no such user can't expand path
			homedir = pw.pw_dir
		
		filename = homedir + filename[strPos:]
		length = len(filename)
		
		for i in range(length):
			if(filename[i] == "\\"):
				filename = filename[:i] + "/" + filename[i+1:]
		
	else:
		for i in range(length):
			if(filename[i] == "/"):
				filename = filename[:i] + "\\" + filename[i+1:]
	
	return filename
	
def openFile(filename, binary=False):
	mode = "r+"
	if(binary):
		mode = "r+b"
	
	file = None
	
	try:
		file = open(expandPathname(filename), mode)	
	except IOError:
		file = None
		
	return file
	
def promptUserForFile(prompt, binary=False):
	while(True):
		filename = raw_input(prompt)
		file = openFile(filename, binary)
		if(file != None): return file
		print "Unable to open that file. Try again."
		if(prompt == ""): prompt = "Filename: "
		
def openFileDialog(title = "Open File", mode="load", path = "", binary=False):
	filename = platform.Platform().openFileDialog(title, mode, path)
	if(filename == ""): return None
	file = openFile(filename, binary)
	if(file != None):
		return file
	return None
	
def readEntireFile(file):
	return file.readlines()
		
def getRoot(filename):
	dot = -1
	length = len(filename)
	for i in range(length):
		if(filename[i] == "."): dot = i
		if(filename[i] == "/" or filename[i] == "\\"): dot = -1
	
	if(dot == -1):
		return filename
	else:
		return filename[:dot]
		
def getExtension(filename):
	dot = -1
	length = len(filename)
	for i in range(length):
		if(filename[i] == "."): dot = i
		if(filename[i] == "/" or filename[i] == "\\"): dot = -1
	
	if(dot == -1):
		return ""
	else:
		return filename[dot:]
	
def getHead(filename):
	slash = -1
	length = len(filename)
	for i in range(length):
		if(filename[i] == "/" or filename[i] == "\\"):
			slash = i
	
	if(slash == -1):
		return ""
	elif(slash == 0):
		return "/"
	else:
		return filename[0:slash]

def getTail(filename):
	slash = -1
	length = len(filename)
	for i in range(length):
		if(filename[i] == "/" or filename[i] == "\\"):
			slash = i
	
	if(slash == -1):
		return filename
	else:
		return filename[slash+1:]

def defaultExtension(filename, ext):
	force = (ext[0] == "*")
	if(force): ext = ext[1:]
	dot = -1
	length = len(filename)
	for i in range(length):
		if(filename[i] == "."): dot = i
		if(filename[i] == "/" or filename[i] == "\\"): dot = -1
	
	if(dot == -1):
		force = True
		dot = length
	
	if(force):
		return filename[0:dot] + ext
	else:
		return filename
	
def openOnPath(path, filename, binary = False):
	paths = splitPath(path)
	for dir in paths:
		pathname = dir + "/" + filename
		file = openFile(pathname, binary)
		if(file != None): return file
	
	return None

def findOnPath(path, filename):
	file = openOnPath(path, filename)
	if(file == None): 
		return None
		
	file.close()
	return file.name
	
def deleteFile(filename):
	os.remove(expandPathname(filename))
	
def renameFile(oldname, newname):
	oldname = expandPathname(oldname)
	newname = expandPathname(newname)
	os.rename(oldname, newname)
	
def createDirectory(path):
	os.mkdir(path)
	
def createDirectoryPath(path):
	if(path.find(os.pardir) == -1):
		os.makedirs(path)
	else: 
		return # TODO throw error since pardir confuses makedirs?

def fileExists(filename):
	return os.path.exists(filename)
	
def isFile(filename):
	return os.path.isfile(filename)
	
def isSymbolicLink(filename):
	return os.path.islink(filename)

def isDirectory(filename):
	return os.path.isdir(filename)
	
def setCurrentDirectory(path):
	return os.chdir(path)
	
def getCurrentDirectory():
	return os.getcwd()
	
def listDirectory(path):
	return os.listdir(path).sort()
	
def getDirectoryPathSeparator():
	return os.sep

def getSearchPathSeparator():
	return os.pathsep
	
def matchFilenamePattern(filename, pattern):
	return recursiveMatch(filename, 0, pattern, 0)

def splitPath(path):
	list = []
	sep = ":" if (path.find(";") == -1) else ";"
	path += sep
	start = 0
	while(True):
		finish = path.find(sep, start)
		if(finish == -1): break
		if(finish > start + 1):
			list.append(path[start:finish])
		start = finish + 1
		
	return list

def recursiveMatch(str, sx, pattern, px):
	slen = len(str)
	plen = len(pattern)
	if(px == plen): return (sx == slen)
	pch = pattern[px]
	
	if(pch == "*"):
		for i in range(sx, slen + 1):
			if(recursiveMatch(str, i, pattern, px + 1)): return True
		return False
	
	if(sx == slen): return False
	
	sch = str[sx]
	if(pch == "["):
		match = False
		invert = False
		px += 1
		if(px == plen):
			#TODO Throw error: missing ]
			dummy = 1
		if(pattern[px] == "^"):
			px += 1
			invert = True
		while(px < plen and pattern[px] != "]"):
			if(px + 2 < plen and pattern[px + 1] == "-"):
				match = (match or (sch >= pattern[px] and sch <= pattern[px+2]))
				px += 3
			else:
				match = (match or (sch == pattern[px]))
				px += 1
		if(px == plen):
			# TODO throw error: missing ]
			dummy = 1
		if(match == invert): return False
	elif(pch != "?"):
		if(pch != sch): return False
	return recursiveMatch(str, sx + 1, pattern, px +1)
				
	
	
if __name__ == '__main__':
	
	filename = "/Users/Alex/Documents/Stanford/senior_project/python_client_spgl/proof_of_concept/notes.txt"
	filename = expandPathname(filename)
	print "expandPathname1 -- should have \\ on windows / on posix"
	print "\t" + filename
	print ""
	
	filename = "\\Users\\Alex\\Documents\\Stanford\\senior_project\\python_client_spgl\\proof_of_concept\\notes.txt"
	filename = expandPathname(filename)
	print "expandPathname2 -- should have \\ on windows / on posix"
	print "\t" + filename
	print ""
	
	filename = "notes.txt"
	file = openFile(filename)
	if(file != None):
		print "openFile1 -- should output first line"
		print "\t" + file.readline()
		print ""
		file.close()
	
	filename = "/Users/Alex/Documents/Stanford/senior_project/python_client_spgl/proof_of_concept/notes.txt"
	file = openFile(filename)
	if(file != None):
		print "openFile2 -- should output first line"
		print "\t" + file.readline()
		print ""
		file.close()
		
	filename = "C:/Users/Alex/Documents/Stanford/senior_project/python_client_spgl/proof_of_concept/notes.txt"
	file = openFile(filename)
	if(file != None):
		print "openFile3 -- should output first line"
		print "\t" + file.readline()
		print ""
		file.close()
	
	file = promptUserForFile("Enter file name: ")
	if(file != None): 
		print "promptUserForFile -- should output first line"
		print "\t" + file.readline()
		print ""
		file.close()
		
	file = openFile(filename)
	lines = readEntireFile(file)
	if(lines != None and len(lines) > 0):
		print "readEntireFile -- should output first line"
		print "\t" + lines[0]
		print ""
	file.close()
		
	file = openFileDialog(title = "Open", mode = "load", path="/Users/Alex/Documents/Stanford/senior_project/python_client_spgl/proof_of_concept/")
	if(file != None):
		print "openFileDialog -- should output first line"
		print "\t" + file.readline()
		print ""
		file.close()
		
	filename = "/this/is/a/path.txt"
	print "getRoot -- should print everything before ."
	print getRoot(filename)
	print ""
	
	filename = "/this/is/a/path.txt"
	print "getExtension -- should print everything after ."
	print getExtension(filename)
	print ""
		
	filename = "/this/is/a/path.txt"
	print "getHead -- should print everything before final / or \\"
	print getHead(filename)
	print ""
	
	filename = "/this/is/a/path.txt"
	print "getTail -- should print everything after final / or \\"
	print getTail(filename)
	print ""
		
	path = raw_input("New path name: ")
	createDirectoryPath(path)
	print "createDirectoryPath: PASS"
	print ""
	