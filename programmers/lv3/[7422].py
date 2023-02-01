def timeSet(time):
    h,h2 = divmod(time,3600)
    m,m2 = divmod(h2,60)
    s,s2 = divmod(m2,60)
    if len(str(h)) == 1 : 
        h ="0"+str(h)
    if len(str(m)) == 1 : 
        m ="0"+str(m)
    if len(str(s2)) == 1 : 
        s2 ="0"+str(s)        
    return str(h)+":"+str(m)+":"+str(s2)
def ssplit(time):
    h,m,s = list(map(int,time.split(":")))
    return h*60*60 + m*60 + s
def solution(play_time, adv_time, logs):
    view_arr = [0] * (ssplit(play_time) + 1)
    
    for i in logs:
        start, end = i.split("-")
        start_sec = ssplit(start)
        end_sec = ssplit(end)
        view_arr[start_sec] +=1
        view_arr[end_sec] -=1
    
    for j in range(1,len(view_arr)):
        view_arr[j] += view_arr[j-1]
    
    prefix_sum = [0]
    total = 0
    for i in range(len(view_arr)):
        total += view_arr[i]
        prefix_sum.append(total)  
    adv_time = ssplit(adv_time)

    max_time = 0
    answer = 0
    for i in range(len(view_arr)):
        if i+1+adv_time >= len(prefix_sum):
            break
        insert_time = prefix_sum[i+adv_time] - prefix_sum[i]
        if insert_time > max_time:
            max_time = insert_time
            answer = i
    return timeSet(answer)


solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])