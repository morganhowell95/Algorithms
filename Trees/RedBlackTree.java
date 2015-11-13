package Trees;
/**
 * Functional implementation of a red-black tree.
 *
 * Has the following properties:
 * 1) Every node is either red or black.
 * 2) The root is black.
 * 3) Every leaf (NULL) is black.
 * 4) If a node is red, then both its children are black.
 * 5) All simple paths from node to descendant leaves contain
 *    the same number of black nodes.
*/

import java.util.*;

class Node<T extends Comparable<T>> {
    public T data;
    public boolean black;
    public Node<T> left;
    public Node<T> right;
    public Node<T> parent;
    public Node(T data, boolean black) {
        this.data = data;
        this.black = black;
    }
}

public class RedBlackTree<T extends Comparable<T>> {



}
