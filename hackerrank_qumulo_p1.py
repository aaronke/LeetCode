"""
N children forming a circle. Counting from the first one, 'one', 'two', 'three'... until find 'M-th', then
remove this child, and start counting 'one' again from the next child.
In the end, only M-1 children should remain in the circle as the winner.（人赢）
input:
5
3
output:
2
4
"""
N = int(raw_input())
M = int(raw_input())

if N < 1 or M < 1 or M > N+1:
    pass
else:
    children = [i for i in xrange(1,N+1)]
    slow, mid, fast = 0, 0, 0
    count = N
    result = []
    while count != M-1:
        if children[(slow+mid+fast)%N] == -1:
            mid += 1
            continue
        if fast == M-1:
            children[(slow+mid+fast)%N] = -1
            slow, mid, fast = (slow+mid+fast)%N, 0, 0
            count -= 1
        else:
            fast += 1

    for i in children:
        if i != -1:
            result.append(i)

    for i in result:
        print i
