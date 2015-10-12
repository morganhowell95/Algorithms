'''
This script represents a tester for the double hashing table functionality. I would usually use an external library for testing, but as per request
I will use only primitive types and in-house functions
'''
#Assuming the script is within the same directory as the hash table file
import math
from DoubleHashing import DoubleHashingTable

#declare hash tables with different sizes using the static factory method
hash_table1 = DoubleHashingTable.constructor(5)
hash_table2 = DoubleHashingTable.constructor(30)
hash_table3 = DoubleHashingTable.constructor(100)
hash_table4 = DoubleHashingTable.constructor(1000)

#function used to help visualize table contents throughout scanning
values = lambda x: x.value if (x is not None and x is not True) else None

#boolean to describe whether tests passed or failed
passed_tests = True

#insert some values into our hash tables respectively
for i in range(0,5):
    string = str(i)
    resp = hash_table1.set(string, i)
    if(resp is False):
    	passed_tests = False
    	print "table1 could not be fully loaded on value: " + str(i)

# for i in range(0,15):
#     string = str(i)
#     resp = hash_table2.set(string, i)

# for i in range(0,75):
#     string = str(i)
#     resp = hash_table3.set(string, i)

# for i in range(0,700):
#     string = str(i)
#     resp = hash_table4.set(string, i)











