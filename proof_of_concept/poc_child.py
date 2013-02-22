import sys

while True:
	input = sys.stdin.readline()
	sys.stdout.write('Received: %s' %input)
	sys.stdout.flush()