public class LPS {

    private static String longestPalindrome(String a) {

        int start_pos = -1;
        int end_pos = -1;
        boolean[][] memo = new boolean[a.length()][a.length()];

        // Initialize trivial case
        for(int i = 0; i < memo.length; i++) {
            for(int j = 0; j <= i; j++) {
                memo[i][j] = true;
            }
        }

        // Begin the dynamic aspect of the program
        for(int len = 2; len <= a.length(); len++) {
            for(int i = 0; i <= a.length() - len; i++) {
                int j = i + len - 1;
                if(a.charAt(i) == a.charAt(j)) {
                    memo[i][j] = memo[i+1][j-1];
                    if(memo[i][j]) {
                        start_pos = i;
                        end_pos = j;
                    }
                } else {
                    memo[i][j] = false;
                }
            }
        }

        return a.substring(start_pos, end_pos + 1);
    }

    public static void main(String[] args) {

        String a = "chaahc";
        String b = "character";
        System.out.println(longestPalindrome(a));
        System.out.println(longestPalindrome(b));

    }


}
