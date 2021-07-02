digits = []
while True:
    try:
        line = input('Please input integer')
        if line:
            number = int(line)
            digits.append(number)
        else:
            break
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break
if len(digits) > 0:
    countd = len(digits)
    for j in range(len(digits) - 1, 0, -1):
        for i in range(j):
            if digits[i] > digits[i + 1]:
                digits[i], digits[i + 1] = digits[i + 1], digits[i]
    sumd = sum(digits)
    index = int(len(digits) / 2)
    median = digits[index]
    if index and index * 2 == len(digits):
        median = (median + digits[index - 1]) / 2
    print(digits)
    print("Count: " + str(countd))
    print('Min: ' + str(min(digits)))
    print('Max: ' + str(max(digits)))
    print('Avr' + str(sum(digits) / len(digits)))
    print('Sum' + str(sumd))
    print('Median' + str(median))
