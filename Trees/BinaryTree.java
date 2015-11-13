package Trees;

/**
 * The following is a complete implementation of a binary tree.
 *
 * The binary tree consists of an ordering of data such that
 * values can be found strategically by comparing the search key
 * by the values at the current node.
*/
import java.util.*;

class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left;
    public Node<T> right;
    public Node(T data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

public class BinaryTree<T extends Comparable<T>> {

    // Base of the tree; null if empty
    private Node<T> root;

    public BinaryTree() {
        this.root = null;
    }

    /**
     * Determines is the passed value is in the given tree
     * or not.
     *
     * @value: Value to text existence in
     *
     * Runtime: O(log(n))
    */
    public boolean containsKey(T value) {
        return containsKey(value, this.root);
    }

    private boolean containsKey(T value, Node<T> n) {
        if(n == null) {
            return false;
        } else if(value.compareTo(n.data) == 0) {
            return true;
        } else if(value.compareTo(n.data) < 0) {
            return containsKey(value, n.left);
        } else {
            return containsKey(value, n.right);
        }
    }

    /**
     * Insertion method.
     *
     * Insertions happen by comparing the inserted value by
     * the current node. If less than or equal to the current
     * value, we look to the left. Otherwise we look to the
     * right.
     *
     * @value: The data to be placed into the tree
     *
     * Runtime: O(log(n))
    */
    public void insert(T value) {
        this.root = insert(value, this.root);
    }

    private Node<T> insert(T value, Node<T> n) {
        if(n == null) {
            return new Node<T>(value);
        } else {
            if(value.compareTo(n.data) < 1) {
                n.left = insert(value, n.left);
            } else {
                n.right = insert(value, n.right);
            }
            return n;
        }
    }

    /**
     * Deletion methods.
     *
     * Deletions occur by finding the given value and then
     * readjusting the tree accordingly. This can be done
     * by finding the value of the tree and then finding
     * the next largest element in the tree.
     *
     * We must first find the element in question and then
     * find its successor.
     *
     * @value: The value to remove from the tree
     *
     * Runtime: O(log(n))
    */
    public void delete(T value) {
        delete(value, this.root, null);
    }

    private void delete(T value, Node<T> n, Node<T> parent) {

        // Value not found in tree; disregard call
        if(n == null) {
            return ;
        }

        // Recursively move further down the tree
        if(value.compareTo(n.data) < 0) {
            delete(value, n.left, n);
        } else if(value.compareTo(n.data) > 0) {
            delete(value, n.right, n);

        // Consider single child nodes
        } else if(n.left == null) {
            transplant(n, parent, n.right);
        } else if(n.right == null) {
            transplant(n, parent, n.left);

        // Find successor to replace current node
        } else {

            Node<T> c_parent = n;
            Node<T> current = n.right;
            while(current.left != null) {
                c_parent = current;
                current = current.left;
            }

            // Want to setup successor as the right child
            // Once this occurs, can transplant correctly
            if(current != n.right) {
                transplant(current, c_parent, current.right);
                current.right = n.right;
            }
            transplant(n, parent, current);
            current.left = n.left;
        }

    }

    /**
     * Transplant method.
     *
     * Utility method to replace a node with that of another
     * The replacement node's parent must be modified outside
     * of this function.
     *
     * @target: Node being replaced
     * @p_target: Parent of the node being replaced
     * @replacement: Node to use for replacement
     *
     * Runtime: O(1)
    */
    private void transplant(Node<T> target, Node<T> p_target, Node<T> replacement) {
        if(p_target == null) {
            this.root = replacement;
        } else if(p_target.left == target) {
            p_target.left = replacement;
        } else {
            p_target.right = replacement;
        }
    }

    /**
     * Convenience function for displaying.
     *
     * Runtime: O(n)
    */
    public void display() {
        display(this.root, 0, "-");
    }

    private void display(Node<T> n, int padding, String dir) {
        if(n != null) {
            System.out.print("|-");
            for(int i = 0; i < padding; i++) {
                System.out.print("-");
            }
            System.out.format(dir + "-%03d%n", n.data);
            display(n.left, padding + 8, "L");
            display(n.right, padding + 8, "R");
        }
    }

}

