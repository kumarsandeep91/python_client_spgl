# Taken from Stack Overflow: What's the best way to implement an 'enum' in Python?
# Link: http://stackoverflow.com/questions/36932/whats-the-best-way-to-implement-an-enum-in-python
'''
Defines a method for creating enumerations
'''

def enum(*sequential, **named):
	'''
	Creates an enum object where the sequential parameters are enumerated according
	to their position, i.e. the first argument has enumerated value 0, etc., and
	named arguments are enumerated explicitly according to the passed in value
	
	@param sequential: positional arguments, ex. enum('ZERO', 'ONE', 'TWO')
	@param named: keyword arguments, ex. enum(ONE = 1, TWO = 2, THREE = 3)
	@rtype: Enum
	'''
	enums = dict(zip(sequential, range(len(sequential))), **named)
	reverse = dict((value, key) for key, value in enums.iteritems())
	enums['reverse_mapping'] = reverse
	return type('Enum', (), enums)

if __name__ == '__main__':
	print
	print "Testing enum.py"
	print 
	print "--------------------------------------------------"
	print 
	
	print "Basic enum test"
	a = enum(a = 1, B = "2", c = 3.0)
	if(a.a != 1 or a.B != "2" or a.c != 3.0):
		print "FAILED"
		print "Expected:"
		print "a = 1, B = 2, c = 3.0"
		print "Actual:"
		print "a = " + str(a.a) + ", B = " + a.B + ", c = " + a.c
	else:
		print "PASSED"