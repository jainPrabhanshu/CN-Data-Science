# Given an array that might contain duplicate elements, find the maximum possible distance between occurrences of two repeating elements i.e. elements having same value. If there are no duplicate elements in the array, return 0.
# Input Format :
# Line 1 : Contains integer N which is the size of array
# Line 2 : Contains N Integers i.e. the elements of the array.
# Sample Output :
#  Line 1 : Maximum Distance Value
# Sample Input :
# 9
# 1  3  1  4  5  6  4  8  3
# Sample Output :
# 7
# Sample Output Explanation :
# arr = [1, 3, 1, 4, 5, 6, 4, 8, 3];
#     index0 = 1
#     index1 = 3
#     index2 = 1
#     index3 = 4
#     index4 = 5
#     index5 = 6
#     index6 = 4
#     index7 = 8
#     index8 = 3

#     In the above array, the repeating elements are :- (1, 3, 4)
#     - Distance bw first and last occurence of 1 = 2(index2 - index0)
#     - Distance bw first and last occurence of 3 = 7(index8 - index1)
#     - Distance bw first and last occurence of 4 = 3(index6 - index3)

#     So, for the above array you must return 7, as this is maximum possible distance between two repeating elements having same value.

## Read input as specified in the question.
## Print output as specified in the question.
def maxDistance(arr, n):
     
    # Used to store element to first index mapping
    mp = {}
 
    # Traverse elements and find maximum distance between
    # same occurrences with the help of map.
    maxDict = 0
    for i in range(n):
 
        # If this is first occurrence of element, insert its
        # index in map
        if arr[i] not in mp.keys():
            mp[arr[i]] = i
 
        # Else update max distance
        else:
            maxDict = max(maxDict, i-mp[arr[i]])
 
    return maxDict

n = int(input())
arr = list(map(int,input().split()))
print(maxDistance(arr, n))