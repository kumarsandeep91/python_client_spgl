'''
Helper module with some string methods
'''
import string

__STRING_DELIMITERS__ = ",:)}]\n"

def stringNeedsQuoting(str):
	'''
	Checks whether the string needs quoting in order to be read correctly.
	
	@type str: string
	@param str: string to check
	@rtype: boolean
	'''
	n = len(str)
	for i in range(n):
		ch = str[i]
		if(ch.isspace()): return False
		if(__STRING_DELIMITERS__.find(ch) != -1): return True
	return False
	
def writeQuotedString(str, forceQuotes = False):
	'''
	Returns the string str surrounded by double quotes, converting
	special characters to escape sequences, as necessary.  If the optional
	parameter forceQuotes is explicitly set to false, quotes are included
	in the output only if necessary.
	
	@type str: string
	@type forceQuotes: boolean
	@rtype: string
	'''
	result = ""
	if(not(forceQuotes) and stringNeedsQuoting(str)): forceQuotes = True
	if(forceQuotes): result += "\""
	length = len(str)
	for i in range(length):
		ch = str[i]
		if(ch == "\a"): result += "\\a"
		elif(ch == "\b"): result += "\\b"
		elif(ch == "\f"): result += "\\f"
		elif(ch == "\n"): result += "\\n"
		elif(ch == "\r"): result += "\\r"
		elif(ch == "\t"): result += "\\t"
		elif(ch == "\v"): result += "\\v"
		elif(ch == "\""): result += "\\" + oct(ord(ch))
		elif(ch == "\\"): result += "\\\\"
		else:
			if(string.printable.find(ch) != -1):
				result += ch
			else:
				result += "\\" + oct(ord(ch))
	if(forceQuotes): result += "\""
	return result

if __name__ == '__main__':
	quoted = "\a\b\f\n\r\t\v\"\\abcdefghijklmnopqrstuvwxyz1234567890"
	print writeQuotedString(quoted)