import sys

print("Number of modules: {}".format(len(sys.modules)))
print(sys.modules)
print()

print("module1 in sys.modules: {}".format('module1' in sys.modules))
print("mod in sys.modules: {}".format('mod' in sys.modules))
import module1 as mod
print("module1 in sys.modules: {}".format('module1' in sys.modules))
print("mod in sys.modules: {}".format('mod' in sys.modules))
