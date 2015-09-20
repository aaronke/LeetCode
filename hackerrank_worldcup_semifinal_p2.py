# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
A = map(int, raw_input().strip().split(' '))
all_size = [2**i for i in range(n)] # use this size for each round DP reuse
def helper(A):
    this_level = []
    for i in range(1,n+1):
        if i == 1:
            this_level.append(A[0])
            continue
        last = A[i-1]
        mask = A[i-1]
        # direct copy past results
        for k in range(all_size[i-2]):
            this_level[k] ^= A[i-1]
        # recursive copy
        for j in range(2,i):
            last += A[i-j]
            mask ^= A[i-j]
            for kk in range(all_size[i-j-1]):
                pre_level = this_level[kk]
                this_level.append(last^pre_level^mask)
        this_level.append(sum(A[:i]))
    return this_level


result = helper(A)
count = 0
for i in result:
    if i == 0:
        count+=1
print count
