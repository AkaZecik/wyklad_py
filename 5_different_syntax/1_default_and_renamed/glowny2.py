import modul as md1
import modul as md2

print(md1.var1)
print(md2._var2)
print(md1.__var3)
print(md2.___var4)

print()

print(md1.method1)
print(md2._method2)
print(md1.__method3)
print(md2.___method4)

print()

print(md1.Class1)
print(md2._Class2)
print(md1.__Class3)
print(md2.___Class4)

print()

try:
    modul.var1
except NameError:
    print("Cannot do that!")

