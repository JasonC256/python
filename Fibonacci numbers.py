

def test(num):
	if(num % 2) == 0:
		return True
	else:
		return False

a = 1
b = 1
js = 2
sum_even = 0
print(a)
print(b)
while True:
	if js < 4000000:
		c = a + b
		print(c)
		if test(c) == True:
			sum_even += c
		a = b
		b = c
		js += 1
	else:
		break
print("\n")
print(c)
print("\n")
print("sum_even:" + str(sum_even))







