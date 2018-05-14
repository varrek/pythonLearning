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
	sumd = sum(digits)
	countd = len(digits)
	print(digits)
	print("Count: " + str(countd))
	print('Min: ' + str(min(digits)))
	print('Max: ' + str(max(digits)))
	print('Avr' + str(sum(digits) / len(digits)))
	print('Sum' + str(sumd))

