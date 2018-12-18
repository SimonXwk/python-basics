# Returns absolute value of a number
res = abs(-5.1)
print(f'* abs(-5.1) -> {res}  {type(res)}')

# Returns quotient and remainder of integer division
res = divmod(100, 33)
print(f'* divmod(100, 33) -> {res}  {type(res)}')

# Returns the largest of the given arguments or items in an iterable
res = max((-1, 3., 3))
print(f'* max((-1, 3., 3)) -> {res}  {type(res)}')

# Returns the smallest of the given arguments or items in an iterable
res = min([False, 0, 3, 5.6])
print(f'* min([ False, 0, 3, 5.6]) -> {res}  {type(res)}')

# Raises a number to a power
res = pow(2.38, 5)
print(f'* pow(2.38, 5) -> {res}  {type(res)}')

# Rounds a floating-point value
res = round(2.35, 1)
print(f'* round(2.35, 1) -> {res}  {type(res)}')

# Sums the items of an iterable, using generator as example
res = sum(x for x in range(1, 5))
print(f'* sum(x for x in range(1, 5)) -> {res}  {type(res)}')
