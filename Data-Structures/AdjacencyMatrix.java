import java.util.*;

public class AdjacencyMatrix<T> {

    private boolean[][] graph;
    private ArrayList<T> vertices;
    private HashMap<Integer, Integer> in_edges;

    /**
     * Constructor.
    */
    public AdjacencyMatrix(int vertexCount) {
        this.graph = new boolean[vertexCount][vertexCount];
        this.vertices = new ArrayList<T>(vertexCount);
        this.in_edges = new HashMap<Integer, Integer>();
    }

    /**
     * Add Edge.
     *
     * Join the two vertices together.
    */
    public void addEdge(T key, T value) {
        int key_index = 0, val_index = 0;

        if(key != null) {
            key_index = vertices.indexOf(key);
            if(key_index == -1) {
                vertices.add(key);
                key_index = vertices.size() - 1;
            }
        }

        if(value != null) {
            val_index = vertices.indexOf(value);
            if(val_index == -1) {
                vertices.add(value);
                val_index = vertices.size() - 1;
            }
            if(!in_edges.containsKey(val_index)) {
                in_edges.put(val_index, 0);
            }
            in_edges.put(val_index, in_edges.get(val_index) + 1);
        }

        if(key != null && value != null) {
            graph[key_index][val_index] = true;
        }
    }

    /**
     * Topological Sort.
     *
     * Performs DFS on the adjacency matrix.
    */
    public LinkedList<T> topologicalSort() {

        LinkedList<T> order = new LinkedList<T>();
        //LinkedList<Integer> queue = new LinkedList<Integer>();
        boolean[] visited = new boolean[graph.length];

        for(int i = 0; i < graph.length; i++) {
            if(!in_edges.containsKey(i)) {
                //queue.add(i);
                //topologicalSortQ(queue, order, visited);
                topologicalSort(i, order, visited);
            }
        }

        return order;
    }

    private void topologicalSort(int index, LinkedList<T> order, boolean[] visited) {
        if(!visited[index]) {
            visited[index] = true;
            for(int i = 0; i < graph[index].length; i++) {
                if(graph[index][i]) {
                    topologicalSort(i, order, visited);
                }
            }
            order.addFirst(vertices.get(index));
        }
    }

    private void topologicalSortQ(LinkedList<Integer> queue, LinkedList<T> order, boolean[] visited) {
        while(!queue.isEmpty()) {
            int index = queue.pollFirst();
            if(!visited[index]) {
                visited[index] = true;
                for(int k = 0; k < graph[index].length; k++) {
                    if(graph[index][k]) {
                        queue.add(k);
                    }
                }
                order.add(vertices.get(index));
            }
        }
    }

}
