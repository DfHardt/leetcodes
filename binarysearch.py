nums = [-1,0,3,5,9,12]
target = 9

def search(self, nums: list[int], target: int) -> int:
    r, l = 0, len(nums)-1

    while l <= r:
        meio = (l+r)//2

        if target > nums[meio]:
            l = meio+1 
        elif target < nums[meio]:
            r = meio-1
        else:
            return meio
    
    return -1