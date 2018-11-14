import modul as md

print(md.var1)
print(md._var2)
print(md.__var3)
print(md.___var4)

print()

print(md.method1)
print(md._method2)
print(md.__method3)
print(md.___method4)

print()

print(md.Class1)
print(md._Class2)
print(md.__Class3)
print(md.___Class4)

print()

try:
    modul.var1
except NameError:
    print("Cannot do that!")

