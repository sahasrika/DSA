nums = [10,2,64,3,5,7,44,6,7,33,2,24,565,773]

def selectionsort(nums):
    n = len(nums)

    for i in range(n):
        minimum_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[minimum_index]:
                minimum_index = j

        nums[i], nums[minimum_index] = nums[minimum_index], nums[i]

selectionsort(nums)
print(nums)