import time
import subprocess

process = subprocess.Popen(['python', 'example_child.py'], shell=false, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
for i in range(5):
	process.stdin.write('%d