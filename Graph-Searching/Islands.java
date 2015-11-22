import java.util.*;

class IslandFinder {

    private int[][] matrix;
    private HashMap<Integer, Integer> island_sizes;
    private HashMap<Integer, DisjointSet<Integer>> labels;

    public IslandFinder(int[][] matrix) {
        this.matrix = matrix;
        this.island_sizes = new HashMap<Integer, Integer>();
        this.labels = new HashMap<Integer, DisjointSet<Integer>>();
    }

    // Used for initialize copy array and converting from count to just
    // 0s and 1s for 2-pass method
    private void initializeBinary(int[][] matrix) {
        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix[i].length; j++) {
                if(matrix[i][j] != 0) {
                    matrix[i][j] = 1;
                }
            }
        }
    }

    // Means of updating each pair of indices in a compact manner
    private void updateLabel(int[][] copy, int i_pos, int j_pos) {

        int[] i_indices = new int[]{i_pos-1, i_pos-1, i_pos-1, i_pos};
        int[] j_indices = new int[]{j_pos+1, j_pos, j_pos-1, j_pos-1};

        for(int k = 0; k < i_indices.length; k++) {
            int i = i_indices[k];
            int j = j_indices[k];
            if(i >= 0 && j >= 0 && j < copy[i].length && copy[i][j] > 1) {
                if(copy[i_pos][j_pos] == 1) {
                    Integer key = labels.get(copy[i][j]).find().value;
                    island_sizes.put(key, island_sizes.get(key) + 1);
                    copy[i_pos][j_pos] = copy[i][j];
                } else if(copy[i_pos][j_pos] != copy[i][j]) {
                    DisjointSet<Integer> set = labels.get(copy[i][j]);
                    set.union(labels.get(copy[i_pos][j_pos]));
                }
            }
        }

    }

    public int[][] findIslands(int[][] matrix) {

        int[][] copy = new int[matrix.length][];
        for(int i = 0; i < copy.length; i++) {
            copy[i] = matrix[i].clone();
        }
        initializeBinary(copy);

        // First pass; label values and create disjoint sets
        Integer label = 2;
        for(int i = 0; i < copy.length; i++) {
            for(int j = 0; j < copy[i].length; j++) {
                if(copy[i][j] == 1) {

                    // See if part of an island
                    updateLabel(copy, i, j);
                    constructIsland(copy[i][j], label++);

                    // New island found
                    if(copy[i][j] == 1) {
                        copy[i][j] = label++;
                        island_sizes.put(copy[i][j], 1);
                        labels.put(copy[i][j], new DisjointSet<Integer>(copy[i][j]));
                    }

                }
            }
        }

        // Second pass; create an int[] for each island
        // Initialze matrix to proper size
        int[][] islands = new int[island_sizes.size()][0];
        for(Integer key : island_sizes.keySet()) {
            islands[key - 2] = new int[island_sizes.get(key)];
        }

        for(int i = 0; i < copy.length; i++) {
            for(int j = 0; j < copy[i].length; j++) {
                if(copy[i][j] > 1) {
                    Integer repr = labels.get(copy[i][j]).find().value;
                    int index = islands[repr-2].length - island_sizes.get(repr);
                    island_sizes.put(repr, island_sizes.get(repr) - 1);
                    islands[repr - 2][index] = matrix[i][j];
                }
            }
        }

        return islands;
    }

}

public class Islands {

    public static void main(String[] args) {
        int[][] mat = new int[][]{
            { 0, 1, 0, 7, 0 },
            { 2, 0, 0, 0, 8 },
            { 3, 4, 0, 0, 0 },
            { 5, 0, 6, 0, 0 },
            { 0, 0, 0, 0, 0 },
        };
        IslandFinder isf = new IslandFinder(mat);
        int[][] islands = isf.findIslands(mat);
        for(int i = 0; i < islands.length; i++) {
            for(int j = 0; j < islands[i].length; j++) {
                System.out.format("%5d", islands[i][j]);
            }
            System.out.println();
        }
    }


}
