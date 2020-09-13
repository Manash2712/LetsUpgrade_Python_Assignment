for i in range(104200,702648266):
    order = len(str(i))
    num = 0
    b = i
    while b>0:
        dig = b%10
        b //= 10
        num +=dig**order
    if num == b:
        print(num)
        break
