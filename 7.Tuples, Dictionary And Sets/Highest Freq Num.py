# You are given an array of integers that contain numbers in random order. Write a program to find and return the number which occurs the maximum times in the given input.
# If two or more elements contend for the maximum frequency, return the element which occurs in the array first.
# Input Format:
# The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
# The following line contains N space separated integers, that denote the value of the elements of the array.
# Output Format :
# The first and only line of output contains most frequent element in the given array.
# Constraints:
# 0 <= N <= 10^8
# Time Limit: 1 sec
# Sample Input 1 :
# 13
# 2 12 2 11 12 2 1 2 2 11 12 2 6 
# Sample Output 1 :
# 2
# Sample Input 2 :
# 3
# 1 4 5
# Sample Output 2 :
# 1

from sys import stdin

MIN_VALUE=-99999999
def maxfreq(test_list):
    d={}
    for i in test_list:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    max=0
    maxKey=MIN_VALUE
    for i in range(len(test_list)):
       	if d[test_list[i]]>max:
            max=d[test_list[i]]
            maxKey=test_list[i]
    return maxKey


def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))