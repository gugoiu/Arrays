# Designing a Customized Print Function
# importing the 'array' module
import array
# defining a custumized print function
def my_print(s):
	for index, element in enumerate(s):
		print("The element at index = {} is: {}".format(index, element))
# creating a list
l = ["aa","b","ccc"]
# printing the list
my_print(l)
# creating a string
s = "Hello World!"
# printing the string
my_print(s)
# creating an array
a = array.array('i',[1,2,3])
# printing the array
my_print(a)
