for i in range(1,101):
    if i%7==0:
	i=i+1
        continue
    elif i%7==7 or i//10==7:
	i=i+1
	continue
    else:
	print(i)
