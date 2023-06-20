
class CountCalls:
	def __init__(self, func):
		self.func = func
		self.count = 0

	def __call__(self, *args, **kwargs):
		self.count += 1
		print(f'This function is called {self.count} times')
		return self.func(*args, **kwargs)


@CountCalls
def Greet(name):
	print(f'Hi {name}')

Greet('Vipul')
Greet('Vipul')
