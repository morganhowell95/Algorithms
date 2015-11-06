class Tree {

    // Internal Node
    private class Node {
        int value;
        int height;
        Node left;
        Node right;
        public Node(int value) {
            this.height = 1;
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }

    // Base of the tree
    private Node root;

    // Used to maintain the longest subsequences
    private Node largest;

    // Build tree given values
    // Then by checking for largest height, we are finished
    public Tree(int[] values) {
        this.root = null;
        this.largest = null;
        for(int i = 0; i < values.length; i++) {
            this.root = this.insert(this.root, values[i]);
        }
    }

    // Our longest subsequence
    public int getLargestHeight() {
        return largest.height;
    }

    // During insertions, keep track of the heights
    // whenever a node is added to the right of the tree
    private Node insert(Node n, int value) {

        if(n == null) {
            return new Node(value);
        }

        // Basic insertion into tree
        if(value <= n.value) {
            n.left = insert(n.left, value);

        // Maintain counts and resume basic insertion
        } else {
            n.height += 1;
            if(this.largest == null || n.height > largest.height) {
                this.largest = n;
            }
            n.right = insert(n.right, value);
        }

        return n;
    }

}

public class LongestSequence {

    public static int longestSubsequence(int[] values) {
        Tree t = new Tree(values);
        return t.getLargestHeight();
    }

    public static void main(String[] args) {
        int[] tmp = new int[]{10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println(longestSubsequence(tmp));
    }

}
