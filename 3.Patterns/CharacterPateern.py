# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# A
# BC
# CDE
# DEFG

# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 13

# Sample Input 1:
# 5
# Sample Output 1:
# A
# BC
# CDE
# DEFG
# EFGHI

# Sample Input 2:
# 6
# Sample Output 2:
# A
# BC
# CDE
# DEFG
# EFGHI
# FGHIJK


num=int(input())
for i in range(1,num+1):
    k=i
    for j in range(1,i+1):

        print(chr(64+k),end='')
        k+=1
    print()