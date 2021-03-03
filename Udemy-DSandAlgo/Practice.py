##37. log all pairs of array
# list_num = [1,2,3,4,5]
# for i in list_num:
#     for j in list_num:
#         if i != j:
#             print(i,j)

# ##52. interview question
#
# # input - 2 arrays, create function, output - boolean, if_common_items_present - rule 1
# # are arrays limited/constant? - rule 2, 4
# # user should give input  or input with function ? - rule 2, 4
# # is any one pair enough? - rule 2, 4
#     # by using break, the algo stops running as soon as it finds one pair - rule 7
#     # but this needed a new variable assignment (result = false) which might take extra space - rule 3
# # the code is readable
# # Time complexity - O9m*n), Space complexity - O(1)
# # brutal force approach - rule 5
# def has_common_items(list1, list2): # nested loop - O(n^2) if same lengths or O(m*n) if different - can be further improved - rule 6
#     result = False
#     for item1 in list1: # rule 12
#         for item2 in list2: # rule 12
#             if item1 == item2:
#                 result = True
#                 break # rule 7 (trying to reduce unnecessary work)
#     return result
#
#
# print(has_common_items([1,2,3,4],[5,8,5,6]))
#
# # this solution can be improved by converting the first
#     # array into an object and comparing the second array to this object.
# ## array1 ==> obj
# ## 1: True
# ## 2: True
# ## 3: True
# ## 4: True
# ## array2[index] == obj.properties
#
# def has_common_items2(list1, list2):
#     ## loop through first array and create object where items == properties - rule 8
#     ## loop through second array and check if number in second array exists on created object - rule 8
#     # this might make two consecutive loops - O(m+n)
#
##53
# def has_common_items2(list1, list2):
#     ## loop through first array and create object where items == properties - rule 8
#     object_array1 = []
#     for item1 in list1:
#         if item1 not in object_array1:
#             object_array1.append(item1) # space - O(array1)
#             # return True
#     # return object_array1
#     ## loop through second array and check if number in second array exists on created object - rule 8
#     for item2 in list2:
#         if item2 in object_array1:
#             return True
#     return False
# print(has_common_items2([1,2,3,4],[3,4,5,6]))
#
# ## it is the same as below. so not correct. rework after learning DS
# for item in list1:
#     if item in list2:
#         return True

## 62. Arrays
strings = ['a', 'b', 'c', 'd'] #array
 # 4*4 = 16 bytes of storage in RAM
print(strings[2]) #access - O(1)
strings.append('e') #push - O(1), O(n) if static arrays (C++)
strings.pop() #pop - O(1) if last element and O(n) if arbitary
strings.insert(0,'x') #insert - O(n) - because indices are shifting througout array
strings.remove('b') #delete - O(n) - because shifting happens after 'b'
print(strings)