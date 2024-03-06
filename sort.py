# # def bubble_sort(arr):
# #     n = len(arr)
# #     for i in range(n):
# #         for j in range(0, n-i-1):
# #             if arr[j] > arr[j+1]:
# #                 arr[j], arr[j+1] = arr[j+1], arr[j]
# #
# # # Example usage:
# # my_list = [64, 34, 25, 12, 22, 11, 90]
# # bubble_sort(my_list)
# # print("Sorted array is:", my_list)
# 
# # my_list = [64, 34, 25, 12, 22, 11, 90]
# # n=len(my_list)
# # for  i in my_list:
# #     for j in range(0,n-1):
# #         if my_list[j]>my_list[j+1]:
# #             my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
# # print(my_list)
# 
# data_list = [11,-5, -23, 5, 0, 23, -6, 23, 67]
# new_list = []
# 
# while data_list:
#     minimum = data_list[0]  # arbitrary number in list
#     for x in data_list:
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)
# 
# print (new_list)

# sorting array without using sort function?
l=[1,3,6,2,8,9,0,12,54]
n=len(l)
for i in l:
    for j in range(0,n-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]