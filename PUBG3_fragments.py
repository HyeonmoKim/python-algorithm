# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    temp = A
    temp.sort()
    if temp[0] == temp[-1]:
        return -1

    dict = {}
    temp = []
    part_sum = 0

    for i in range(len(A)):
        part_sum += A[i]

        if part_sum == 0:
            temp.append((0, i))

        # dp
        dp = []
        if part_sum in temp:
            dp = temp[part_sum]
            n = len(dp)
            for j in range(0, n):
                temp.append((dp[j] + 1, i))

        dp.append(i)
        dict[part_sum] = dp

    return len(dict)


def for_solution(A):
    # write your code in Python 3.6
    answer = 0

    for i in range(0, len(A)):
        for j in range(i, len(A)):
            total_sum = 0

            for k in range(i, j + 1):
                total_sum += A[k]

            if (total_sum == 0):
                answer += 1
            if answer > 1000000000:
                return -1
    return answer
