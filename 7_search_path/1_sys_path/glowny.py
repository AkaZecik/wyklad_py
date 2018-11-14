import sys

for path in sys.path:
    print(path)

print()

try:
    import my_module
except ModuleNotFoundError:
    print("Module not found!")

print()

sys.path.append("./my_modules")
import my_module
my_module.my_method()
