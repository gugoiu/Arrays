# Designing a Custumized Reverse Function
# importing "array" for array creation
import array
# importing "copy" for shallow copy
import copy
# define the function my_reverse() that takes a list or an array and returns all elements in reverse order
def my_reverse(s1):
	s2 = copy.copy(s1)
	for i in range(len(s1)):
    		s2[i] = s1[len(s1)-1-i]
	return s2
# create a sample list
l = [0,2.5,"Hi!"]
# reverse the list and print
l = my_reverse(l)
print(l)
# create sample array of 10 integers by using the range() function
a = array.array('i', range(10))
# reverse the array and print
a = my_reverse(a)
for i in range(len(a)):
	print(a[i], end=" ")
