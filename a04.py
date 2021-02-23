# Making copies of Lists and Arrays
# import module copy and module array
import copy
import array
# create a sample array
a1=array.array('i',[1,2,3])
# copy the array a1 into array a2 by using a shallow copy (no nested structures here)
a2=copy.copy(a1)
# change the firts elemnt of the array a1
a1[0]=-1
# print both arrays to observe the changes
print(a1)
print(a2)

