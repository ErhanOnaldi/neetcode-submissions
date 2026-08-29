class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        count1 = 0 
        count2 = 0 
        res = []

        def if_bigger_than_n_divided_by_3(candidate) -> bool:
            n_divided_by_3 = len(nums) / 3
            counter = 0
            for num in nums:
                if num == candidate:
                    counter += 1 
            return counter > n_divided_by_3

        for num in nums:
            if count1==0:
                candidate1 = num
            if count2 == 0 and num != candidate1:
                candidate2 = num
            
            if candidate1 == num:
                count1+=1
            elif candidate2 == num:
                count2+=1
            else:
                count1 -= 1 
                count2 -= 1
        
        if count1 > 0 and if_bigger_than_n_divided_by_3(candidate1):
            res.append(candidate1)
        
        if count2 > 0 and if_bigger_than_n_divided_by_3(candidate2):
            res.append(candidate2)


        return res

    



                



    