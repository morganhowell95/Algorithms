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



#I chose to use a more basic hashing mechanism, double hashing, because of the cited constraint
#involving a fixed table size. Double hashing is an open addressed hashing scheme that
#optimizes runtime performance for nonstatic keys of fixed table size by using two
#hash function paired with an iterator to probe addresses. Asymptotic analysis
#of double hashing (including an expected number of probes) shows that worse case is related
#to load factor "a", as seen in the expression: theta(1/a*ln(1/(1-a))).

#AUTHOR: MORGAN J. HOWELL
#DATE: 10/11/2015

import random
import math
class DoubleHashingTable:

	hash_table = []
	table_size = 0
	hash_f1 = None
	hash_f2 = None
	values_stored = 0

	#Initialize an empty hash table full of null slots
	def __init__(self,size):
		self.hash_table = [None] * size
		self.table_size = size
	
	def set(self, key, value):
		#Upon initial storage, the hash functions are generated 
		if(self.isEmpty()): (self.hash_f1, self.hash_f2) = DoubleHashingTable.genHashFunctions(self.table_size)
		#Double hashing will work up until the table is completely full, so if load factor is 1 we should report an insert failure
		if(int(math.floor(self.load())) is 1.0): return False
		
		#Instantiating the wrapper that creates arbitrary data storage for our key, value pair
		new_hash_insert = self.Data(key, value)

		#Hashing our key against our first designated hash function
		hash_value_f1 = self.hash_f1(key)
		occupied_slot = self.hash_table[hash_value_f1]

		#If the slot we are hashing to is currently filled, we will implement probing via double hashing
		if(occupied_slot is not None and occupied_slot is not True):
			#Replace value of slot with same key with new value
			if(key == occupied_slot.key):
				new_hash_insert.hash_value = hash_value_f1
				self.hash_table[hash_value_f1] = new_hash_insert
				return True
			#Double hashing works by pairing an incrementing variable that is multiplied by a second hash function
			hashed = False
			attempt = 1
			while(not hashed):
				hash_value_f2 = (self.hash_f1(key) + (attempt+(attempt*self.hash_f2(key)) %(self.table_size-1))) % self.table_size
				occupied_slot = self.hash_table[hash_value_f2]
				if(occupied_slot is not None and occupied_slot is not True):
					if(key == occupied_slot.key):
						new_hash_insert.hash_value = hash_value_f2
						self.hash_table[hash_value_f2] = new_hash_insert
						return True
					attempt = attempt + 1
					#In the extremely unlikely event that we've probed the table more than M times, we report an insertion failure
					#This is extremely unlikely because with a larger load factor and high attempt number, our double hashing 
					#mechanism will converge to the behavior a normal linear probe because of the increment operator involved.
					if(attempt is self.table_size): return False
				else:
					new_hash_insert.hash_value = hash_value_f2
					self.hash_table[hash_value_f2] = new_hash_insert
					hashed = True
					self.values_stored = self.values_stored + 1
		else:
			#We insert the value if the spot is not occupied or deleted (deleted element signified by boolean)
			new_hash_insert.hash_value = hash_value_f1
			self.hash_table[hash_value_f1] = new_hash_insert
			self.values_stored = self.values_stored + 1
		
		#Return true upon successful insertion
		return True
		
	def get(self, key):
		#If our table is empty or we hash to an empty spot we can return null
		if(self.isEmpty()): return None
		hash_value_f1 = self.hash_f1(key)
		occupied_slot = self.hash_table[hash_value_f1]
		if(occupied_slot is None): return None

		#Check to make sure our desired element is not occupied
		if(occupied_slot is True or occupied_slot.key != key):
			#Double hashing works by pairing an incrementing variable that is multiplied by a second hash function
			hashed = False
			attempt = 1
			while(not hashed):
				hash_value_f2 = (self.hash_f1(key) + (attempt+(attempt*self.hash_f2(key))% (self.table_size-1))) % self.table_size
				occupied_slot = self.hash_table[hash_value_f2]
				if(occupied_slot is None): return None

				if(occupied_slot is True or occupied_slot.key != key):
					attempt = attempt + 1
					#In the extremely unlikely event that we've probed the table more than M times, we report an insertion failure
					#This is extremely unlikely because with a larger load factor and high attempt number, our double hashing 
					#mechanism will converge to the behavior a normal linear probe because of the increment operator involved.
					if(attempt is self.table_size): return None
				elif(occupied_slot.key == key):
					return occupied_slot.value

		elif(occupied_slot.key == key):
			return occupied_slot.value
		
		return None

	#Our implementation of delete is extremely similar to get. Ideally, we would want to resuse our "get" functionality within delete to avoid redundancy. However this
	#would involve introducing optional parameters (in the form of *args or **kwargs) which would break the requirement for using dictionary data structures and using the
	#signatures provided by KPCB.
	def delete(self, key):
		#If our table is empty or we hash to an empty spot we can return null
		if(self.isEmpty()): return None
		hash_value_f1 = self.hash_f1(key)
		occupied_slot = self.hash_table[hash_value_f1]
		if(occupied_slot is None): return None

		#Check to make sure our desired element is not occupied
		if(occupied_slot is True or occupied_slot.key != key):
			#Double hashing works by pairing an incrementing variable that is multiplied by a second hash function
			hashed = False
			attempt = 1
			while(not hashed):
				hash_value_f2 = (self.hash_f1(key) + (attempt+(attempt*self.hash_f2(key))% (self.table_size-1))) % self.table_size
				occupied_slot = self.hash_table[hash_value_f2]
				if(occupied_slot is None): return None

				if(occupied_slot is True or occupied_slot.key != key):
					attempt = attempt + 1
					if(attempt is self.table_size): return None
				elif(occupied_slot.key == key):
					self.hash_table[hash_value_f2] = True
					self.values_stored = self.values_stored - 1
					return occupied_slot.value

		elif(occupied_slot.key == key):
			self.hash_table[hash_value_f1] = True
			self.values_stored = self.values_stored - 1
			return occupied_slot.value
		
		return None
		
	#Load factor is defined by items in hash map divided by table size
	def load(self):
		return float(self.values_stored)/self.table_size

	#Returns true if no element has been inserted
	def isEmpty(self):
		return True if (self.values_stored is 0) else False
	
	#Static class method for generating new hash functions, random seeds are avoided within this implementation because we strive to have hash functions
	#that are as close as possible to coprime with the hashtable, so that we can achieve a load factor of 1 if necessary. However, in this case double hashing is
	#essentially linear probing
	@staticmethod
	def genHashFunctions(size):
		#Construct hash functions based off seed and table size, relies on standard builtin method __hash__()
		hash_f1 = lambda key: abs((hash(key))) % size
		hash_f2 = lambda key: abs((hash(key)))
		return (hash_f1, hash_f2)

	#Class factory method for generating new double hash j
	@staticmethod
	def constructor(size):
		return DoubleHashingTable(size)

	#Local class that represents the "arbitrary data" that we are wrapping our keys/values within
	class Data:
		key = None
		value = None
		data = None
		hash_value = None

		def __init__(self, key, value):
			self.key = key
			self.value = value
