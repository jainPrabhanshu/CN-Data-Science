# Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
# Input format :
# Integer x
# Output format :
# Terms of series (separated by space)
# Constraints :
# 1 <= x <= 1,000

# Sample Input 1 :
# 10
# Sample Output 1 :
# 5 11 14 17 23 26 29 35 38 41

# Sample Input 2 :
# 4
# Sample Output 2 :
# 5 11 14 17

n=int(input())
count=0
flag=True
k=1
while flag:
    x=3*k+2
    if x%4!=0:
        print(x,end=' ')
        count+=1
    k+=1
    if count==n:
        flag=False