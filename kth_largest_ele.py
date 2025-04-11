def find_kth_largest(nums,k):
    for i in range (len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums[-k]

nums = [3, 2, 1, 5, 6, 4]
k = int(input("Enter the Kth largest element:"))
print(find_kth_largest(nums,k))