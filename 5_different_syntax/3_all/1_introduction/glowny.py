from modul import *

for el in dir():
    print(el)

print()

try:
    modul.method1()
except NameError:
    print("Cannot do that!")

import sys
print("modul in sys.modules: {}".format('modul' in sys.modules))
