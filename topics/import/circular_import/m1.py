print(f' > Entering Module [{__name__}]')


def func1():
	print(f'   [{__name__}] Running Function')


print(f' * [{__name__}] Import Start')
from m2 import func2
print(f' * [{__name__}] Import Finished')


func1()
func2()

print(f' < Exiting Module [{__name__}]\n')
