class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }

        int lowest = 1000000;
        
        int best = 0;

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] >= lowest) {
                continue;
            } else {
                lowest = prices[i];
            }
            for (int j = i+1; j < prices.length; j++) {
                if (prices[j] - prices[i] > best) {
                    best = prices[j] - prices[i];
                }
            }
        }
        return best;
    }
}