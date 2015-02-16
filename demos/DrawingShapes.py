#Demonstration of using draw commands to draw simple shapes using wghs.

from wghs import *

screenSize(400,400)
setBackgroundColour("white")

drawEllipse(200,200,350,350,"lightblue")

drawRect(100,100,200,200,"darkgreen", 3)

drawTriangle(150,150,180,150,165,180,"red") # left eye
drawTriangle(220,150,250,150,235,180,[255,100,50]) # right eye  # uses RGB for orange colour

drawPolygon([ (110,250) , (290,250) , (280,220), (120,220) ], "sienna" )  # note the pairs of points within the point list.



endWait()