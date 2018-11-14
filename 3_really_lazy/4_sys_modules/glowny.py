import sys

print("Number of modules: {}".format(len(sys.modules)))
print(sys.modules)
print()

print("module1 in sys.modules: {}".format('module1' in sys.modules))
import module1
print("module1 in sys.modules: {}".format('module1' in sys.modules))
