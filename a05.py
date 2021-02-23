# Designing a Customized Length Function
# importing "array" for array creation
import array
# define the function my_len() that takes a string and returns the number of characters in that string
def my_len(s):
	n = 0
	for c in s:
    	n = n + 1
	return n
# create a sample string
s1 = "Hello World!"
# find the length of the string by using my_len() function
l1 = my_len(s1)
# print the length
print(l1)
# create a sample list
l2 = [0,-5.4,"Hi!"] 
# print the length of the list
print(my_len(l2))
# create a sample array of 4 float numbers
a3 = array.array('f',[1.1,2.2,3.3,4.4])
# print the length of the array
print(my_len(a3))
# print the length of a string parameter
print(my_len("How many characters are here?"))
