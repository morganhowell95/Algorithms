// Caleb
// Reverse integer

// Reverse digits of an integer.
// Example1: x = 123, return 321
// Example2: x = -123, return -321
// Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows.
// For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

public class Solution {
    public int reverse(int x) {
        int sum = 0;
        int neg = 0;
        
        if (x < 0) {
            x = x * -1;
            neg = 1;
        }
        
        while (x > 0) {
            if (sum != 0 && Integer.MAX_VALUE / sum < 10 && Integer.MAX_VALUE / sum > -10) {
                return 0;
            }
            sum = sum * 10 + x % 10;
            x /= 10;
        }
            
        if (neg == 1) {
            sum *= -1;
        }
            
        return sum;
    }
}