import sys

input = sys.stdin.readline
write = sys.stdout.write

MOD = 2010

def reduce_shift(t):
    if t <= 11:
        return t
    return 2 + ((t - 2) % 10)


def apply_shift(node, t, seg, lazy):
    t = reduce_shift(t)
    if t == 0:
        return
    old = seg[node]
    new = [0] * 12
    for k in range(12):
        idx = k + t
        if idx <= 11:
            new[k] = old[idx]
        else:
            new[k] = old[2 + ((idx - 2) % 10)]
    seg[node] = new
    lazy[node] = reduce_shift(lazy[node] + t)


def build(node, l, r, arr, seg):
    if l == r:
        seq = [0] * 12
        seq[0] = arr[l]
        for i in range(1, 12):
            v = seq[i - 1]
            seq[i] = (v * v) % MOD
        seg[node] = seq
        return
    mid = (l + r) // 2
    build(node * 2, l, mid, arr, seg)
    build(node * 2 + 1, mid + 1, r, arr, seg)
    left = seg[node * 2]
    right = seg[node * 2 + 1]
    seg[node] = [left[i] + right[i] for i in range(12)]


def push(node, seg, lazy):
    if lazy[node]:
        apply_shift(node * 2, lazy[node], seg, lazy)
        apply_shift(node * 2 + 1, lazy[node], seg, lazy)
        lazy[node] = 0


def update(node, l, r, ql, qr, seg, lazy):
    if ql <= l and r <= qr:
        apply_shift(node, 1, seg, lazy)
        return
    push(node, seg, lazy)
    mid = (l + r) // 2
    if ql <= mid:
        update(node * 2, l, mid, ql, qr, seg, lazy)
    if qr > mid:
        update(node * 2 + 1, mid + 1, r, ql, qr, seg, lazy)
    left = seg[node * 2]
    right = seg[node * 2 + 1]
    seg[node] = [left[i] + right[i] for i in range(12)]


def query(node, l, r, ql, qr, seg, lazy):
    if ql <= l and r <= qr:
        return seg[node][0]
    push(node, seg, lazy)
    mid = (l + r) // 2
    total = 0
    if ql <= mid:
        total += query(node * 2, l, mid, ql, qr, seg, lazy)
    if qr > mid:
        total += query(node * 2 + 1, mid + 1, r, ql, qr, seg, lazy)
    return total


n_line = input().strip()
if n_line:
    n = int(n_line)
    arr = [0] + list(map(int, input().split()))
    m = int(input())
    seg = [[0] * 12 for _ in range(4 * n)]
    lazy = [0] * (4 * n)
    build(1, 1, n, arr, seg)

    out = []
    for _ in range(m):
        ops, l, r = map(int, input().split())
        if ops == 1:
            update(1, 1, n, l, r, seg, lazy)
        else:
            out.append(str(query(1, 1, n, l, r, seg, lazy)))
    write("\n".join(out))
