public class Node<T> {

    // Traditional node components
    private T data;
    private Node<T>[] edges;

    // DFS specific components
    int start_time;
    int finish_time;

    /**
     * Constructor
     *
     * @data: Data contained in node.
    */
    public Node(T data) {
        this.data = data;
        this.start_time = -1;
        this.finish_time = -1;
    }
    
}

public class Graph<T> {

    private ArrayList<Node<T>> roots;

    public Graph() {
        this.roots = new ArrayList<>();
    }

    private int topologicalSort(Node<T> root, int time, LinkedList<Node<T>> order) {
        if(root.start_time != -1) {
            root.start_time = time;
            for(Node<T> edge : root.edges) {
                time = topologicalSort(edge, time + 1, order);
            }
            root.finish_time = time;
            order.addFirst(root);
        }
        return time;
    }

    public LinkedList<Node<T>> topologicalSort() {
        int time = 0;
        LinkedList<Node<T>> order = new LinkedList<>();
        for(Node root : this.roots) {
            time = topologicalSort(root, time + 1, order);
        }
        return order;
    }

}
