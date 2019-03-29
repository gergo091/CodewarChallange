def order_weight(strng):
    number = []
    sum = []
    try:
        number = map(int, sorted(strng.split(' ')))
    except ValueError as e:
        print("You didn't enter a number! Shame on you.")

    for i in number:
        sum.append(digit_sum(i))

    for passnum in range(len(sum)-1,0,-1):
        for n in range(passnum):
            if sum[n] > sum[n + 1]:
                a = sum[n]
                sum[n] = sum[n + 1]
                sum[n +1] = a
                b = number[n]
                number[n] = number[n + 1]
                number[n + 1] = b
    result = []
    for s in number:
        result.append(str(s))
    return ' '.join(result)

def digit_sum(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum

if __name__ == "__main__":
    print order_weight("103 123 4444 99 2000")
    print order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
    #Test.it("Basic tests")
    #Test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
    #Test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
