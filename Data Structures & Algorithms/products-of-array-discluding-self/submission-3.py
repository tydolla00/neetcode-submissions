class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            pro = 1
            left, right = i -1, i + 1
            while not left < 0 or not right >= len(nums):
                if left >=0:
                    pro *= nums[left]
                    left-= 1
                if right < len(nums):
                    pro *= nums[right]
                    right+=1
            res.append(pro)
        return res