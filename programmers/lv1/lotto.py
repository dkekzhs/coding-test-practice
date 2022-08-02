def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))
    print(cnt)
    zero_cnt = lottos.count(0)

    answer =  [7 - max(cnt+zero_cnt,1 ), 7 -max(cnt ,1)]
    return answer

solution(	[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
