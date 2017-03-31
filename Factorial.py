def factorial(num):
    if num == 0:
        return "Must pass a non zero, non negative integer"
    else:
        cnt = num - 1
        while cnt != 0:
            num = num * cnt
            cnt = cnt - 1
        return num