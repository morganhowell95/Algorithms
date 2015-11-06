class Node<T> {
    public T data;
    public Node<T> next;
    public Node(T data) {
        this.data = data;
    }
}

public class Interweave {

    // Convenience method to quickly build a linked list
    // Useful for testing purposes
    public static Node<Integer> buildLinkedList(int count) {
        Node<Integer> root = (count < 1) ? null : new Node<Integer>(0);
        Node<Integer> tmp = root;
        for(int i = 1; i < count; i++) {
            tmp.next = new Node<Integer>(i);
            tmp = tmp.next;
        }
        return root;
    }

    // Convenience method for printing out a linked list
    // Assumes integer values for formatting purposes
    public static void printLinkedList(Node<Integer> root) {
        for(Node<Integer> tmp = root; tmp != null; tmp = tmp.next) {
            System.out.format("%5d", tmp.data);
        }
        System.out.println();
    }

    // Actual generic method requested.
    public static <T> void interweave(Node<T> root) {

        // Using the runner method, find the middle of the linked list
        Node<T> start = root;
        Node<T> middle = root;
        while(middle != null) {
            start = start.next;
            middle = middle.next;
            if(middle != null) {
                middle = middle.next;
            }
        }

        // Reset pointers
        middle = start;
        start = root;

        // Begin the actual interweaving process. Need to grab values
        // from both halves of the list and append to a current. Middle
        // will always hit the end of the list first since if list size
        // is odd, middle will point to the element immediately following
        // the true middle
        boolean flag = true;
        Node<T> current = start;
        Node<T> start_end = middle;
        while(start != start_end && middle != null) {
            if(flag) {
                start = start.next;
                current.next = middle;
            } else {
                middle = middle.next;
                current.next = start;
            }
            current = current.next;
            flag = !flag;
        }

        // Must close off the list
        if(current != null) {
            current.next = null;
        }

    }

    public static void main(String[] args) {
        Node<Integer> root = buildLinkedList(6);
        printLinkedList(root);
        interweave(root);
        printLinkedList(root);
    }

}



