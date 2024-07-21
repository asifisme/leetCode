# Coin change 

class Solution:
    def __init__(self, coins : list[int], amount : int):
        self.coins = coins 
        self.amount = amount 
    
    def coinChange(self):
        dp  = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                pass 
            
        return dp 

coins = [1,2,5]
amount = 11

s = Solution(coins, amount) 

print(s.coinChange())
