import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class FindOrderStat {

    private static void swap(int[] values, int i, int j) {
        int tmp = values[i];
        values[i] = values[j];
        values[j] = tmp;
    }

    private static int partition(int[] values, int low, int high) {
        int j = low - 1;
        for(int i = low; i < high; i++) {
            if(values[i] <= values[high]) {
                j++;
                swap(values, i, j);
            }
        }
        swap(values, j+1, high);
        return j+1;
    }

    private static int findOrderStatistic(int[] values, int low, int high, int index) {
        if(low == high) {
            return values[low];
        } else {
            int pivot = partition(values, low, high);
            if(pivot == index) {
                return values[pivot];
            } else if(index < pivot) {
                return findOrderStatistic(values, low, pivot - 1, index);
            } else {
                return findOrderStatistic(values, pivot + 1, high, index - pivot);
            }
        }
    }

    public static int findOrderStatistic(int[] values, int i) {
        return findOrderStatistic(values, 0, values.length - 1, i);
    }
  
    public static void main(String[] args) {

        // Display our unsorted array
        Random r = new Random();
        int[] values = new int[10];
        System.out.format("%10s", "Unsorted:");
        for(int i = 0; i < values.length; i++) {
            values[i] = Math.abs(r.nextInt() % 30);
            System.out.format("%5d", values[i]);
        }
        System.out.println();

        // Print out our order statistic (e.g. 7th)
        System.out.println("Order Stat: " + findOrderStatistic(values, 7));

        // Compare with sorted array
        Arrays.sort(values);
        System.out.format("%10s", "Sorted:");
        for(int i = 0; i < values.length; i++) {
            System.out.format("%5d", values[i]);
        }
        System.out.println();

    }
}

