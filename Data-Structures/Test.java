import java.util.*;

public class Test {

    public static void main(String[] args) {
        AdjacencyMatrix<Integer> tmp = new AdjacencyMatrix<Integer>(7);
        tmp.addEdge(4, 1);
        tmp.addEdge(1, 2);
        tmp.addEdge(2, 3);
        tmp.addEdge(3, 1);
        tmp.addEdge(5, null);
        tmp.addEdge(6, 7);
        LinkedList<Integer> sort = tmp.topologicalSort();
        for(Integer i : sort) {
            System.out.println(i);
        }
    }

}
