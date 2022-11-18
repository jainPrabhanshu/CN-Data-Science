# Print the following pattern for the given number of rows.
# Pattern for N = 4

# The dots represent spaces.

# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints :
# 0 <= N <= 50

# Sample Input 1:
# 5
# Sample Output 1:
#            1
#          232
#        34543
#      4567654
#    567898765

# Sample Input 2:
# 4
# Sample Output 2:
#            1
#          232
#        34543
#      4567654

n = int(input())
currRow = 1
while currRow <= n:
    spaces = 1
    while spaces <= (n - currRow):
        print(" ", end="")
        spaces += 1
    currCol = 1
    valToPrint = currRow
    while currCol <= currRow:
        print(valToPrint, end="")
        valToPrint += 1
        currCol += 1
    currCol = 1
    valToPrint = 2 * currRow - 2
    while currCol <= currRow - 1:
        print(valToPrint, end="")
        valToPrint -= 1
        currCol += 1
    print()
    currRow += 1

