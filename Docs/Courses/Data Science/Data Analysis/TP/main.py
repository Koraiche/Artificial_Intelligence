##LIBRARY
import geometry
car = geometry.carre(4)
tri = geometry.triangle(3, 6, 5)

print(geometry.pi) # -> 3.14159265359

geometry.aire(car) # -> 16

import geometry as geo # on peut maintenant accéder à geo.aire() ou geo.pi
print(geo.pi) # -> 3.14159265359

from geometry import pi
print(pi) # -> 3.14159265359

from geometry import *
print(phi)
##PACKAGE
from geometry2.variables import *
print(pi2)
import geometry2 as g2
print(g2.variables.pi2)
import geometry2.classes
