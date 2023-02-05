# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    answer = 0
    maxturn = 0

    for pos, j in enumerate(A):
        # print(maxturn, j)
        maxturn = max(j, maxturn)
        if maxturn == pos + 1:
            answer += 1
    return answer
