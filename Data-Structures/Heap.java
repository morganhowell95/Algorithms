import java.io.*;
import java.util.*;

/**
 * A general array heap implementation.
 *
 * The following can be used as a priority queue
 * and allows for heapsorting.
*/
class Heap {
  
  // Flag to determine min/max heap
  private boolean min;
  
  // Containers of actual values
  private int[] values;
  private int heap_size;
  
  /**
   * General comparison for both min/max percolation
   * 
   * @a: index of value on left side
   * @b: index of valiue on right side
  */
  private boolean compare(int a, int b) {
    if(this.min) {
      return this.values[a] < this.values[b];
    } else {
      return this.values[a] > this.values[b];
    }
  }
  
  /**
   * Convenience method for proper swapping
   *
   * @a: Index of value to swap
   * @b: Index of value to swap
  */
  private void swap(int a, int b) {
    int tmp = this.values[a];
    this.values[a] = this.values[b];
    this.values[b] = tmp;
  }
  
  /**
   * Maintains the heap property recursively,
   * ensuring that comparisons are valid
   *
   * @index: Position to check heap properties at
  */
  private void heapify(int index) {
    
    int left = (index << 1) + 1;
    int right = left + 1;
    
    // Find next index to swap with
    int next_index = index;
    if(left < this.heap_size && compare(left, next_index)) {
      next_index = left;
    }
    if(right < this.heap_size && compare(right, next_index)) {
      next_index = right;
    }
    
    if(next_index != index) {
      swap(next_index, index);
      heapify(next_index);
    }
  }
  
  /**
   * Inserts element into our heap according to whether
   * the heap should be a minimum or maximum. We append
   * to the end and percolate the value up until it is
   * in the right position
   *
   * @value: Number to insert into the heap
  */
  public void insert(int value) {
    
    // Dynamically grow array if necessary
    if(this.heap_size + 1 == this.values.length) {
      int[] copy = new int[this.values.length * 2];
      System.arraycopy(this.values, 0, copy, 0, this.heap_size);
      this.values = copy;
    }
    
    // Insert into heap
    this.values[this.heap_size++] = value;
    
    // Percolate value up
    int index = this.heap_size - 1;
    while(index > 0) {
      
      // Since offsetted at 0, must correctly specify parent
      int parent = index >> 1;
      if(index % 2 == 0) {
        parent = (index - 1) >> 1;
      }
      
      // Determine if continuing is necessary
      if(!compare(parent, index)) {
        swap(parent, index);
        index = parent;
      } else {
        break;
      }
      
    }    
  }
  
  /**
   * Takes the topmost element off the array and swaps
   * the given values, reheapifying as necessary
  */
  public Integer extract() {
    if(this.heap_size == 0) {
      return null;
    }
    
    int tmp = this.values[0];
    this.values[0] = this.values[--this.heap_size];
    heapify(0);
    
    return tmp;
  }
  
  /**
   * Implementation of the heapsort algorithm.
   *
   * Note this should only be done with a max heap. Otherwise
   * the values will be in reverse.
  */
  public int[] heapsort() {
    
    // Restore state afterward
    int size = this.heap_size;
    int[] copy = new int[size];
    System.arraycopy(this.values, 0, copy, 0, size);
    
    // Sort
    while(this.heap_size > 0) {
      int tmp = extract();
      this.values[this.heap_size] = tmp; 
    }
    
    // Restore
    int[] result = new int[size];
    System.arraycopy(this.values, 0, result, 0, size);
    this.values = copy;
    this.heap_size = size;
    
    return result;
  }
  
  /**
   * Constructor.
   *
   * @min: Specifies whether the heap is a min or max.
   * @values: Initial values to place into the heap.
  */
  public Heap(boolean min, int[] values) {
    this.min = min;
    
    // Default size of values
    if(values == null) {
      this.values = new int[10];
      
    // Heapify the given values instead of inserting them all
    } else {
      this.heap_size = values.length;
      this.values = new int[values.length * 2];
      System.arraycopy(values, 0, this.values, 0, values.length);
      for(int i = (this.heap_size / 2) - 1; i >= 0; i--) {
        heapify(i);
      }
    }
    
  }
  
}

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class Solution {
  public static void main(String[] args) {
    
    // Heap Sample
    System.out.println("======================  Heap ======================");
    int[] unsorted = new int[]{5, 4, 3, 2, 1, 6, 1};
    System.out.format("%10s", "Unsorted:");
    for(int i = 0; i < unsorted.length; i++) {
      System.out.format("%5d", unsorted[i]);
    }
    System.out.println();
    
    
    Heap h = new Heap(false, unsorted);
    int[] sorted_heap = h.heapsort();
    System.out.format("%10s", "Sorted:");
    for(int i = 0; i < sorted_heap.length; i++) {
      System.out.format("%5d", sorted_heap[i]);
    }
    System.out.println();
    
    
  }
}
