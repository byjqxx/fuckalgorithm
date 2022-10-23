"""
https://blog.nowcoder.net/n/6fa75be72d684be6a3e8830af1d2ff46
"""
def get_real_time(t):
    nums = [int(i) for i in t if i != ":"]
    h, m = [int(i) for i in t.spilt(":")]
    time = []

    for i in nums:
        for j in nums:
            time.append(str(i) + str(j))
    time_m = []
    time_h = []

    for i in range(len(time)):
        if int(time[i]) > m and int(time[i]) <= 59:
            time_m.append(time[i])

    if len(time_m) > 0:
        time_m.sort()
        if h < 10:
            return "0" + str(h) + ":" + time_m[0]
        else:
            return str(h) + ":" + time_m[0]
    else:
        for i in range(len(time)):
            if int(time[i]) > h and int(time[i]) <= 23:
                time_h.append(time[i])
        if len(time_h) > 0:
            time_h.sort()
            return str(time_h[0]) + ":" + str(min(time))
        else:
            return str(min(time)) + ":" + str(min(time))

origin_time = input()
real_time = get_real_time(origin_time)
print(real_time)