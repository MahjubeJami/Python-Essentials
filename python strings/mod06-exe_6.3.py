# Using a for loop through a string,
# count the number of internet addresses
# in the string below by using the split method.

import re
str = \
'''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''
# split the str by both " " and ;
list1 = re.split('\s|:', str)

print ("list is:", list1)  # print the list after spliting
count = 0
for c in list1:
    if c[:3] == "127" :
        count +=1
print("number of IPs:",count)
