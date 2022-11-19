# Find and return number of trailing 0s in n factorial without calculating n factorial.
# Sample Input
# 50
# Sample Output
# 12
# Input Size Limit
# n < 10^"11



n=int(input())
if(n < 0):
    print(-1)

count = 0

while(n >= 5):
    n //= 5
    count += n

print(count)