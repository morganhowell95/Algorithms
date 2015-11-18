/**
 * The following is a disjoint set linked list implementation.
 *
 * Note each disjoint set must be maintained separately. This supports
 * construction (via the constructor), union with another disjoint set,
 * and the obtainment of the representative element of the list.
 *
 * This implementation works via linked lists.
*/
public class DisjointSet<T> {

    public class Node<T> {
        public T value;
        private Node<T> next;
        private Node<T> parent;
        public Node(T value, Node<T> parent) {
            this.value = value;
            this.next = null;
            this.parent = (parent == null) ? this : parent;
        }
    }

    private Node<T> head;
    private Node<T> tail;

    public DisjointSet(T value) {
        head = new Node<T>(value, null);
        tail = head;
    }

    public void union(DisjointSet<T> ll) {
        Node<T> other_head = ll.head;
        while(other_head != null) {
            tail.next = other_head;
            tail.next.parent = head;
            tail = tail.next;
            other_head = other_head.next;
        }
    }

    public Node<T> find() {
        return head.parent;
    }

    public boolean front() {
        return head.parent == head;
    }

}
