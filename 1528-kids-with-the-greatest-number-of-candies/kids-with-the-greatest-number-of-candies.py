class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        # Find the maximum candies currently held by any kid
        max_candies = max(candies)
        
        # Check if adding extraCandies makes the current kid's total >= max_candies
        return [candy + extraCandies >= max_candies for candy in candies]
