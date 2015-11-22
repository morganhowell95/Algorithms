package Trees;
/**
 * Functional implementation of an AVL tree.
 *
*/

import java.util.*;

class Node<T extends Comparable<T>> {
    public T data;
    public int height;
    public Node<T> left;
    public Node<T> right;
    public Node<T> parent;
    public Node(T data, Node<T> parent) {
        this.height = 1;
        this.data = data;
        this.parent = parent;
    }
}

public class AVLTree<T extends Comparable<T>> {

    private Node<T> root;

    // Constructor
    public AVLTree() {
        this.root = null;
    }

    /**
     * Checks if value exists in tree.
     *
     * @value: Value to search for
     *
     * Runtime: O(log(n))
    */
    public boolean containsKey(T value) {
        return containsKey(value, this.root);
    }

    private boolean containsKey(T value, Node<T> n) {
        if(n == null) {
            return false;
        } else if(value.compareTo(n.data) < 0) {
            return containsKey(value, n.left);
        } else if(value.compareTo(n.data) > 0) {
            return containsKey(value, n.right);
        } else {
            return true;
        }
    }

    /**
     * Places node into tree, performing any self-balancing necessary.
     *
     * During an insertion, if there is any unbalance, we apply rotations
     * to rebalance the tree.
     *
     * @value: The value of the new node to insert
     *
     * Runtime: O(log(n))
    */
    public void insert(T value) {
        this.root = insert(value, this.root, null);
    }

    private Node<T> insert(T value, Node<T> n, Node<T> p) {
        if(n == null) {
            return new Node<T>(value, p);
        } else if(value.compareTo(n.data) <= 0) {
            n.left = insert(value, n.left, n);
        } else if(value.compareTo(n.data) > 0) {
            n.right = insert(value, n.right, n);
        }

        n = rebalance(n, false);
        return n;
    }

    /**
     * Deletion methods.
     *
     * Follows the same deletion pattern as a binary tree but with
     * rebalancing occurring afterward (and propagating rotations
     * upward potentially).
    */
    public void delete(T value) {
        delete(value, this.root);
    }

    private void delete(T value, Node<T> n) {

        // Could not find value
        if(n == null) {
            return;

        // Continue searching
        } else if(value.compareTo(n.data) < 0) {
            delete(value, n.left);
            return;
        } else if(value.compareTo(n.data) > 0) {
            delete(value, n.right);
            return;

        // Single children nodes
        } else if(n.left == null) {
            transplant(n, n.right);
        } else if(n.right == null) {
            transplant(n, n.left);

        // Try to remove successor instead
        } else {

            // Find successor
            Node<T> current = n.right;
            while(current.left != null) {
                current = current.left;
            }

            // Switch contents over
            if(n.right != current) {
                transplant(current, current.right);
                current.right = n.right;
            }
            transplant(n, current);
            current.left = n.left;

        }

        rebalance(n, true);
    }

    /**
     * Transplant method.
     *
     * The following is a convenience method used to
     * transfer over the parents of the nodes in a correct
     * order.
    */
    private void transplant(Node<T> target, Node<T> replacement) {
        if(target.parent == null) {
            this.root = replacement;
        } else if(target.parent.left == target) {
            target.parent.left = replacement;
        } else {
            target.parent.right = replacement;
        }
        if(replacement != null) {
            replacement.parent = target.parent;
        }
    }

    /**
     * Rotation methods.
     *
     * The following apply rotations on the tree so as to maintain
     * as close of an equal balance as possible. When the heights
     * of a node's left/right trees are imbalanced, these are then
     * applied.
    */
    private Node<T> lrRotate(Node<T> A) {
        Node<T> B = A.left;
        Node<T> C = B.right;

        B.right = C.left;
        if(B.right != null) {
            B.right.parent = B;
        }

        C.left = B;
        A.left = C;
        B.parent = C;
        C.parent = A;

        readjustHeight(B);
        readjustHeight(C);
        readjustHeight(A);

        return A;
    }

    private Node<T> llRotate(Node<T> A) {
        Node<T> B = A.left;
        Node<T> C = B.left;

        A.left = B.right;
        if(A.left != null) {
            A.left.parent = A;
        }

        B.right = A;
        B.parent = A.parent;
        A.parent = B;

        readjustHeight(A);
        readjustHeight(B);

        return B;
    }

    private Node<T> rlRotate(Node<T> A) {
        Node<T> B = A.right;
        Node<T> C = B.left;

        B.left = C.right;
        if(B.left != null) {
            B.left.parent = B;
        }

        C.right = B;
        A.right = C;
        B.parent = C;
        C.parent = A;

        readjustHeight(B);
        readjustHeight(C);
        readjustHeight(A);

        return A;
    }

    private Node<T> rrRotate(Node<T> A) {
        Node<T> B = A.right;
        Node<T> C = B.right;

        A.right = B.left;
        if(A.right != null) {
            A.right.parent = A;
        }

        B.left = A;
        B.parent = A.parent;
        A.parent = B;

        readjustHeight(A);
        readjustHeight(B);

        return B;
    }

    /**
     * Convenience method for insertion/deletion.
     *
     * The following will apply rotations to the tree and
     * correct the heights of the nodes as insertions or
     * deletions are applied.
     *
     * Note during deletions, height rotations may need to
     * be applied repeatedly. As a result, we add an additional
     * flag to specify propagating upward.
     *
     * @n: The node to rebalance
     * @propagate: Whether to rebalance upward
     *
     * Runtime: O(1) or O(log(n))
    */
    private Node<T> rebalance(Node<T> n, boolean propagate) {
        if(n == null) {
            return null;
        }

        readjustHeight(n);

        // LL rotations
        if(height(n.left) - height(n.right) > 1) {
            if(height(n.left.right) > height(n.left.left)) {
                n = lrRotate(n);
            }
            n = llRotate(n);

        // RL rotations
        } else if(height(n.right) - height(n.left) > 1) {
            if(height(n.right.left) > height(n.right.right)) {
                n = rlRotate(n);
            }
            n = rrRotate(n);
        }

        return n;
    }

    /**
     * Convenience method for modifying height of node.
     *
     * The following is a utility function that corrects the
     * height of a node.
     *
     * @n: The node to readjust
     *
     * Runtime: O(1)
    */
    private void readjustHeight(Node<T> n) {
        n.height = Math.max(height(n.left), height(n.right)) + 1;
    }

    /**
     * Convenience method for finding height of a node.
     *
     * Though the heights are recorded into the nodes, it is convenient
     * to have a separate function in the case of nulls.
     *
     * @n: The node to determine height of.
     *
     * Runtime: O(1)
    */
    private int height(Node<T> n) {
        return (n == null) ? 0 : n.height;
    }

    /**
     * Convenience function for printing tree.
     *
     * The following displays the values of the tree
     * in order.
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
