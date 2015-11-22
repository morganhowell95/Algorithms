import java.util.HashMap;

/**
 * Disjoint Set implementation.
 *
 * Assumes that all elements in each tree are completely disjoint.
 * Implements rank and path compression optimizations.
*/
public class DisjointSet<T> {

    private class Node<T> {
        public int rank;
        public T parent;
        public Node(int rank, T parent) {
            this.rank = rank;
            this.parent = parent;
        }
    }

    private HashMap<T, Node<T>> table;

    /**
     * Constructor.
     *
    */
    public DisjointSet() {
        this.table = new HashMap<T, Node<T>>();
    }

    /**
     * Creates New Set.
     *
     * Creates a new set and adds it to the forest of
     * disjoint sets. We ensure the object does not
     * exist in the set.
    */
    public void createSet(T value) {
        table.put(value, new Node<T>(0, value));
    }

    /**
     * Finds representative.
     *
     * Finds the set of a given value and returns the
     * representative of this element, performing path
     * compression as the search continues.
    */
    public T findSet(T value) {
        Node<T> key = table.get(value);
        if(key == null) {
            return null;
        } else if(key.parent != value) {
            key.parent = findSet(key.parent);
        }
        return key.parent;
    }


    /**
     * Joins two sets together.
     *
     * Works by determining the rank of a given node
     * and joining based on the rank.
    */
    public void union(T a, T b) {
        Node<T> a_key = table.get(a);
        Node<T> b_key = table.get(b);
        if(a_key != null && b_key != null) {
            if(a_key.rank < b_key.rank) {
                a_key.parent = b;
            } else {
                b_key.parent = a;
                if(a_key.rank == b_key.rank) {
                    a_key.rank++;
                }
            }
        }
    }

}
