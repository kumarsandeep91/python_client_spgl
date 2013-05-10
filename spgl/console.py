'''
This file redirects the cin, cout,
and cerr channels to use a console window.  This file
must be included in the source file that contains the main
method, although it may be included in other source files as well.
'''

import platform

def clearConsole():
	'''
	Erases the contents of the console window.
	'''
	platform.Platform().clearConsole()
	
def setConsoleFont(font):
	'''
	Changes the font used for the console.  The font parameter
	is typically a string in the form family-style-size.
	In this string, family is the name of the font family;
	style is either missing (indicating a plain font) or one
	of the strings Bold, Italic, or
	BoldItalic; and size is an integer
	indicating the point size.  If any of these components is
	specified as an asterisk, the existing value is retained.
	The font parameter can also be a sequence of
	such specifications separated by semicolons, in which case the
	first available font on the system is used.
	
	@type font: string
	@param font: font definition
	'''
	platform.Platform().setConsoleFont(font)
	
def setConsoleSize(width, height):
	'''
	Changes the size of the console to the specified dimensions, measured
	in pixels.
	
	@type width: float
	@param width: console width
	@type height: float
	@param height: console height
	'''
	platform.Platform().setConsoleSize(width, height)