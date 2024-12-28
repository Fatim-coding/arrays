import array as arr

# create an arrary
array_num = arr.array('i', [1,2,3,5,3,7,9,3])
print("Original array: "+str(array_num))

# count number of occurences
print("Numbernof occurences of the number 3 in the said arrray: "+str(array_num.count(3)))

# reveres the arrray
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))