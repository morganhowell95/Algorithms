
/*
   class Node 
       int data;
       Node left;
       Node right;
*/
void top_view(Node root)
{
    Node left = root.left;
    int left_height = 0;
    while(left!=null){
        left_height++;
        left = left.left;
    }
    
    int [] nodes_left = new int[left_height];
    
    left = root.left;
    int height = 0;
    while(left!=null){
        nodes_left[height] = left.data;
        height++;
        left = left.left;
    }
    
    for(int i=nodes_left.length-1; i>=0; i--){
        System.out.print(nodes_left[i]);
        System.out.print(" ");
    }
    
    
    System.out.print(root.data);
    System.out.print(" ");
    
    
    Node right = root.right;
    int right_height = 0;
    while(right!=null){
        right_height++;
        right = right.right;
    }
    
    int [] nodes_right = new int[right_height];
    
    right = root.right;
    height = 0;
    while(right!=null){
        nodes_right[height] = right.data;
        height++;
        right = right.right;
    }
    
    for(int i=0; i<nodes_right.length; i++){
        System.out.print(nodes_right[i]);
        System.out.print(" ");
    }
    
    
  
}

