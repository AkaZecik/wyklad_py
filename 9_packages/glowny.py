print("--- 1 ---")

import my_package

print("--- 2 ---")

import my_package.my_module
my_package.my_module.my_method()

print("--- 3 ---")

from my_package import my_module
my_module.my_method()

print("--- 4 ---")

from my_package.my_module import my_method
my_method()

print("--- 5 ---")

import my_package.my_subpackage1

print("--- 6 ---")

from my_package import shadowed
print(shadowed)

print("--- 7 ---")

from my_package.my_subpackage2 import *
A.a()
C.c()

try:
    B.b()
except NameError:
    print("Package B was not imported!")
