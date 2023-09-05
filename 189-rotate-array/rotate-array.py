class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n 
        x = n - k 
        store = []
        for i in range(n):
            if i >= x:
                store.append(nums[i])
        # print(store)
        for i in range(len(nums)-1,-1,-1):
            if i >= k:
                nums[i] = nums[i-k]
            else:
                # print(i)
                nums[i] = store[i]