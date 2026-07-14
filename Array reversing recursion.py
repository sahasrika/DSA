print("-------REVERSING AN ARRAY USING RECURSION----------")
nums = [5,7,3,2,6,1,5,9]

def function(nums , left , right):
    if left>=right:
        return
    nums[left],nums[right]= nums[right],nums[left]
    function(nums , left+1, right-1)
function(nums , 0 , len(nums)-1)
print(nums)S