def find_missing_num(arr):

    total_sum = n * (n+1)/2
    arr_sum = sum(arr)

    missing_num = total_sum - arr_sum

    return missing_num


n = int(input("Enter the length of array:"))
arr = []
for i in range(n):
    num = int(input("Enter the Number in array:"))
    arr.append(num)
print(arr)

print(find_missing_num(arr))