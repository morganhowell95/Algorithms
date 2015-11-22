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

    // Used to maintain invariants
    public T data;
    public boolean black;

    // Tree structure
    public Node<T> left;
    public Node<T> right;
    public Node<T> parent;

    public Node(T data, boolean black, Node<T> parent) {
        this.data = data;
        this.black = black;
        this.left = null;
        this.right = null;
        this.parent = parent;
    }
}

public class RedBlackTree<T extends Comparable<T>> {

    private Node<T> root;

    /**
     * Constructor.
    */
    public RedBlackTree() {
        this.root = null;
    }

    /**
     * Insertion.
     *
     * Takes O(lg(n)) time. Must fixup the tree as each
     * insertion goes along to ensure all variants are
     * maintained.
    */
    public void insert(T value) {
        if(this.root == null) {
            this.root = new Node<T>(value, true, null);
        } else {
            // Find where to insert
            Node<T> parent = null;
            Node<T> current = this.root;
            while(current != null) {
                parent = current;
                if(value.compareTo(current.data) <= 0) {
                    current = current.left;
                } else {
                    current = current.right;
                }
            }

            // Insert accordingly
            Node<T> next = new Node<T>(value, false, parent);
            if(value.compareTo(parent.data) <= 0) {
                parent.left = next;
            } else {
                parent.right = next;
            }

            // Propagate fixes upward
            // Note this should only be called if the parent is
            // also red, as this violates invariant 3
            insert_fixup(next);
            this.root.black = true;
            while(this.root.parent != null) {
                this.root = this.root.parent;
            }
        }
    }

    /**
     * Insertion Fixup.
     *
     * Maintains all invariants of the given tree for balance purposes.
    */
    private void insert_fixup(Node<T> x) {
        if(x.parent != null && !x.parent.black) {

            // The parent is red, and so is this node, so the parent
            // must in turn have a parent which must be black
            Node<T> p = x.parent;
            Node<T> w = p.parent;

            // Uncle node. This determines how coloring occurs
            Node<T> y = (w.left == p) ? w.right : w.left;

            // Case 1: If the uncle is red, then we can just recolor
            // all nodes and propagate upward.
            if(y != null && !y.black) {
                p.black = true;
                y.black = true;
                w.black = false;
                insert_fixup(w);

            // Case 2/3: We must apply certain rotations and recolorings,
            // depending on the side each node is on. First we consider
            // when the parent is to the left of the grandparent.
            } else if(w.left == p) {
                if(x == p.right) {
                    lrRotate(w);
                }
                w.black = false;
                x.black = true;
                llRotate(w);

            // Next we handle the case on the right
            } else {
                if(x == p.left) {
                    rlRotate(w);
                }
                w.black = false;
                x.black = true;
                rrRotate(w);
            }

        }
    }

    /**
     * Rotations.
     *
     * Rotations happen in constant time and simply move pointers around
     * on trees.
    */
    private void lrRotate(Node<T> A) {
        Node<T> B = A.left;
        Node<T> C = B.right;

        B.right = C.left;
        if(B.right != null) {
            B.right.parent = B;
        }

        A.left = C;
        C.left = B;
        B.parent = C;
        C.parent = A;
    }

    private void llRotate(Node<T> A) {
        Node<T> B = A.left;
        Node<T> C = B.left;

        A.left = B.right;
        if(A.left != null) {
            A.left.parent = A;
        }

        B.right = A;
        B.parent = A.parent;
        if(B.parent != null) {
            if(B.parent.left == A) {
                B.parent.left = B;
            } else {
                B.parent.right = B;
            }
        }

        A.parent = B;
    }

    private void rlRotate(Node<T> A) {
        Node<T> B = A.right;
        Node<T> C = B.left;

        B.left = C.right;
        if(B.left != null) {
            B.left.parent = B;
        }

        A.right = C;
        C.right = B;
        B.parent = C;
        C.parent = A;
    }

    private void rrRotate(Node<T> A) {
        Node<T> B = A.right;
        Node<T> C = B.right;

        A.right = B.left;
        if(A.right != null) {
            A.right.parent = A;
        }

        B.left = A;
        B.parent = A.parent;
        if(B.parent != null) {
            if(B.parent.left == A) {
                B.parent.left = B;
            } else {
                B.parent.right = B;
            }
        }

        A.parent = B;
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
        System.out.println("ROOT: " + this.root.data);
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
