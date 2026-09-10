class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 # tracking max profit
        lP, rP = 0, 1 # Two pointers 

        while rP < len(prices):
            if(prices[rP] > prices[lP]):
                profit = prices[rP] - prices[lP] 
                maxP = max(maxP, profit) # if a new profit is found check if higher
            else:
                lP = rP # Set lP to rP if rP is lesser
            rP += 1 # increment rP every time
        return maxP