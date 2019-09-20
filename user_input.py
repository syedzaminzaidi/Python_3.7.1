Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class cal():
	global x
	x = input ('enter your name')
	global y
	y = input ('enter your value')
	sum = int(x) + int(y)
	#def fun(x,y):
	print (x)
	print (y)
	print ('The sum is {0} and {1} is {2}'.format(x,y,sum))
	#return x,y
