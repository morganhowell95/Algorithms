enum Direction {
    UP,
    LEFT,
    DIAG,
    END
}

public class LPSS {

    private static String reverse(String s) {
        StringBuilder sb = new StringBuilder(s);
        return sb.reverse().toString();
    }

    private static Direction[][] findLCS(String a, String b) {
        if(a.isEmpty() || b.isEmpty()) {
            return null;
        }

        // Initialize Dynamic Tables
        int[][] memo = new int[a.length() + 1][b.length() + 1];
        Direction[][] bt = new Direction[a.length() + 1][b.length() + 1];

        for(int i = 0; i < memo.length; i++) {
            memo[i][0] = 0;
            bt[i][0] = Direction.END;
        }
        for(int j = 0; j < memo[0].length; j++) {
            memo[0][j] = 0;
            bt[0][j] = Direction.END;
        }

        // Construct Table
        for(int i = 1; i < memo.length; i++) {
            for(int j = 1; j < memo[i].length; j++) {
                if(a.charAt(i-1) == b.charAt(j-1)) {
                    memo[i][j] = memo[i-1][j-1] + 1;
                    bt[i][j] = Direction.DIAG;
                } else if(memo[i-1][j] > memo[i][j-1]) {
                    memo[i][j] = memo[i-1][j];
                    bt[i][j] = Direction.UP;
                } else {
                    memo[i][j] = memo[i][j-1];
                    bt[i][j] = Direction.LEFT;
                }
            }
        }

        return bt;
    }

    private static String findPalindromeSequence(String s) {
        if(s == null || s.isEmpty()) {
            return "";
        }

        // Search for a palindrome
        int middle = s.length() / 2;
        String left = s.substring(0, middle);
        String right = reverse(s.substring(middle, s.length()));

        // Find the actual LCS
        Direction[][] backtrack = findLCS(left, right);
        if(backtrack == null) {
            return "";
        } else {
            StringBuilder common = new StringBuilder();
            int x = left.length(), y = right.length();
            while(backtrack[x][y] != Direction.END) {
                switch(backtrack[x][y]) {
                    case UP:
                        x -= 1;
                        break;
                    case LEFT:
                        y -= 1;
                        break;
                    case DIAG:
                        x -= 1;
                        y -= 1;
                        common.insert(0, left.charAt(x));
                        break;
                    default:
                        break;
                }
            }

            // Determine if the palindrome should be even or odd
            StringBuilder tmp = new StringBuilder(common).reverse();
            if(backtrack[left.length()][right.length()] != Direction.DIAG) {
                common.append(left.charAt(left.length() - 1));
            }
            common.append(tmp.toString());
            return common.toString();
        }
    }

    public static void main(String[] args) {
        String test = "character";
        System.out.println(findPalindromeSequence(test));
    }



}
