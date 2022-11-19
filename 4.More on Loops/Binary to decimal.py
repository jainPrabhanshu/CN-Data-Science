# Given a binary number as an integer N, convert it into decimal and print.
# Input format :
# An integer N in the Binary Format
# Output format :
# Corresponding Decimal number (as integer)
# Constraints :
# 0 <= N <= 10^9
# Sample Input 1 :
# 1100
# Sample Output 1 :
# 12
# Sample Input 2 :
# 111
# Sample Output 2 :
# 7    
## Read input as specified in the question.
## Print output as specified in the question.



num=int(input())
i=0
sum=0
while num!=0:
    r=num%10
    sum+=r*(2**i)
    num=num//10
    i+=1
print(sum)