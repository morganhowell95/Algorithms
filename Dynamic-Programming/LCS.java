enum Direction {
    UP,
    LEFT,
    DIAG,
    END
}

public class LCS {

    private static String printBacktrack(Direction[][] backtrack, String a, String b) {
        int x = a.length();
        int y = b.length();
        StringBuilder bs = new StringBuilder();
        while(backtrack[x][y] != Direction.END) {
            switch(backtrack[x][y]) {
                case UP:
                    x -= 1;
                    break;
                case LEFT:
                    y -= 1;
                    break;
                case DIAG:
                    bs.insert(0, a.charAt(x-1));
                    x -= 1;
                    y -= 1;
                    break;
                default:
                   break;
            }
        }
        return bs.toString();
    }

    private static String longestCommonSubsequence(String a, String b) {

        if(a.isEmpty() || b.isEmpty()) {
            return "";
        }

        // We use a dynamic programming solution to build up the longest
        // common subsequence as we continue moving upward through the
        // strings
        int[][] optimal = new int[a.length()+1][b.length()+1];
        Direction[][] backtrack = new Direction[a.length()+1][b.length()+1];

        // Initialize our values
        for(int i = 0; i < optimal.length; i++) {
            optimal[i][0] = 0;
            backtrack[i][0] = Direction.END;
        }
        for(int j = 0; j < optimal[0].length; j++) {
            optimal[0][j] = 0;
            backtrack[0][j] = Direction.END;
        }

        // Populate the table for the longest values
        for(int i = 1; i < optimal.length; i++) {
            for(int j = 1; j < optimal[i].length; j++) {
                if(a.charAt(i-1) == b.charAt(j-1)) {
                    optimal[i][j] = optimal[i-1][j-1] + 1;
                    backtrack[i][j] = Direction.DIAG;
                } else if(optimal[i-1][j] > optimal[i][j-1]) {
                    optimal[i][j] = optimal[i-1][j];
                    backtrack[i][j] = Direction.UP;
                } else {
                    optimal[i][j] = optimal[i][j-1];
                    backtrack[i][j] = Direction.LEFT;
                }
            }
        }

        // To obtain the longest common subsequence, we move backwards through
        // our backtrack array
        return printBacktrack(backtrack, a, b);
    }

}
