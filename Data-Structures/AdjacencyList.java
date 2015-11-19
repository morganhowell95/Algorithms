import java.util.HashSet;
import java.util.HashMap;
import java.util.LinkedList;

public class AdjacencyList<T> {

    private HashMap<T, Integer> in_edges;
    private HashMap<T, LinkedList<T>> graph;

    /**
     * Constructor
    */
    public AdjacencyList() {
        this.in_edges = new HashMap<T, Integer>();
        this.graph = new HashMap<T, LinkedList<T>>();
    }

    /**
     * Add Edge.
     *
     * Adds the edge onto the linked list representing
     * the edges coming from the given key.
    */
    public void addEdge(T key, T value) {
        if(key != null && !graph.containsKey(key)) {
            graph.put(key, new LinkedList<T>());
        }
        if(value != null) {
            if(!graph.containsKey(value)) {
                graph.put(value, new LinkedList<T>());
            }
            LinkedList<T> edges = graph.get(key);
            edges.addFirst(value);

            if(!in_edges.containsKey(value)) {
                in_edges.put(value, 0);
            }
            in_edges.put(value, in_edges.get(value) + 1);
        }
    }

    /**
     * Topological Sorting.
     *
     * A means of sorting the elements based on which elements come
     * along without any previous edges in the list.
    */
    public LinkedList<T> topologicalSort() {
        HashSet<T> seen = new HashSet<T>();
        LinkedList<T> order = new LinkedList<T>();
        //LinkedList<T> queue = new LinkedList<T>();
        for(T key : graph.keySet()) {
            if(in_edges.get(key) == null) {
                topologicalSort(key, order, seen);
                //queue.add(key);
                //topologicalSortQ(queue, order, seen);
            }
        }
        return order;
    }

    private void topologicalSort(T key, LinkedList<T> order, HashSet<T> seen) {
        if(!seen.contains(key)) {
            seen.add(key);
            LinkedList<T> edges = graph.get(key);
            if(edges != null) {
                for(T edge : edges) {
                    topologicalSort(edge, order, seen);
                }
            }
            order.addFirst(key);
        }
    }

    private void topologicalSortQ(LinkedList<T> queue, LinkedList<T> order, HashSet<T> seen) {
        while(!queue.isEmpty()) {
            T key = queue.pollFirst();
            if(!seen.contains(key)) {
                seen.add(key);
                LinkedList<T> edges = graph.get(key);
                if(edges != null) {
                    for(T edge : edges) {
                        queue.add(edge);
                    }
                }
                order.add(key);
            }
        }
    }

}
