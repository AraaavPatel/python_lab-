import math
from random import randint, choice
import datetime as dt
from os.path import *

# 1. Import entire module
print("Square root of 16:", math.sqrt(16))
print("Pi value:", math.pi)

# 2. Import specific items from module
print("Random integer (1-10):", randint(1, 10))
print("Random choice:", choice(['apple', 'banana', 'cherry']))

# 3. Import with alias
current_time = dt.datetime.now()
print("Current time:", current_time)

# 4. Import all items (use carefully)
print("Basename of '/a/b/c.txt':", basename('/a/b/c.txt'))

# 5. Import from custom module (if it exists)
# from mymodule import my_function
# my_function()

# 6. Check module attributes
print("\nMath module contents:")
print([attr for attr in dir(math) if not attr.startswith('_')])

