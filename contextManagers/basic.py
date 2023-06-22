

# context starts with keyword 'with' and all the line within run under same context.
# Below will take care of exception handles as well.
with open("abc.txt", 'w') as f:
	f.write("hi there");

# class object can also be used as contextManagers. Class need to satisfy __enter__
# and __exit__ funtions to be uses a context. See below.

class ManagedFiles:
	def __init__(self, filename):
		print('init')
		self.filename = filename

	def __enter__(self):
		print('enter')
		self.f = open(self.filename, 'w')
		return self.f

	def __exit__(self, exc_type, exc_value, exc_traceback):
		if self.f:
			self.f.close()
		if exc_type is not None:
			print(f'exception caught {exc_type}')
			#handle exception here
			print('exception handled')
		print('exit')
		return True

with ManagedFiles('abc.txt') as file:
	print('do some stuff')
	file.write('With class context')
	file.someMethod() # this will raise exception

print('continue')
