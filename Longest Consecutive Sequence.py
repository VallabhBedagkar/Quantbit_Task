def longest_consecutive(nums):

    nums_sort = sorted(nums)
    long = []
    current = [nums_sort[0]]
    for i in range (1,len(nums_sort)):
            if nums_sort[i] == nums_sort[i-1]+1:
                current.append(nums_sort[i])
            else:
                if len(current) > len(long):    
                    long = current
                current = [nums_sort[i]]

    if len(current) > len(long):
        long = current
    return long

nums = [100,4,200,1,2,3]

print(longest_consecutive(nums))