def program(**a):
	print(type(a))
	for k,v in a.items():
		print(k,":",v)
program(name="Vijay",college="CBIT",Roll=102)