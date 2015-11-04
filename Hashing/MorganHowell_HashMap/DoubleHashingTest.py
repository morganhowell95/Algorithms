'''
This script represents a tester for the double hashing table functionality. I would usually use an external library for testing, but as per request
I will use only primitive types and in-house functions
'''
#Assuming the script is within the same directory as the hash table file
import math
from DoubleHashing import DoubleHashingTable

#Declare hash tables with different sizes using the static factory method
hash_table1 = DoubleHashingTable.constructor(5)
hash_table2 = DoubleHashingTable.constructor(30)
hash_table3 = DoubleHashingTable.constructor(100)
hash_table4 = DoubleHashingTable.constructor(1000)

#Function used to help visualize table contents throughout scanning
values = lambda x: x.value if (x is not None and x is not True) else None

#Boolean to describe whether tests passed or failed
passed_tests = True

#Insert some values into our hash tables respectively
for i in range(0,5):
	string = str(i)
	resp = hash_table1.set(string, i)
	if(resp is False):
		passed_tests = False
		print "table1 could not be fully loaded on value: " + str(i)

for i in range(0,15):
	 string = str(i)
	 resp = hash_table2.set(string, i)
	 if(resp is False):
		passed_tests = False
		print "table2 could not be fully loaded on value: " + str(i)

for i in range(0,75):
	string = str(i)
	resp = hash_table3.set(string, i)
	if(resp is False):
		passed_tests = False
		print "table3 could not be fully loaded on value: " + str(i)

for i in range(0,700):
	string = str(i)
	resp = hash_table4.set(string, i)
	if(resp is False):
		passed_tests = False
		print "table4 could not be fully loaded on value: " + str(i)


#Testing the expected load factor of each table as a float value
t1_load = hash_table1.load() # 5/5 -> 1.0, after one deleted 4/5 -> 0.8
t2_load = hash_table2.load() # 15/30 -> 0.5, after one insert 16/30 -> 0.533333
t3_load = hash_table3.load() # 75/100 -> 0.75
t4_load = hash_table4.load() # 700/1000 -> 0.70, after one deleted 699/1000 -> 0.699

#Testing the current load factors before alteration
if(abs(t1_load - 1.0)>.0001):
	passed_tests = False
	print "table1 shows incorrect load factor calculation: " + str(t1_load)

if(abs(t2_load - 0.5)>.0001):
	passed_tests = False
	print "table2 shows incorrect load factor calculation: " + str(t2_load)

if(abs(t3_load - 0.75)>.0001):
	passed_tests = False
	print "table3 shows incorrect load factor calculation: " + str(t3_load)

if(abs(t4_load - .70)>.0001):
	passed_tests = False
	print "table4 shows incorrect load factor calculation: " + str(t4_load)

#Testing load factor calculations after the insertion/deletion of elements
hash_table1.delete("0")
hash_table2.set("hello there!",700)
hash_table4.delete("500")
t1_load = hash_table1.load() # 5/5 -> 1.0, after one deleted 4/5 -> 0.8
t2_load = hash_table2.load() # 15/30 -> 0.5, after one insert 16/30 -> 0.533333
t4_load = hash_table4.load() # 700/1000 -> 0.70, after one deleted 699/1000 -> 0.699

if(abs(t1_load - 0.8)>.0001):
	passed_tests = False
	print "table1 shows incorrect load factor calculation: " + str(t1_load)

if(abs(t2_load - 0.53333)>.0001):
	passed_tests = False
	print "table2 shows incorrect load factor calculation: " + str(t2_load)

if(abs(t4_load - .699)>.0001):
	passed_tests = False
	print "table4 shows incorrect load factor calculation: " + str(t4_load)


#Testing the set and get functionality of table 1
item_from_t1_retrieved = hash_table1.get("3")
item_deleted_from_t1 = hash_table1.delete("4")
item_deleted_retrieved_from_t1 = hash_table1.get("4")
item_set_in_t1 = hash_table1.set("hello there!", 700)
new_item_from_t1_retrieved = hash_table1.get("hello there!")

if(item_from_t1_retrieved != 3):
	passed_tests = False
	print "table1 failed to retrieve key: " + str(item_from_t1_retrieved)

if(item_deleted_from_t1 != 4):
	passed_tests = False
	print "table1 failed to delete key: " + str(item_deleted_from_t1)

if(item_deleted_retrieved_from_t1 != None):
	passed_tests = False
	print "table1 did not actually delete the key, but it ran a successful deletion: " + str(item_deleted_retrieved_from_t1)

if(item_set_in_t1 != True):
	passed_tests = False
	print "table1 failed on insertion: " + str(item_set_in_t1)

if(new_item_from_t1_retrieved != 700):
	passed_tests = False
	print "table1 never actually inserted value properly: " + str(new_item_from_t1_retrieved)


#Testing the set and get functionality of table 2
item_from_t2_retrieved = hash_table2.get("3")
item_deleted_from_t2 = hash_table2.delete("4")
item_deleted_retrieved_from_t2 = hash_table2.get("4")
item_set_in_t2 = hash_table2.set("hello there!", 700)
new_item_from_t2_retrieved = hash_table2.get("hello there!")

if(item_from_t2_retrieved != 3):
	passed_tests = False
	print "table2 failed to retrieve key: " + str(item_from_t2_retrieved)

if(item_deleted_from_t2 != 4):
	passed_tests = False
	print "table2 failed to delete key: " + str(item_deleted_from_t2)

if(item_deleted_retrieved_from_t2 != None):
	passed_tests = False
	print "table2 did not actually delete the key, but it ran a successful deletion: " + str(item_deleted_retrieved_from_t2)

if(item_set_in_t2 != True):
	passed_tests = False
	print "table2 failed on insertion: " + str(item_set_in_t2)

if(new_item_from_t2_retrieved != 700):
	passed_tests = False
	print "table2 never actually inserted value properly: " + str(new_item_from_t2_retrieved)


#Testing the set and get functionality of table 3
item_from_t3_retrieved = hash_table3.get("3")
item_deleted_from_t3 = hash_table3.delete("4")
item_deleted_retrieved_from_t3 = hash_table3.get("4")
item_set_in_t3 = hash_table3.set("hello there!", 700)
new_item_from_t3_retrieved = hash_table3.get("hello there!")

if(item_from_t3_retrieved != 3):
	passed_tests = False
	print "table3 failed to retrieve key: " + str(item_from_t3_retrieved)

if(item_deleted_from_t3 != 4):
	passed_tests = False
	print "table3 failed to delete key: " + str(item_deleted_from_t3)

if(item_deleted_retrieved_from_t3 != None):
	passed_tests = False
	print "table3 did not actually delete the key, but it ran a successful deletion: " + str(item_deleted_retrieved_from_t3)

if(item_set_in_t3 != True):
	passed_tests = False
	print "table3 failed on insertion: " + str(item_set_in_t3)

if(new_item_from_t3_retrieved != 700):
	passed_tests = False
	print "table1 never actually inserted value properly: " + str(new_item_from_t1_retrieved)



#Testing the set and get functionality of table 4
item_from_t4_retrieved = hash_table4.get("3")
item_deleted_from_t4 = hash_table4.delete("4")
item_deleted_retrieved_from_t4 = hash_table4.get("4")
item_set_in_t4 = hash_table4.set("hello there!", 700)
new_item_from_t4_retrieved = hash_table4.get("hello there!")

if(item_from_t4_retrieved != 3):
	passed_tests = False
	print "table4 failed to retrieve key: " + str(item_from_t4_retrieved)

if(item_deleted_from_t4 != 4):
	passed_tests = False
	print "table4 failed to delete key: " + str(item_deleted_from_t4)

if(item_deleted_retrieved_from_t4 != None):
	passed_tests = False
	print "table4 did not actually delete the key, but it ran a successful deletion: " + str(item_deleted_retrieved_from_t4)

if(item_set_in_t4 != True):
	passed_tests = False
	print "table4 failed on insertion: " + str(item_set_in_t4)

if(new_item_from_t4_retrieved != 700):
	passed_tests = False
	print "table4 never actually inserted value properly: " + str(new_item_from_t4_retrieved)



#Edge cases: some edge cases we can test include inserting a key that already exists, adding
#to a table when the table is already completely full, and deleting something that doesn't exist
#Since all these cases are independent of table size, it is sufficient to test it on one table

#Adding duplicate keys
hash_table1.set("3",700)
hash_table1.set("3",800)
hash_table1.set("3",-1000)

value_replaced = hash_table1.get("3")
if (value_replaced!=-1000):
	passed_tests = False
	print "when inserting a duplicate key value is not replaced"

#Adding more keys than the table can possible hold
for i in xrange(1000):
	string_key = "a-" + str(i)
	boolean_return = hash_table1.set(string_key,i)

if (boolean_return!=False):
	passed_tests = False
	print "The table added more keys than it can hold, your table is a liar because that's not possible"

#Deleting keys that don't exist
deleted_key_return = hash_table1.delete("RANDOM DELETE")
if(deleted_key_return!=None):
	passed_tests = False
	print "The table deleted something that doesn't exist"

#retrieving keys that don't exist
fetched_ghost_key = hash_table1.get("NEEDLE IN HAY STACK")
if(fetched_ghost_key!=None):
	passed_tests = False
	print "The table must be able to catch ghosts because it retrieved a key that doesn't exist"

if(passed_tests):
	print '---------------------------------------------------------'
	print '\n\n\nSUCCESS! The hash table is working properly.\n\n\n'
	print '---------------------------------------------------------'
else:
	print 'FAILED TEST CASES!'
	print '---------------------------------------------------------'




