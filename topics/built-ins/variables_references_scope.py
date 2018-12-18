from functools import reduce
import sys

test_int = reduce(lambda ac, cr: ac + cr, (1, 2, 3, 4), 0)


def test_func():
	return None


class TestClass:
	class_var1 = 'class var'

	def __init__(self):
		self.instance_var1 = 1


# Returns a list of names in current local scope or a list of object attributes
print(f'dir():\n{dir()}\n')

# Returns a dictionary representing the current [global symbol table]
print(f'globals():\n{globals()}\n')

# Updates and returns a dictionary representing current [local symbol table]
print(f'locals():\n{locals()}\n')

# Returns __dict__ attribute for a module, class, or object
print(f'vars():\n{vars()}\n')

# Returns the identity of an object
print(f'id(5):\n{id(5)}\n')

print(f'dir(TestClass):\n{dir(TestClass)}\n')
print(f'vars(TestClass):\n{vars(TestClass)}\n')
