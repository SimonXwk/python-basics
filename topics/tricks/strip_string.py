import re

sample_string = ' This is a   String  to be tested On        '
print(f'Original String     : [{sample_string}]')

# Trim spaces from left
print(f'lstrip()            : [{sample_string.lstrip()}]')

# Trim spaces from right
print(f'rstrip()            : [{sample_string.rstrip()}]')

# Trim spaces from both sides
print(f'strip()             : [{sample_string.strip()}]')

# Remove spaces
print(f'replace(" ", "")    : [{sample_string.replace(" ", "")}]')

# Remove duplicate spaces
print(f're.sub(" +", "", s) : [{re.sub(" +", " ", sample_string)}]')

# Excel Trim() like function
print(f're.sub() + strip()  : [{re.sub(" +", " ", sample_string).strip()}]')
