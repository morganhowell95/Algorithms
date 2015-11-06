'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Subscribe to see which companies asked this question
'''

#my idea is to create an open addressed hashing scheme
#each value is wrapped in a data object, where frequency of access is held
#if an item is being set and capacity is full, we remove item with least number of times accessed
#in the case two items have equal least number of accessed, we will delete the "younger" one
#thus we will keep two increment variables, the age of the data and the # of times accessed

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.items = 0
        self.table = [None] * capacity
        

    #open addressed linear probing, using default Python __hash__ method
    def get(self, key):
        """
        :rtype: int
        """
        hash_value = hash(key) % self.capacity
        found=False
        quit = false
        value=-1
        
        while not found and not quit:
            
            #if we bump into a slot that hasn't been set yet we know he key is not in the table
            if self.table[hash_value] is None:
                quit = True
            
            #if we've scanned the whole table quit
            elif linear_probe>= self.capacity:
                quit=True
                
            #we've found our item if it hashes to an existing key
            elif self.table[hash_value].key is key:
                #retreive value of key
                value = self.table[hash_value].value
                
                #reset life to most recently used
                self.table[hash_value].life = 0
                
                #increment other lives
                for i in self.table:
                    i.life+=1
                found = True
                
            else:
                linear_probe+=1
                hash_value = (hash(key) % self.capacity) + linear_probe
                
        return value
        
            
    def _remove(self, key):
                """
        :rtype: bool
        """
        hash_value = hash(key) % self.capacity
        found=False
        quit = false
        value=-1
        
        while not found and not quit:
            
            #if we bump into a slot that hasn't been set yet we know he key is not in the table
            if self.table[hash_value] is None:
                quit = True
            
            #if we've scanned the whole table quit
            elif linear_probe>= self.capacity:
                quit=True
                
            #we've found our item if it hashes to an existing key
            elif self.table[hash_value].key is key:
                self.table[hash_value]=None
                found=True
            else:
                linear_probe+=1
                hash_value = (hash(key) % self.capacity) + linear_probe
        return found
        
    def fetchLoadFactor(self):
        self.items/self.capacity
        
    def deleteLR(self):
        max_num = (-1, None)
        for slot in self.table:
            if(max_num[0] <= slot.life): max_num = (slot.life, slot.key)
        return max_num[1]

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if(self.fetchLoadFactor == 1):
            lru_slot = self.deleteLR()
            self._remove(lru_slot)
        
        new_obj = LRUCache.Data(key,value)
        hash_value = hash(key) % self.capacity
        linear_probe = 0
        inserted=False
        
        while not inserted:
            if self.table[hash_value] is None:
                self.table[hash_value] = new_obj
                inserted=True
            else:
                linear_probe+=1
                hash_value = (hash(key) % self.capacity) + linear_probe
                
        
    class Data:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.life = 0
            
