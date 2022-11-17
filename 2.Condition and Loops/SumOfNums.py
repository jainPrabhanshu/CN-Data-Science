# Sum of n numbers
# Send Feedback
# Given an integer n, find and print the sum of numbers from 1 to n.
# Note : Use while loop only.
# Input Format :
# Integer n
# Output Format :
# Sum
# Constraints :
# 1 <= n <= 100
# Sample Input :
# 10
# Sample Output :


n = int(input())
total_sum = 0
i = 1
while i <= n:
    total_sum += i
    i = i + 1
print(total_sum)