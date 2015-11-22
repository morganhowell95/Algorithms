import java.util.*;
import java.lang.reflect.Array;

/**
 * Hashable Interface.
 *
 * Allows for generic hashing of objects by extending
 * the class. Note it is import to be able to compare
 * values to ensure if a match exists in the hash table.
*/
interface Hashable extends Comparable<Hashable> {
    public int hashKey();
}

/**
 * Abstract Probing Hash Table.
 *
 * The goal of this class is to allow custom subclasses
 * to define how the probing (in the general open addressing
 * scheme) should be approached.
*/
public abstract class ProbeHashing<T extends Hashable> {

    private Class<T> clazz;

    protected int size;
    protected T[] table;
    protected final double LOAD_FACTOR = 0.75;

    /**
     * Constructor.
     *
     * Create an array of the given table.
    */
    @SuppressWarnings("unchecked")
    public ProbeHashing(Class<T> clazz) {
        this.size = 0;
        this.clazz = clazz;
        table = (T[]) Array.newInstance(clazz, 10);
    }

    /**
     * Contains Key.
     *
     * Checks that the passed value exists in the table.
     *
     * Amortized Runtime: O(1)
    */
    public boolean containsKey(T value) {
        for(int i = 0; i < table.length; i++) {
            int key = probe(value, i);
            if(table[key] == null) {
                return false;
            } else if(value.compareTo(table[key]) == 0) {
                return true;
            }
        }
        return false;
    }

    /**
     * Insertion.
     *
     * We place an element into the array if possible, probing for
     * additional elements if a collision occurs.
     *
     * @key: Key to be inserted into table
     *
     * Amortized Runtime: O(1)
    */
    @SuppressWarnings("unchecked")
    public void insert(T key) {

        // Grow array if the contents grow too large. Must reinsert into
        // the array since probing uses the size of the table
        if((double) (size + 1) / table.length > LOAD_FACTOR) {
            T[] copy = table;
            table = (T[]) Array.newInstance(clazz, table.length * 2);
            for(int i = 0; i < copy.length; i++)  {
                if(copy[i] != null) {
                    insert(copy[i]);
                }
            }
        }

        // Place into the table if possible
        for(int i = 0; i < table.length; i++) {
            int index = probe(key, i);
            if(table[index] != null) {
                table[index] = key;
                break;
            }
        }

    }

    /**
     * Probing Method.
     *
     * Must declare how to continue probing if a collision occurs.
     * That is, each subsequent call should return a unique address
     * amongst the empty indices, and must iterate through all
     * indices if called m times (from 0 to m - 1).
     *
     * @offset: The ith time this method has been called, because
     *          of a collision.
    */
    abstract protected int probe(T key, int offset);


}
