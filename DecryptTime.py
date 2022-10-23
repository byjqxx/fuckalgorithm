"""
https://blog.nowcoder.net/n/6fa75be72d684be6a3e8830af1d2ff46
从输入的时间中拼出，比输入时间新的，最小的一个时间
比如 22:19  --> 22:21   23:59 --> 22:22
"""


def get_real_time(t):
    nums = [int(i) for i in t if i != ":"]
    h, m = [int(i) for i in t.split(":")]
    time = []

    # 将拼接后的数字放入time中
    for i in nums:
        for j in nums:
            time.append(str(i) + str(j))
    time_m = []
    time_h = []

    # 从输入的时间的数字中拼出比原分钟数m大且有效的分钟数，加入到time_m中
    for i in range(len(time)):
        if int(time[i]) > m and int(time[i]) <= 59:
            time_m.append(time[i])

    # 如果time_m不为空，则可以将time_m排序
    # 将原来的小时数h和time_m中最小的分钟数time_m[0]拼接输出
    if len(time_m) > 0:
        time_m.sort()
        # 根据原来小时数h的位数进行格式化输出
        if h < 10:
            return "0" + str(h) + ":" + time_m[0]
        else:
            return str(h) + ":" + time_m[0]
    # 如果time_m为空，说明拼接的分钟数没有比原来分钟数m大的
    # 需要找一个比原来h大的小时数，才能拼接出比原来时间新的最小的时间
    else:
        for i in range(len(time)):
            if int(time[i]) > h and int(time[i]) <= 23:
                time_h.append(time[i])
        # 如果能在time里找到比h大的数字，则用h加min(time)拼接
        if len(time_h) > 0:
            time_h.sort()
            return str(time_h[0]) + ":" + str(min(time))
        # 如果没有比h大的时间数，则需要找一个最小的时间数和分钟数拼接
        else:
            return str(min(time)) + ":" + str(min(time))


origin_time = input()
real_time = get_real_time(origin_time)
print(real_time)
