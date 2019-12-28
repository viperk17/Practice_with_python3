# Task
# Read an integer . For all non-negative integers , print
#
# . See the sample for details.


# Output Format
#
# Print
# lines, one corresponding to each
#
# .
#
# Sample Input 0
#
# 5
#
# Sample Output 0
#
# 0
# 1
# 4
# 9
# 16
import os

if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i * i)
print()
