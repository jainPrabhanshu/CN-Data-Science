# You are given n triangles. You are required to find how many triangles are unique out of given triangles. For each triangle you are given three integers a, b and c (the sides of a triangle).
# A triangle is said to be unique if there is no other triangle with same set of sides.
# In other words, we have to find frequency of each triangle and return the count of triangles whose frequency is 1.
# Note : It is always possible to form triangle with given sides.
# Input Constraints :
# Line 1 : Integer n, the number of triangles
# Next n lines : Three integers a,b,c (sides of a triangle).
# Output Format :
# print single integer, the number of unique triangles.
# Constraints :
# 1 <= n <= 10^4
# 1 <= a,b,c <= 10^15.
# Sample Input :
# 5
# 7 6 5
# 5 7 6
# 8 2 9
# 2 3 4
# 2 4 3
# Sample Output :
# 1
# Explanation:
# The answer will be 1, as there is only one triangle with unique set of sides. There are three triangles here: Triangle with sides 2, 3, 4 and Triangle with sides 5, 6, 7 and Triangle with sides 2, 8, 9. The frequency of first two triangles is 2 and the frequency of last triangle is 1. Hence, there is only one triangle with frequency equal to 1.

## Read input as specified in the question.
## Print output as specified in the question.
#Taking Input Using Fast I/O
def uniqueTriangle(arr):
  row = len(arr)
  col = len(arr[0])
  mp = {}
  hel = {}

  for i in range(row):
    tri = arr[i]
    tri.sort()
    strA = [str(x) for x in tri]
    strB = ''
    strB = strB.join(strA)
    if strB not in mp.values():
      mp[i] = strB
    else:
      hel[i] = strB

  count = 0
  for i in range(row):
    if i in mp:
      val = mp.get(i)
      if val not in hel.values():
        count = count + 1

  print (count)


def takeInput():
    # n = int(input())
    elements = list(map(int, input().strip().split(" ")))

    return elements

# Main.

num = int(input())
arr=[]
for i in range(num):
	arr.append(takeInput())
    
uniqueTriangle(arr)