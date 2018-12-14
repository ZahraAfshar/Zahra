from math import log
from math import floor
def kill1(n, k):
    p, i, seq = list(range(n)), 0, [ ]
    while p:
        i = (i + k - 1) % len(p)
        seq.append(p.pop(i))
    return 'Killing order: %s.\nSurvivor: %i\n' % (', '.join(str(i) for i in seq[:-1]), seq[-1])
def kill2(n,k):
    r=0
    for i in range(1, n + 1):
        r = (r + k) % i
    return 'Survivor:%i' % r
def kill3(n):
    return int(2 * (n - 2 ** (floor(log(n, 2)))))