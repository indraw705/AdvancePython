# WS  MS  AI       AI  MS  WS
# 1   2   3        4   5   6
# 12  11  10       9   8   7
# 13  14  15       16  17  18


num = int(input("enter your seat  \n"))

if (num + 1) % 3 == 0:
    print("you have middle seat")
elif num % 6 == 0 or (num - 1) % 6 == 0:
    print("you have Window seat")
elif num % 3 == 0 or (num - 1) % 3 == 0:
    print("you have AI seat")
