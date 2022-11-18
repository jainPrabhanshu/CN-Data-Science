# Print the following pattern for the given number of rows.
# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

# Input format :
# N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 26

# Sample Input 1:
# 8
# Sample Output 1:
# H
# GH
# FGH
# EFGH
# DEFGH
# CDEFGH
# BCDEFGH
# ABCDEFGH

# Sample Input 2:
# 7
# Sample Output 2:
# G
# FG
# EFG
# DEFG
# CDEFG
# BCDEFG
# ABCDEFG


n = int(input())
i = 1
while i <= n:
    j = 1
    startChar = chr(ord('A') + n - i)
    while j <= i:
        char = chr(ord(startChar) + j - 1)
        print(char, end='')
        j = j + 1
    print()
    i = i + 1