class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)

        for i in nums:
            dictionary[i] += 1 
        
        res = []
        for j in range(k):
            max_key = max(dictionary, key=dictionary.get)
            res.append(max_key)
            del dictionary[max_key]
        return res