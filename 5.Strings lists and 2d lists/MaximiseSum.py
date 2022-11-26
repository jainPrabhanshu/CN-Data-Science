# Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum sum and return the maximum sum.
# That is, we can switch from one array to another array only at common elements.
# If no intersection element is present, we need to take sum of all elements from the array with greater sum.
# Input Format :
#  Line 1 : An integer M i.e. size of first array
#  Line 2 : M integers which are elements of first array, separated by spaces
#  Line 3 : An integer N i.e. size of second array
#  Line 4 : N integers which are elements of second array, separated by spaces
# Output Format :
# Maximum sum value
# Constraints :
# 1 <= M, N <= 10^6
# Sample Input :
# 6
# 1 5 10 15 20 25
# 5
# 2 4 5 9 15
# Sample Output :
# 81
# Explanation :
# We start from array 2 and take sum till 5 (sum = 11). Then we'll switch to array at element 10 and take till 15. So sum = 36. Now, no elements left in array after 15, so we'll continue in array 1. Hence sum is 81



def maxPathSum(arr1, arr2, m, n):
    i, j = 0, 0
    result, sum1, sum2 = 0, 0, 0
    while (i < m and j < n):
        if arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        elif arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        else:
            result += max(sum1, sum2) + arr1[i]
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1

    while i < m:
        sum1 += arr1[i]
        i += 1
    while j < n:
        sum2 += arr2[j]
        j += 1

    result += max(sum1, sum2)

    return result


def takeInput():
    n = int(input())
    elements = list(map(int, input().strip().split(" ")))

    return n, elements

# Main.


m, arr1 = takeInput()
n, arr2 = takeInput()

print(maxPathSum(arr1, arr2, m, n))
