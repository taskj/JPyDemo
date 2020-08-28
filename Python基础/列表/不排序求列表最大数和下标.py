nums = [3,1,9,8,4,2,0,7,5]

x = nums[0] #假设第0个是最大数
for num in nums:
    if num > x: #如果发现列表里面存在比假设还要大的数字
        #假设不成立，把假设的数字设置为发现的数字
        x = num
print('发现的最大数字是%d，它的下标是%d' % (x,nums.index(x)))
