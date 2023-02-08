def timeSplit(time):
    h,m,s = list(map(int,time.split(":")))
    return (h*60*60)+(m*60)+s
def timeTrans(time):
    h = time//3600
    time %=3600
    m = time//60
    time %=60
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(time).zfill(2)
def solution(play_time, adv_time, logs):
    view_arr = [0] * (timeSplit(play_time) + 1)
    
    for i in logs:
        start, end = i.split("-")
        start_sec = timeSplit(start)
        end_sec = timeSplit(end)
        view_arr[start_sec] +=1
        view_arr[end_sec] -=1
    
    for j in range(1,len(view_arr)):
        view_arr[j] += view_arr[j-1]
    prefix_sum = [0]
    total = 0
    for i in range(len(view_arr)):
        total += view_arr[i]
        prefix_sum.append(total)  
    adv_time = timeSplit(adv_time)
    
    max_time = 0
    answer = 0
    for i in range(len(view_arr)):
        if i+1+adv_time >= len(prefix_sum):
            break
        insert_time = prefix_sum[i+adv_time] - prefix_sum[i]
        if insert_time > max_time:
            max_time = insert_time
            answer = i
    return timeTrans(answer)


solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])