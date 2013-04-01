def check_string(str):
	n = len(str)

	for i in range(0,n-1):
		if str[i] == str[(n-1)-i]:
			pass
		else:
			return 0	
	
	return 1



check = raw_input('input string :')
result = check_string(check)

if result == 1:
	print 'same'
elif result == 0:
	print 'different'