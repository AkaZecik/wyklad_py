from modul import var
from modul import method
from modul import Class as Klass

print(var)
method()
Klass()

try:
    modul.method()
except NameError:
    print("Cannot do that!")

import sys
print("modul in sys.modules: {}".format('modul' in sys.modules))
