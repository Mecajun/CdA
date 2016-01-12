
linha={}

while True:
	a=ser.readline()
	print a
	print a=="to mandando matricula"
	if a=="to mandando matricula":
		linha['matricula']=ser.readline()
		linha['soma']=-1
	a=ser.readline()
	if a=="to mandando soma":
		linha['soma']=int(ser.readline())
	soma=0
	for i in linha['matricula']:
		if i>='0' and i<='9':
			soma=soma+int(i)
	print soma==linha['soma']
	print linha['matricula']
