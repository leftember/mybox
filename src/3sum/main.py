from typing import List
import sys

class Solution:
    def threeSum2(self, nums: List[int], start: int, end: int) -> set():
        result = set()
        if end - start < 2:
            return result
        if nums[end] < 0:
            return result
        if nums[start] > 0:
            return result
        left = start
        while nums[left] <= -nums[end] // 2 and left < end-1:
            missing = -(nums[left] + nums[end])
            if self.get_num(nums, left + 1, end -1, missing):
                result.add((nums[left], missing, nums[end]))
            left += 1
        right = end -1
        while nums[right] >= -nums[start] // 2 and start < right-1:
            missing = -(nums[start] + nums[right])
            if self.get_num(nums, start + 1, right-1, missing):
                result.add((nums[start], missing, nums[right]))
            right -= 1
        result.update(self.threeSum2(nums, start +1, end -1))
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []
        nums.sort()
        # delete duplicate numbers if more then 3 and more then 3 zeros.
        nnums = [nums[0]]
        pre = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] != pre:
                pre = nums[i]
                nnums.append(nums[i])
                i += 1
            else:
                nnums.append(nums[i])
                if nums[i] != 0:
                    while i < len(nums) and nums[i] == pre:
                        i += 1
                else:
                    i += 1
                    if i < len(nums) and nums[i] == pre:
                        nnums.append(nums[i])
                        i += 1
                    while i < len(nums) and nums[i] == pre:
                        i += 1
        #print(nnums)
        return list(self.threeSum2(nnums, 0, len(nnums)-1))

    def get_num(self, nums, start, end, to_find):  # [start, end], inclusive.
        while start < end:
            mid = (start + end) // 2
            if nums[mid] >= to_find:
                end = mid
            else:
                start = mid + 1
        return nums[start] == to_find

if __name__ == '__main__':
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    s = Solution()
    nums = eval(input())
    r = s.threeSum(nums)
    #ll = [li for li in r if li[0] == -99927]
    #print(len(ll))
    print(len(r))
    #print(r)
