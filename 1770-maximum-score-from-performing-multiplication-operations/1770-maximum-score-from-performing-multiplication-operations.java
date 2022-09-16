class Solution {
    public static int maximumScore(int[] nums, int[] multipliers) {
        int n = nums.length;
        int m = multipliers.length;

        int[][] dp = new int[m + 1][m + 1];

        for (int i = 1; i <= m; i++) {
            dp[0][i] = dp[0][i - 1] + nums[n - i] * multipliers[i - 1];
            dp[i][0] = dp[i - 1][0] + nums[i - 1] * multipliers[i - 1];
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= m - i; j++) {
                int idx = i + j - 1;
                dp[i][j] = Math.max(dp[i - 1][j] + nums[i - 1] * multipliers[idx], dp[i][j - 1] + nums[n - j] * multipliers[idx]);
            }
        }

        int ans = Integer.MIN_VALUE;
        for (int i = 0; i <= m; i++) {
            ans = Math.max(ans, dp[i][m - i]);
        }

        return ans;
    }
}