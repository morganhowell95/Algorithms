For the KPCB Fellows application I chose to implement a double hashing mechanism with the following public methods:


----------------------------
constructor(size): return an instance of the class with pre-allocated space for the given number of objects.

boolean set(key, value): stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.

get(key): return the value associated with the given key, or null if no value is set.
delete(key): delete the value associated with the given key, returning the value on success or null if the key has no value.

float load(): return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.

-------------------------------

The extensive test cases that are laid out in "DoubleHashingTest.py" show how to use the static factory method "constructor" to make several hash tables at once and begin filling them in appropriatley. I've included a brief asymptotic analysis of my solution at the top of "DoubleHashing.py".

This hash map relies soley on the primitive types and standard syntax of Python 2.7.10 No pip installs required!


**NOTE: all runnable command-line functions are given in "DoubleHashingTest.py" in a sequential fashion. 

If you would like to run all these modules/functions within an interpreter via the terminal. Run (within directory of zip file):

$ python
$ execfile("DoubleHashingTest.py")
$ from DoubleHashing import DoubleHashingTable

Thanks and enjoy the code! :)

-Morgan J. Howell