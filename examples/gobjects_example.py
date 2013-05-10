from spgl import gwindow
from spgl import gtypes
from spgl import gobjects
from spgl import gsounds
from spgl import filelib

raw_input("\nPress enter to start graphics program\n")

window = gwindow.GWindow()

raw_input("\nPress enter to continue\n")

rect = gobjects.GRect(45,54,10,10)
window.add(rect)

raw_input("\nPress enter to continue\n")

rect.setFilled(True)

raw_input("\nPress enter to continue\n")

rect.move(100,100)

raw_input("\nPress enter to continue\n")

rect.setLocation(x=0,y=0)

raw_input("\nPress enter to continue\n")

rect.setColor(color = "RED")

raw_input("\nPress enter to continue\n")

rect.setColor(rgb = 0x00ff00)

raw_input("\nPress enter to continue\n")

rect.setVisible(False)

raw_input("\nPress enter to continue\n")

rect.setVisible(True)

raw_input("\nPress enter to continue\n")

window.repaint()

raw_input("\nPress enter to continue\n")

window.clear()

raw_input("\nPress enter to continue\n")

window.add(rect)
rect2 = gobjects.GRect(10, 10)
gcomp = gobjects.GCompound()
gcomp.add(rect)
gcomp.add(rect2)
window.add(gcomp, 50, 50)

raw_input("\nPress enter to continue\n")

gcomp.remove(rect2)

raw_input("\nPress enter to continue\n")

gcomp.add(rect2)

raw_input("\nPress enter to continue\n")

gcomp.sendForward(rect)

raw_input("\nPress enter to continue\n")

gcomp.sendBackward(rect)

raw_input("\nPress enter to continue\n")

gcomp.sendToFront(rect)

raw_input("\nPress enter to continue\n")

gcomp.sendToBack(rect)

raw_input("\nPress enter to continue\n")

gcomp.removeAll()

raw_input("\nPress enter to continue\n")

round = gobjects.GRoundRect(30, 30, 50, 50)
window.add(round)

raw_input("\nPress enter to continue\n")

window.remove(round)
rect3d = gobjects.G3DRect(30, 30, 50, 50, True)
rect3d.setFilled(True)
window.add(rect3d)

raw_input("\nPress enter to continue\n")

rect3d.setRaised(False)

raw_input("\nPress enter to continue\n")

window.remove(rect3d)
oval = gobjects.GOval(20, 40, 50, 50)
window.add(oval)

raw_input("\nPress enter to continue\n")

oval.setSize(40, 20)

raw_input("\nPress enter to continue\n")

oval.setFilled(True)
oval.setFillColor(rgb = 0x30c290)

raw_input("\nPress enter to continue\n")

window.remove(oval)
arc = gobjects.GArc(50, 20, 30, 225, 50, 50)
window.add(arc)

raw_input("\nPress enter to continue\n")

arc.setStartAngle(0)

raw_input("\nPress enter to continue\n")

arc.setSweepAngle(90)

raw_input("\nPress enter to continue\n")

arc.setFilled(True)
arc.setFillColor(rgb = 0xffff00)

raw_input("\nPress enter to continue\n")

window.remove(arc)
line = gobjects.GLine(0,0,50,50)
window.add(line)

raw_input("\nPress enter to continue\n")

line.setStartPoint(150,150)

raw_input("\nPress enter to continue\n")

line.setEndPoint(0,0)

raw_input("\nPress enter to continue\n")

window.remove(line)
image = gobjects.GImage("python.jpg")
window.add(image)

raw_input("\nPress enter to continue\n")

image.scale(sf = 3)

raw_input("\nPress enter to continue\n")

window.remove(image)
label = gobjects.GLabel("This is the Python client with a quote \\\"", 50, 50)
window.add(label)

raw_input("\nPress enter to continue\n")

label.setFont("Arial-30")

raw_input("\nPress enter to continue\n")

label.setLabel("Changing the label now")

raw_input("\nPress enter to continue\n")

window.remove(label)
poly = gobjects.GPolygon()
poly.addVertex(50, 50)
poly.addVertex(75, 25)
poly.addEdge(-20,100)
poly.addPolarEdge(15, 190)
window.add(poly)

raw_input("\nPress enter to continue\n")

poly.setFilled(True)
poly.setFillColor(rgb = 0xa01090)

raw_input("\nPress enter to continue\n")

window.remove(poly)

'''
raw_input("\nPress enter to continue\n")

s = sound.Sound("fireball.wav")raw_input("\nPress enter to continue\n")"/Users/Alex/Documents/Stanford/senior_project/python_client_spgl/proof_of_concept/mysound.mp3")

raw_input("\nPress enter to continue\n")

s.play()
'''

raw_input("\nPress enter to continue\n")

file = filelib.openFileDialog(title = "Open", mode = "load", path="/Users/Alex/Documents/Stanford/senior_project/python_client_spgl/proof_of_concept/")

raw_input("\nPress enter to continue\n")

window.remove(rect)

raw_input("\nPress enter to continue\n")

window.requestFocus()

raw_input("\nCompleted, press enter to close program")

window.close()