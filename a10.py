# Looping with zip
# creating a string with all vertexes
vertexes="ABC"
# creating a list with all x-coordinates
xcoords=[1,2,3]
# creating a list with all y-coordinates
ycoords=[-2,7,9]
# creating a list with all z-coordinates
zcoords=[-5,4,0]
# printing in the format P(x,y,z)
for vertex, x, y, z in zip(vertexes, xcoords, ycoords, zcoords):
	print("{}({},{},{})".format(vertex, x, y, z))
