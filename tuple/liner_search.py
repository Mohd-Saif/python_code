def liner_data(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[1,2,1,2,3,4,5,6,3,4,6,7,12,9897]
target=5
data=liner_data(arr,target)
print(data)