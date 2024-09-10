def find_max_min(A):
    max_val = A[0]
    min_val = A[0]
    for i in range(1, len(A)):
        if A[i] > max_val:
            max_val = A[i]
        if A[i] < min_val:
            min_val = A[i]
    return max_val, min_val
def sum_negative_between_max_min(A):
    max_val, min_val = find_max_min(A)
    start = A.index(max_val)
    end = A.index(min_val)
    sum_negative = 0
    for i in range(start + 1, end):
        if A[i] < 0:
            sum_negative += A[i]
    return sum_negative