'''
This file exports an enumerated type called Direction whose elements are the four
compass points: NORTH, SOUTH, EAST, and WEST.
'''
from enum import enum


Direction = enum(NORTH = 0, EAST = 1, SOUTH = 2, WEST = 3) #: This enumerated type is used to represent the four compass directions.

def leftFrom(dir):
	'''
	Returns the direction that is to the left of the argument.
	
	@type dir: Direction
	@rtype: Direction
	'''
	return (dir+3) % 4
	
def rightFrom(dir):
	'''
	Returns the direction that is to the right of the argument.
	
	@type dir: Direction
	@rtype: Direction
	'''
	return (dir+1) % 4
	
def opposite(dir):
	'''
	Returns the direction that is opposite to the argument.
	
	@type dir: Direction
	@rtype: Direction
	'''
	return (dir+2) % 4
	
def directionToString(dir):
	'''
	Returns the name of the direction as a string.
	
	@type dir: Direction
	@rtype: string
	'''
	if(dir == Direction.NORTH):
		return "NORTH"
	elif(dir == Direction.EAST):
		return "EAST"
	elif(dir == Direction.SOUTH):
		return "SOUTH"
	elif(dir == Direction.WEST):
		return "NORTH"
	else:
		return "???"
		
	