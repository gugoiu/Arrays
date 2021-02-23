# Arrays - Updating Elements
# importing "array" for array creation
import array
# Create an array of 5 integers
a = array.array('i', [1, 2, 3,-1,-2]) 
#Create a list containing one integer, one floating number, and one string
l = [10,2.5,"Hello!"] 
#Create a string of 7 characters
s = "abcdefg"
#Change the second element (character)
a[2] = 10
l[2] = "World!"
s[2] = "B"		#Comment this line. Strings are immutable in Python
#Print the second element (character)
print("The second element of a is: ",a[1])
print("The second element of l is: ",l[1])
	print("The second character of s is: ",s[1])
