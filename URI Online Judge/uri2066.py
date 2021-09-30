def reverseN(n):
    revs_n = 0
    while (n > 0):
        # Logic
        remainder = n % 10
        revs_n = (revs_n * 10) + remainder
        n = n // 10
    return(revs_n) 

def isReversible(n):
    temp = reverseN(n)
    if n < temp:
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