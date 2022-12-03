# Find number of elements to be removed to make an array of all distinct elements.
# Example:
# Ar = {2,1,4,2,1} 
# output = 2 (remove 2 and 1).
# Input format :
# Line 1 : Integer N 
# Line 2 : N integers separated be a single space
# Output Format :
#  Integer
# Constraints :
#  0 <= N <= 10^4
# Sample Input :
# 5
# 2 1 4 2 1
# Sample Output :
# 2

def duplicateCount(arr):
    s = set()
    for i in arr:
        s.add(i)
    return (len(arr) - len(s))

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(duplicateCount(arr))
