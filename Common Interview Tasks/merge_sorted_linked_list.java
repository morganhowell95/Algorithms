/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/

Node MergeLists(Node headA, Node headB) {
    Node n = new Node();
    Node head = n;
    
    //while neither list is empty compare elements and insert
    while(headA!=null && headB!=null){
        if(headA.data < headB.data){
            n.data = headA.data;
            headA = headA.next;
        } else {
            n.data = headB.data;
            headB = headB.next;
        }
        
        n.next = new Node();
        n = n.next;
    }
        
    //list 1 has elements, but list 2 is empty
    while(headA!=null){
        n.data = headA.data;
        headA = headA.next;
        
        if(headA!=null){
            n.next = new Node();
            n = n.next;
        }
    }
        
    //list 1 is empty, but list 2 has elements
    while(headB!=null){
        n.data = headB.data;
        headB = headB.next;
        
        if(headB!=null){
            n.next = new Node();
            n = n.next;
        }
    }
    
    return head;
}

