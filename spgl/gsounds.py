'''
This file defines a class that represents a sound.
'''
import platform

__ID__ = 0 #: Next ID to use for a Sound object

class Sound():
	'''
	This class encapsulates a sound file.  The sound file is specified in the
	constructor and must be a file in either the current directory or a
	subdirectory named sounds.

	The following code, for example, plays the sound file ringtone.wav::

		Sound ringtone("ringtone.wav");
		ringtone.play();

	'''
	def __init__(self, filename):
		'''
		Creates a Sound object.  The default constructor
		creates an empty sound that cannot be played.  The second form
		initializes the sound by reading in the contents of the specified
		file.
		
		@type filename: string
		@param filename: sound file
		@rtype: void
		'''
		global __ID__
		self.filename = filename
		self.valid = True
		self.ID = "Sound-" + str(__ID__)
		__ID__ = __ID__ + 1
		platform.Platform().createSound(self, filename)
	
	def __del__(self):
		'''
		Informs the Java backend that the sound should be deleted
		
		@rtype: void
		'''
		platform.Platform().deleteSound(self)
	
	def play(self):
		'''
		Starts playing the sound.  This call returns immediately without waiting
		for the sound to finish.
		
		@rtype: void
		'''
		platform.Platform().playSound(self)