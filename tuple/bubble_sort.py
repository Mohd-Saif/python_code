# def bubble_sort(arr):
#     n=len(arr)
#     list=[]
#     for i in range(n):
#         for j in range(0,n-i-1):
#            if arr[j]>arr[j+1]:
#                arr[j],arr[j+1]=arr[j+1],arr[j]
#     for i in arr:
#         if i not in list:
#             list.append(i)
#     return list
# arr=[12,3,4,5,5,6,7,4,2,1,4,56]
# print(bubble_sort(arr))



def sorted_list(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [1, 2, 355, 6, 6, 77, 7, 12, 4, 45, 5]
print(sorted_list(arr))
