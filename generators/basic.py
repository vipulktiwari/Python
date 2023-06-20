import sys

def myGenerator(limit):
	for i in range(limit):
		if i % 2 == 0:
			yield i

mg = myGenerator(10)

for i in mg:
	print(i)

# another way

gen = ( i for i in range(1000) if i % 2 == 0 )

# similar to list comprehension
li = [ i for i in range(1000) if i % 2 == 0 ]

# Generator takes very less memory hence useful in large data operations
print(sys.getsizeof(gen))

print(sys.getsizeof(li)) 
