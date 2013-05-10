'''
This file exports functions for generating pseudorandom numbers.
'''
import random

__INITIALIZED__ = False #: Flag to check if seeded

def initRandomSeed():
	'''
	Internal function
	'''
	global __INITIALIZED__
	if(__INITIALIZED__ == False):
		random.seed()
		__INITIALIZED__ = True
		
def randomInteger(low, high):
	'''
	Returns a random integer in the range low to
	high, inclusive.
	
	@type low: int
	@param low: lower bound
	@type high: int
	@param high: upper bound
	@rtype: int
	'''
	initRandomSeed()
	return random.randint(low, high-1)
	
def randomReal(low, high):
	'''
	Returns a random real number in the half-open interval
	[low&nbsp;..&nbsp;high).  A half-open
	interval includes the first endpoint but not the second, which
	means that the result is always greater than or equal to
	low but strictly less than high.
	
	@type low: float
	@param low: lower bound
	@type high: float
	@param high: upper bound
	@rtype: float
	'''
	initRandomSeed()
	return random.uniform(low, high)
	
def randomChance(p):
	'''
	Returns true with the probability indicated by p.
	The argument p must be a floating-point number between
	0 (never) and 1 (always).  For example, calling
	randomChance(.30) returns true 30 percent
	of the time.
	
	@type p: float
	@param p: percent chance of being true
	@rtype: boolean
	'''
	initRandomSeed()
	return (randomReal(0,1) < p)
	
def setRandomSeed(seed):
	'''
	Sets the internal random number seed to the specified value.  You
	can use this function to set a specific starting point for the
	pseudorandom sequence or to ensure that program behavior is
	repeatable during the debugging phase.
	
	@type seed: Hashable
	@param seed: seed value
	@rtype: void
	'''
	initRandomSeed()
	random.seed(seed)
		