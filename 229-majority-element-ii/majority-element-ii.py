class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        Counter = dict()
        for ele in nums:
            Counter[ele] = Counter.get(ele,0) +1
        n = len(nums)
        ans =[]
        for value, count in Counter.items():
            if count > n//3:
                ans.append(value)
        return ans