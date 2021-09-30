def reverseN(x):
    return (x[::-1])

def isReversible(n):
    temp = int(reverseN(str(n)))
    if n<temp:
        return True
    else:
        return False

count = 0
i = int(input())
i = i*'9'

max = int(i)

for n in range(max+1):
    if isReversible(n):
        count = count + 1

print(count)
# print(count)
# count = 0
# reverse = list(range(i))

# for i in reverse:
#     if i 

# for reverse in range(i):
#     if n > reverseN(n):
#         count = count+1

# print(count)
# # max = reverseN(max)
# print(max)
