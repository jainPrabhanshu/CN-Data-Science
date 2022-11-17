# Sum of Even Numbers
# Send Feedback
# Given a number N, print sum of all even numbers from 1 to N.
# Input Format :
# Integer N
# Output Format :
# Required Sum 
# Sample Input 1 :
#  6
# Sample Output 1 :
# 12

num = int(input())
sum = 0
for i in range(1, num+1):
    if i % 2 == 0:
        sum += i

print(sum)
