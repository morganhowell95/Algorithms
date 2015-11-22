/**
 * An implementation of chain hashing.
 *
 * For testing purposes, we expect objects to be
 * hashed to implement the Hashable interface defined
 * below and to define the hashing function returned.
*/
import java.util.*;

interface Hashable extends Comparable<Hashable> {
    public int hashValue();
}

public class ChainHashing<T extends Hashable> {

    // The ratio of elements in the array and size of the array
    private final double LOAD_FACTOR = 0.7;

    // An array of linked lists which will be
    // dynamically grown as the load factor increases
    private int size;
    private LinkedList<T>[] contents;

    /**
     * Constructor.
     *
     * Setup the array containing our hashed values.
    */
    public ChainHashing() {
        this(0);
    }

    @SuppressWarnings("unchecked")
    public ChainHashing(int init_cap) {
        this.size = 0;
        int capacity = (init_cap < 1) ? 10 : init_cap;
        contents = (LinkedList<T>[]) new LinkedList<?>[capacity];
    }

    /**
     * Hashing.
     *
     * Simple hash method returning the hash code of the
     * object being passed.
    */
    private int hashIndex(T value) {
        return (value.hashValue()) % contents.length;
    }

    /**
     * Containment.
     *
     * Checks if the given value exists in the hash table. Only
     * anticipate iterating through (size / contents.length) elements.
     *
     * @value: Key to be searching for
     *
     * Runtime: O(1)
    */
    public boolean containsKey(T value) {
        int key = hashIndex(value);
        if(contents[key] != null) {
            for(T tmp : contents[key]) {
                if(tmp.compareTo(value) == 0) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * Insertion.
     *
     * Given the hash code of the value we are trying to insert,
     * we place the value into our array. If a collision exists,
     * we add the element to the front of the linked list that
     * currently resides in the given slot.
     *
     * Runtime: Amortized O(1)
    */
    @SuppressWarnings("unchecked")
    public void insert(T value) {

        // If the new load factor reaches a certain threshold we
        // resize our array to again decrease the load factor and
        // maintain an amortized constant time
        //
        // Because keys are potentially hased based on the size of
        // the array, we must actually reinsert all elements back
        // into the array
        if((double) (size + 1) / contents.length > LOAD_FACTOR) {
            LinkedList<T>[] copy = contents;
            contents = (LinkedList<T>[]) new LinkedList<?>[contents.length * 2];
            for(int i = 0; i < copy.length; i++) {
                if(copy[i] != null) {
                    for(T tmp : copy[i]) {
                        insert(tmp);
                    }
                }
            }
        }

        // Insert into our array based on the hash value of the given object
        int key = hashIndex(value);
        if(contents[key] == null) {
            contents[key] = new LinkedList<T>();
        }
        contents[key].addFirst(value);
        size += 1;

    }

    /**
     * Deletion.
     *
     * Find key. If it exists, simply remove from the linked list.
     * We anticipate searching through only 0.5 * (size / content.length)
     * elements through the process.
     *
     * @value: The key to delete.
     *
     * Runtime: O(1)
    */
    public void delete(T value) {
        int key = hashIndex(value);
        if(contents[key] != null) {
            int i = 0;
            ListIterator<T> it = contents[key].listIterator();
            while(it.hasNext()) {
                T tmp = it.next();
                if(tmp.compareTo(value) == 0) {
                    contents[key].remove(i);
                    size -= 1;
                    break;
                } else {
                    i += 1;
                }
            }
        }
    }

    /**
     * Display.
     *
     * Convenience method for printing out the values stored in the hash table.
     *
     * Runtime: O(n)
    */
    public void display() {
        for(int i = 0; i < contents.length; i++) {
            System.out.print(i + ": ");
            if(contents[i] == null || contents[i].size() == 0) {
                System.out.println(" NIL");
            } else {
                ListIterator<T> it = contents[i].listIterator();
                for(int j = 0; j < contents[i].size() - 1; j++) {
                    T next = it.next();
                    System.out.format("%4s ->", next.toString());
                }
                System.out.format("%4s%n", it.next().toString());
            }
        }
    }

}
