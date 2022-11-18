# Print the following pattern
# Pattern for N = 4

# The dots represent spaces.

# Input Format :
# N (Total no. of rows)
# Output Format :
# Pattern in N lines
# Constraints :
# 0 <= N <= 50
# Sample Input 1 :
# 3
# Sample Output 1 :
#    *
#   *** 
#  *****
# Sample Input 2 :
# 4
# Sample Output 2 :
#     *
#    *** 
#   *****
#  *******

n = int(input())
i = 1
while i <= n:
    spaces = n - i
    while spaces > 0:
        print(" ", end='')
        spaces -= 1
    stars = (2 * i) - 1
    while stars:
        print("*", end='')
        stars -= 1
    print()
    i = i + 1 