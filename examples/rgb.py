
rgbHex = raw_input("enter color as hex integer (format #ffffff): ")
rgbHex = "0x" + rgbHex[1:]
rgbInt = int(rgbHex, base = 16)

print "rgbInt: " + str(rgbInt)
print "rgbHex: " + str(rgbHex)

r = rgbInt >> 16 & 0xFF
g = rgbInt >> 8 & 0xFF
b = rgbInt & 0xFF

print "r: " + str(r)
print "g: " + str(g)
print "b: " + str(b)

hexString = hex(rgbInt)
hexString = "#" + hexString[2:].upper()
print "making string from int: " + hexString 
