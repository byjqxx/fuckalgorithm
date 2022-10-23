"""
找朋友
https://www.cnblogs.com/xycbq/p/16195464.html
https://blog.csdn.net/weixin_39772200/article/details/107728832
https://blog.csdn.net/weixin_47243236/article/details/122556082
"""
n = int(input())
height = input()
height = [int(x) for x in height.split()]
result = []

# 为第一个到倒数第二个人找朋友
for i in range(len(height)-1):
    # 为 i 找朋友时，遍历 i 之后的人（i+1，n）即可
    for j in range(i+1, len(height)):
        # i之后，第一个身高比 i 高的人j，即为 i 的朋友
        # 找到之后，记录下i朋友j的位置
        print(i, j)
        if height[j] > height[i]:
            result.append(j)
            break
    # 一次循环完，不符合上面条件后，说明i没找到朋友
    # 将 i 的朋友的位置置为0
    else:
        result.append(0)

# 最后一个人，由于后面没有人了，所以不用找,最后一个人的朋友位置置为0
result.append(0)
for num in result:
    print(num, end=" ")
