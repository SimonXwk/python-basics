import sys

print('\n** Module Level')
frame_modlue = sys._getframe()
print(f'dir(_getframe()) :\n{dir(frame_modlue)}\n')
print(f'dir(_getframe().f_code) :\n{dir(frame_modlue.f_code)}\n')

print(f'_getframe().f_lineno : {frame_modlue.f_lineno}')
print(f'_getframe().f_code.co_filename : {frame_modlue.f_code.co_filename}')
print(f'_getframe().f_code.co_name : {frame_modlue.f_code.co_name}')
print(f'_getframe().f_code.co_firstlineno : {frame_modlue.f_code.co_firstlineno}')
print(f'_getframe().f_code.co_argcount : {frame_modlue.f_code.co_argcount}')
print(f'_getframe().f_code.co_varnames : {frame_modlue.f_code.co_varnames}')


def func(a=1):
	print('\n** Function Level')
	frame_func = sys._getframe()
	print(f'_getframe().f_lineno : {frame_func.f_lineno}')
	print(f'_getframe().f_code.co_filename : {frame_func.f_code.co_filename}')
	print(f'_getframe().f_code.co_name : {frame_func.f_code.co_name}')
	print(f'_getframe().f_code.co_firstlineno : {frame_func.f_code.co_firstlineno}')
	print(f'_getframe().f_code.co_argcount : {frame_func.f_code.co_argcount}')
	print(f'_getframe().f_code.co_varnames : {frame_func.f_code.co_varnames}')

	# By calling sys._getframe(1), you can get this information for the caller of the current function
	frame_caller = sys._getframe(1)
	print(f'Caller: {frame_caller.f_code.co_name}')
	return frame_caller.f_code.co_name


me = func()
