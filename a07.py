# Reversing a String, List or Array
# importing "array" for array creation
import array
# create a sample string
s = "Hello World!"
# create a sample list
l = [0,2.5,"Hi!"] 
# create a sample array of 3 integers
a = array.array('i',[1,2,3])
# use .reverse() method to reverse the order in each sequence
s.reverse()	# Change this line to s = s[::-1] .reverse() does not work on strings
l.reverse()
a.reverse()
# print the sequences and observe the changes
print(s)
print(l)
for i in range(len(a)):
	print(a[i], end=" ")
