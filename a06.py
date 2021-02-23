# Creating an Arrays with Fibonacci Numbers
# importing "array" for array creation
import array
# create an array of 20 integers by using the range() function
a = array.array('i', range(20))
# updating elements starting with the third by using Fibonacci numbers property: f(n)=f(n-1)+f(n-2)
for i in range(2,len(a)):
	a[i] = a[i-2]+a[i-1]
# printing elements separated by a space character on a line
for i in range(len(a)):
	print(a[i], end=" ")
