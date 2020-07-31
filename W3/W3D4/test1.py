def do_test(*k):
    sum = 0
    for i in k:
        sum += i
    return sum

print(do_test(300,100,200,300))