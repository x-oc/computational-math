def get_det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def solve2(A, B):
    n = 2
    det = get_det2(A)
    det1 = get_det2([[B[r], A[r][1]] for r in range(n)])
    det2 = get_det2([[A[r][0], B[r]] for r in range(n)])
    return det1 / det, det2 / det


def get_det3(A):
    pos = A[0][0] * A[1][1] * A[2][2] + \
          A[0][1] * A[1][2] * A[2][0] + \
          A[0][2] * A[1][0] * A[2][1]
    neg = A[0][2] * A[1][1] * A[2][0] + \
          A[0][1] * A[1][0] * A[2][2] + \
          A[0][0] * A[1][2] * A[2][1]
    return pos - neg


def solve3(A, B):
    n = 3
    det = get_det3(A)
    det1 = get_det3([[B[r], A[r][1], A[r][2]] for r in range(n)])
    det2 = get_det3([[A[r][0], B[r], A[r][2]] for r in range(n)])
    det3 = get_det3([[A[r][0], A[r][1], B[r]] for r in range(n)])
    return det1 / det, det2 / det, det3 / det


def get_det4(A):
    n = 4
    sign = 1
    r = 0
    res = 0
    for c in range(n):
        A_ = [[A[r_][c_] for c_ in range(n) if c_ != c]
              for r_ in range(n) if r_ != r]
        res += sign * A[r][c] * get_det3(A_)
        sign *= -1
    return res


def solve4(A, B):
    n = 4
    det = get_det4(A)
    det1 = get_det4([[B[r], A[r][1], A[r][2], A[r][3]] for r in range(n)])
    det2 = get_det4([[A[r][0], B[r], A[r][2], A[r][3]] for r in range(n)])
    det3 = get_det4([[A[r][0], A[r][1], B[r], A[r][3]] for r in range(n)])
    det4 = get_det4([[A[r][0], A[r][1], A[r][2], B[r]] for r in range(n)])
    return det1 / det, det2 / det, det3 / det, det4 / det


def solve_sle(A, B, n):
    if n == 2:
        return solve2(A, B)
    if n == 3:
        return solve3(A, B)
    if n == 4:
        return solve4(A, B)
    print(f"! n должно быть 2/3/4, а получено {n}")
    return None
