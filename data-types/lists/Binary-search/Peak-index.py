nums = [2,4,6,8,10,8,5]


def get_peak_index(nums,n):
    index=-1
    start=0
    end=n-1

    while (start<=end):
        mid = start + (end-start)//2

        if(nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]):
            return mid
        elif (nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]):
            start=mid+1
        else:
            end=mid-1
    
    return index

index = get_peak_index(nums,len(nums))

print(index)