'''
Problem
Using only primitive types, implement a fixed-size hash map that associates string keys with arbitrary data object references (you don't need to copy the object). Your data structure should be optimized for algorithmic runtime and memory usage. You should not import any external libraries, and may not use primitive hash map or dictionary types in languages like Python or Ruby.

The solution should be delivered in one class (or your language's equivalent) that provides the following functions:

	constructor(size): return an instance of the class with pre-allocated space for the given number of objects.
	boolean set(key, value): stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
	get(key): return the value associated with the given key, or null if no value is set.
	delete(key): delete the value associated with the given key, returning the value on success or null if the key has no value.
	float load(): return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.
	If your language provides a built-in hashing function for strings (ex. `hashCode` in Java or `__hash__` in Python) you are welcome to use that. If not, you are welcome to do something naive, or use something you find online with proper attribution.

'''
import random

class CuckooHashMap:
	HASH1_SEED = None
	HASH2_SEED = None
	HASH1_F = None
	HASH2_F = None

	c_table_1 = None
	c_table_2 = None
	table_size = 0
	elements_inserted = 0
	elements_deleted = 0

	def __init__(self, table_size):
		self.table_size = table_size
		self.c_table_1 = [None] * table_size
		self.c_table_2 = [None] * table_size
		(self.HASH1_F, self.HASH2_F) = self.genHashFunctions()

	#Insert key/value pair into hash table and return boolean based off the success/failure of insertion
	def set(self, key, value):
		new_element = CuckooHashMap.Data(key, value)

		#since our hashmap is fixed, we must keep a list of shifted elements so that we can rollback our hashtables to their
		# original state in the case of an insertion failure
		inserted_elements = []
		#we will have tighter constraints and say kicking five elements out could be considered detection of an infinite loop
		#This suggestion was adapted from a homework solution I found online: https://www.ics.uci.edu/~eppstein/261/s13-hw2-answers.txt
		for i in range(0,10):
			table1_hashvalue = self.HASH1_F(key)
			element_occupied = self.c_table_1[table1_hashvalue]
			new_element.hashvalue = table1_hashvalue
			#attempt insertion into the first table, checking to see if element already occupies this spot
			if(not element_occupied):
				#self.c_table_1[table1_hashvalue] = new_element
				inserted_elements.append((1, new_element))
				table2_hashvalue = self.HASH2_F(element_occupied.key)
				new_element = CuckooHashMap.Data(element_occupied.key, element_occupied.value)
				element_occupied = self.c_table_2[table2_hashvalue]
				new_element.hashvalue = table2_hashvalue
				#if an element did occupy that spot we're going to kick it out and move it to the second table.
				#element occupied in the second table will be rehashed to the first, and this process will continue until either an infinite loop
				#was detected or the load factor is abnormally high.
				if(not element_occupied):
					#self.c_table_2[table2_hashvalue] = new_element
					inserted_elements.append((2, new_element))
					new_element=element_occupied

				else:
					self.c_table_2[table2_hashvalue] = new_element
					self.elements_inserted = self.elements_inserted+1
					submitInsertions(inserted_elements)
					return True

			else:
				self.c_table_1[table1_hashvalue] = new_element
				self.elements_inserted = self.elements_inserted+1
				submitInsertions(inserted_elements)
				return True

			#The instructions for the KPCB app specified the hashmap must be fixed, however in an actual implementation we would retrieve new hash
			#functions and call growTablesAndTransferContents() in O(n) effeciency 
			return False
	
	#If our insertions fails, we want to be able to roll back the insertions we made that pushed other elements. Thus instead of directly
	#changing our table as we insert, we keep track of which ones caused the push
	def submitInsertions(elements):
		for i in elements:
			element = i[1]
			if i[0] is 1:
				self.c_table_1[element.hashvalue] = element
			else:
				self.c_table_2[element.hashvalue] = element


	def get(self, key):

		#element is within the first hash table
		index = self.HASH1_F(key)
		element = self.c_table_1[index]
		if(element.key is key): return element.value

		#element is within the second hash table
		index = self.HASH2_F(key)
		element = self.c_table_2[index]
		if(element.key is key): return element.value

		#element does not exists with the Cuckoo hash schema
		return None

	def load(self):
		return self.elements_inserted/(2*self.table_size)

	#We can describe generated hash functions by a static class method which incorporate random seeds, calling this upon table creation and when tables face
	#abnormally high load factors
	def genHashFunctions(self):
		self.HASH1_SEED = random.randint(1,1000)
		self.HASH2_SEED = random.randint(1,1000)
		f1 = lambda key:((self.HASH1_SEED * (hash(key) % self.table_size))**2) % self.table_size
		f2 = lambda key:((self.HASH2_SEED  * (hash(key) % self.table_size))**2) % self.table_size
		return (f1, f2)

	#When we detect an infinite loop (i.e. 5 element kickouts) we must create new hash functions in constant time and
	#rehash existing elements to be appropriated into a bigger table size. A random seed is incorporated into the hash functions
	#in order to maximize the effeciency of pseudo-random key hashing equivalences. Please note the functions do incorporate python's native __hash__ function.
	def growTablesAndTransferContents(self):
		self.table_size

	#Static factory method that returns an instance of the class as specified

	@staticmethod
	def constructor(size):
		return CuckooHashMap(size)
	#A local (i.e. nested) class has been created to encapsulate arbitrary elements, as described in the KPCB Fellows outlines
	#Thus hashed keys and elements will be converted to this high level data storage, giving the flexibility of increased customization

	class Data:
		key = None
		value = None
		hashvalue = None

		def __init__(self, key, value):
			self.key = key
			self.value = value

