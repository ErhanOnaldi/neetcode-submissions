class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = l
        while l <= r:
            rate = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += (pile + rate - 1) // rate

            if hours <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1

        return res