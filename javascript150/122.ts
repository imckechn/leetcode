function maxProfit(prices: number[]): number {
    var profit: number = 0;
    var stockPrice: number = 0;
    var isBought: boolean = false;

    for (var i = 0; i < prices.length-1; i++) {
        if (prices[i] > prices[i+1] && isBought) {
            profit += prices[i]-stockPrice;
            stockPrice = 0;
            isBought = false;

        } else if (prices[i] < prices[i+1] && !isBought) {
            stockPrice = prices[i];
            isBought = true;
        }
    }

    if (isBought) {
        return profit + (prices[prices.length-1]-stockPrice);
    }
    return profit;
};

//Better version
function maxProfitV2(prices: number[]): number {
    var profit: number = 0;
    for (var i = 1; i < prices.length; i++) {
        if (prices[i-1] < prices[i]) {
            profit += prices[i-1] - prices[i];
        }
    }
    return profit;
};

console.log(maxProfit([7,1,5,3,6,4]))