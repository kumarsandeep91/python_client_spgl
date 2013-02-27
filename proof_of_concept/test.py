import gwindow
import gobjects



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

'''
requestFocus
clear
repaint
setVisible
'''

window.remove(rect)

raw_input("\nCompleted, press enter to close program")

window.close()