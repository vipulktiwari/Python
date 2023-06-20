import functools

def add_decorator(func):
	# functools.wraps reservs the function name for helper module
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		print('start')
		result = func(*args, **kwargs)
		print('end')
		return result
	return wrapper

@add_decorator
def add5(x):
	return x + 5

# To understand below statement is same as adding a wrapper to function
# add5 = add_decorator(add5)

result = add5(5)
#print(help(add5))
print(add5.__name__)
print(result)
