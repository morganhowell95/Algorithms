enum Method {
    INSERT,
    DELETE,
    COPY,
    NONE
}

class DistanceResult {

    private String a;
    private String b;
    private int edit_count;

    public DistanceResult(String a, String b, int edit_count) {
        this.a = a;
        this.b = b;
        this.edit_count = edit_count;
    }

    @Override
    public String toString() {
        return String.format("%s%n%s%nEdit Count: %d", a, b, edit_count);
    }
}

public class EditDistance {

    private static DistanceResult buildDistanceResult(Method[][] backtrack, String a, String b) {
        StringBuilder aBuilder = new StringBuilder();
        StringBuilder bBuilder = new StringBuilder();

        int edit_cost = 0;
        int x = a.length(), y = b.length();
        while(backtrack[x][y] != Method.NONE) {
            switch(backtrack[x][y]) {
                case INSERT:
                    y -= 1;
                    edit_cost += 1;
                    aBuilder.insert(0, ' ');
                    bBuilder.insert(0, b.charAt(y));
                    break;
                case DELETE:
                    x -= 1;
                    edit_cost += 1;
                    bBuilder.insert(0, ' ');
                    aBuilder.insert(0, a.charAt(x));
                    break;
                case COPY:
                    x -= 1;
                    y -= 1;
                    aBuilder.insert(0, a.charAt(x));
                    bBuilder.insert(0, b.charAt(y));
                    edit_cost += (a.charAt(x) == b.charAt(y)) ? 0 : 1;
                    break;
                default:
                    break;
            }
        }

        return new DistanceResult(aBuilder.toString(), bBuilder.toString(), edit_cost);
    }

    private static DistanceResult distance(String a, String b) {

        // Consider all base cases beforehand
        a = (a == null) ? "" : a;
        b = (b == null) ? "" : b;
        if(a.isEmpty()) {
            return new DistanceResult(b, b, b.length());
        } else if(b.isEmpty()) {
            return new DistanceResult(a, a, a.length());
        }

        // Begin dynamic methodology
        int[][] table = new int[a.length()+1][b.length()+1];
        Method[][] backtrack = new Method[a.length()+1][b.length()+1];

        // Initialize base case
        table[0][0] = 0;
        backtrack[0][0] = Method.NONE;

        for(int i = 1; i < table.length; i++) {
            table[i][0] = i;
            backtrack[i][0] = Method.DELETE;
        }
        for(int j = 1; j < table[0].length; j++) {
            table[0][j] = j;
            backtrack[0][j] = Method.INSERT;
        }

        // Begin enumerating options
        for(int i = 1; i < table.length; i++) {
            for(int j = 1; j < table[i].length; j++) {

                // Assume top first
                Method m = Method.DELETE;
                int min = table[i-1][j] + 1;

                // Check left
                if(table[i][j-1] + 1 < min) {
                    m = Method.INSERT;
                    min = table[i][j-1] + 1;
                }

                // Check topleft
                int cost = (a.charAt(i-1) == b.charAt(j-1)) ? 0 : 1;
                if(table[i-1][j-1] + cost < min) {
                    m = Method.COPY;
                    min = table[i-1][j-1] + cost;
                }

                // Lastly update current position
                table[i][j] = min;
                backtrack[i][j] = m;

            }
        }

        return buildDistanceResult(backtrack, a, b);
    }

    public static void main(String[] args) {
        String a = "GTGA";
        String b = "ATCGAC";
        String c = "appropriate meaning";
        String d = "approximate matching";
        System.out.println(distance(a, b));
        System.out.println(distance(c, d));
    }

}
