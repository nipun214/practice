# First line take a number of country and if the country is repeating in list don't count that county and last give how many unique country are there
# Example:
# Line1: 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 

# Ans: 5


c=[]
a = int(input())
for i in range(0,a):
    ele= str(input())
    c.append(ele)
total = len(c)

if total==0:
    print()
if total<=1:
    print(total)

for j in range(len(c)):
    for k in range(j):
        if c[j]==c[k]:
            total = total-1
print(total)


-----OR-------

# n,s= int(input()),set()
# for i in range(n):
#     s.add(input())
# print(len(s))