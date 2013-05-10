Author: Alex Valderrama
Title: Implementation of a Python Client for the Stanford Portable Graphics Library
Date: 5/10/2013

=====
Index
-----
I)		Background
II)		First Steps
III)	Client Design
IV) 	Results
V)		Additional Information

==================
I)		Background
------------------
The Stanford Portable Graphics Library (SPGL) is a graphical library designed for use
with introductory computer science courses. It is flexible, but powerful and provides
abstractions for events, threads, sounds, interactors (in the flavor of Java swing),
file processing, as well as graphics. However, the main innovation of the SPGL lies 
in its implementation design. 

One of the major problems for other graphical libraries is cross compatability across
platforms. In addition to the cost of maintenance on this code base, it becomes even
more difficult to provide support for the same library interface across mutiple
languages. This causes many graphical libraries to only support one language (Java,
C/C++, Python, etc.). 

The SPGL consists of a single Java Archive (JAR) file, spl.jar, which implements the 
entirety of the library as well as providing an interface for inter-process
communication to access these library commands. Because the SPGL is written in Java 
it is cross-platform compatible for any platform supported by Java. Since, the SPGL 
provides an interface by which another process can communicate commands, to draw,
access files, etc., the SPGL can be used with any language that allows for processes
to communicate. This includes older C based languages, more modern languages like
Python and Ruby, and potentially even functional languages like Haskell to work with
the SPGL.

In order to support a specific language a front-end client must be built for that
language to communicate with the Java backend. Although this is no small task, the
amount of work required to create a client that maintains minimal state and passes 
messages is dramatically smaller than the amount of work required to implement cross
platform compatible graphical routines. Hopefully this design will encourage the 
development of clients for many languages, giving teachers the option to use a 
friendly, well designed, graphical library in the language of their choice.

Currently, there exists clients in C, C++, and Java that were developed in
conjunction with the creation of the Java backend. This project is intended to show 
that a programmer, or programmers, can easily and quickly implement a front-end 
client (even in a langauge they have little experience with).

===================
II)		First Steps
-------------------
The primary goals I had for this project were to learn the Python programming
language and implement a client for the SPGL in Python. My main guide for learning 
Python was the tutorial Dive Into Python (DIP) (http://www.diveintopython.net/) as 
well as the online documentation for the language (http://docs.python.org/2/). Using 
the starter code provided by DIP I was able to obtain a solid understanding of the
design of Python as well as the basic data structures used in the language.

The next step was to understand how interprocess communication works in Python. I
decided to use popen instead of the subprocess module since popen provided more
flexibility not provided by the convenience functions in the subprocess module of 
the python language. I initially created a simple python program that passed strings 
from one process to another. After this, I extended the program to communicate with
a process running the Java backend. Upon succesfully opening a channel of 
communication I was able to draw an object on screen using the provided interface.

Before actually implementing the client, the final step of preparation was reading
through a reference implementation so I could understand the interface to the Java
backend. Reading through the C++ client it became apparent that some aspects of the
Python client would be easier, for example Python has great support for interactions
with the file system that C++ does not. However, there would also be some challenges,
like the fact that Python does not have method overloading nor static variables. 

=====================
III)	Client Design
---------------------
After becoming comfortable with the C++ reference implementation I began to design 
the Python version of the client. Like the C++ version, all the code that supports
inter-process communcation is located in one file, the remaining files describe the
interface the user programs interact with. 

Unlike the C++ version however the Python client maintains a reference to the Java
backend process within the Platform class, instead of as a global static variable. 
The Platform class contains a method for each interface command, as well as code for
processing and creating objects based on responses from the backend.

The remaining Python modules are straightforward in their design and do not differ 
much from the C++ reference. The class design maintains a fair amount of state to 
reduce the communication load between the client and backend. 

There were two major additional changes between the C++ and Python clients. First, as 
a modern language Python provides built in support for a number of actions that are
not supported in C++. For example, the C++ client has a number of data structures
like a hashmap and lexicon, a foreach statement implementation, as well as a simple
threading model that are all redundant due to the design of the Python language. Thus
I chose not to implement many of these features as I felt it would be better for 
students to utilize Python's built in versions.

The other major difference is that Python does not support method overloading, which 
causes overloaded C++ methods to be grouped together into a single method in the 
Python client. Python supports named/default arguments which provides the same
functionality as method overloading, however I had to take care to structure my 
methods to handle cases where more parameters were passed than necessary.

================
IV) 	Results
----------------

After completing my client I created a number of sample user programs to test the 
library's functionality. The program gobjects_example.py tests the majority of 
graphical objects that can be created as well as the methods they utilize. In
addition it does some testing of the file system implementation. The 
interactors_example.py tests the use of the Java-swing like interactors, as well as 
the gevents class. Finally, breakout_example tests a broad range of functionality
while allowing the user to play a fun game! While these programs demonstrate that
the library does provide the majority of the functionality the SPGL claims to support,
they are by no means a comprehensive testing suite. 

This is apparent in the sounds_example.py file which currently does not work. The 
program does pass messages correctly to the Java backend as compared to the C++ 
implementation, however at some point in the backend there is an error that prevents 
sound files from being opened. Whether this is some error with the Python client, the
backend or the platform (Windows 8) remains to be determined.

Additionally, on the subject of testing, while the example programs demonstrate good
functionality, and a number of the modules in the Python client have basic test
suites, testing is definitely an area that could benefit from future work as there 
are undoubtedly errors in my implementation.

In conclusion, the implemntation of a Python client for the SPGL was successful. 
Over the course of about 6 weeks I was able to go from having no experience with 
Python to creating a working client. Additionally, during the process I was able to 
find and fix a number of bugs within the C++ client. Hopefully this experience shows
that developing clients for the SPGL is nowhere near as difficult a task as 
implementing an entire graphics library in a new language.

==============================
V)		Additional Information
------------------------------

Source Code:
The source code for this project is available online at
(https://github.com/valderrama/python_client_spgl)
Written for Python 2.*

Documentation:
This project uses EPydoc to automatically generate HTML/PDF documentation of the
Python client. EPydoc is available at (http://epydoc.sourceforge.net/). A copy of
the HTML documentation is available on Github with the source code

Installation:
There are two options for using the Python client:
1) Copy all the files in the "python_client_spgl/spgl/" directory into your working 
directory and write your user program there
2) Install the library by going to the root directory "python_client_spgl/" and 
typeing the command "python setup.py install". Include a copy of "spl.jar" in your
working directory and write your user program there.




