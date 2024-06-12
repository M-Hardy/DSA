class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int oneBack = 0;
        int twoBack = 0;

        for (int i = 2; i < cost.length; i++) {
            int cur = Math.min(oneBack + cost[i - 1], twoBack + cost[i - 2]);
            twoBack = oneBack;
            oneBack = cur;

        }

        // twoBack is @ 2nd last pos, oneBack is @ last pos; add 2nd last/last vals
        // to both costs and return min
        return Math.min(twoBack + cost[cost.length - 2], oneBack + cost[cost.length - 1]);
    }

    public int ARRAYminCostClimbingStairs(int[] cost) {
        int[] dp = new int[cost.length];
        dp[0] = 0;
        dp[1] = 0;

        for (int i = 2; i < dp.length; i++) {
            dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }

        return Math.min(dp[dp.length - 2] + cost[cost.length - 2], dp[dp.length - 1] + cost[cost.length - 1]);
    }
}