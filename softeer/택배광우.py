import sys
import itertools

n, m, k = map(int, input().split())
packs = map(int, input().split())
packs_all_lst = list(itertools.permutations(packs, n))


def algorithm(rails, busket, k, packs_all_lst):
    min_total = 2500

    for i in packs_all_lst:
        work_cnt = 0
        index = 0
        current = 0
        total_weight = 0
        temp = 0

        while True:
            if total_weight > min_total:
                break

            if work_cnt < k:
                temp += i[index % rails]
                if temp > busket:
                    work_cnt += 1
                    total_weight += current
                    temp = 0
                    current = 0
                else:
                    current += i[index % rails]
                    index += 1

            else:
                min_total = min(min_total, total_weight)
                break

    return min_total


# print(list(packs_all_lst))
min_total = algorithm(n, m, k, packs_all_lst)

print(min_total)
# algorithm(n,m,k,packs_all_lst)