def get_rand_mobile(start='13'):

	# 以start开头，后面跟一位4~9之间的任意一位数字，后面是8位随机数字
	temp = (start + str(random.randrange(4, 10)) +
		''.join(str(random.choice(range(10))) for _ in range(8)))

	return temp