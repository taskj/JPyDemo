nums = [6,5,3,1,8,0.5,8,7,2,4]

j = 0

while j < len(nums) -1:
    j += 1
    i = 0
    while i < len(nums) -1:
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
        i += 1
print(nums)