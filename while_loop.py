Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class yar():
	global x
	x = 5
	def check(x):
		while x > 0:
			x -= 1
			if (bool(x>=5)):
				print(x)
			elif (bool(x>=4)):
				print(x)
			elif (bool(x>=3)):
				print(x)
			elif (bool(x>=2)):
				print(x)
			elif (bool(x>=1)):
				print(x)
			else:
				print('')
