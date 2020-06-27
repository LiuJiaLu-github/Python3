from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        if target not in nums:
            return -1
        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        else:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid