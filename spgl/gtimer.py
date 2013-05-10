'''
This file defines the GTimer class, which implements a
general interval timer.
'''
import platform

# pause and deleteTimer exists in c++ platform but aren't ever called
__ID__ = 0 #: Next ID to use for a GTimerData object


class GTimerData():
	'''
	This type maintains a reference count to determine when it is
	possible to free the timer.
	'''
	def __init__(self):
		'''
		Initializes the timer data
		
		@rtype: void
		'''
		global __ID__
		self.ID = "GTimer-" + str(__ID__)
		__ID__ = __ID__ + 1

class GTimer():
	'''
	This class implements a simple interval timer that generates a
	GTimerEvent with a specified frequency.  Copying
	a GTimer object is legal and creates an object that
	refers to the same internal timer.
	'''
	
	def __init__(self, milliseconds = None, gtd = None, src = None):
		'''
		Creates a timer object that generates a GTimerEvent
		each time the specified number of milliseconds has elapsed.  No
		events are generated until the client calls start
		on the timer.  For more details on using timers, see the documentation
		for the GTimerEvent
		class.
		
		@type milliseconds: int
		@param milliseconds: interval for timer event, takes precedence over gtd and src
		@type gtd: GTimerData
		@param gtd: creates a GTimer with the same data as the given GTD, takes precedence over src
		@type src: GTimer
		@param src: creates a GTimer with the same data as the given GTimer
		@rtype: void
		'''
		if(milliseconds != None):
			self.gtd = GTimerData()
			platform.Platform().createTimer(self, milliseconds) #!!
		elif(gtd != None):
			self.gtd = gtd
		elif(src != None):
			self.gtd = src.gtd
			
	def __eq__(self, other):
		'''
		Defines equality for GTimers, namely that they have the same GTimerData ID
		
		@type other: GTimer
		@param other: object to compare with
		@rtype: boolean
		'''
		if(other == None): return False
		return self.gtd.ID == other.gtd.ID
	
	def __ne__(self, other):
		'''
		Defines inequality for GTimers, opposite of equality
		
		@type other: GTimer
		@param other: object to compare with
		@rtype: boolean
		'''
		return not(self == other)
		
	def start(self):
		'''
		Starts the timer.  A timer continues to generate timer events until it
		is stopped; to achieve the effect of a one-shot timer, the simplest
		approach is to call the stop method inside the event
		handler.
 
		@rtype: void
		'''
		platform.Platform().startTimer(self)
		
	def stop(self):
		'''
		Stops the timer so that it stops generating events until it is restarted.
		
		@rtype: void
		'''
		platform.Platform().stopTimer(self)
		
	