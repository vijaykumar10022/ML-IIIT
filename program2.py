try:
	a=input("Enter Value :")
	b=5
	c=a+b
except TypeError:
	c=int(a)+b
	print(c)
except ValueError:
	c=int(a)+b	#optional
	print(c)
else:
	z=11
	h=32
	print(z+h)
finally:
	e=7
	f=8
	g=e*f
	print(g)

	
