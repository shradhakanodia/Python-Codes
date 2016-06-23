num=int(raw_input("enter a number"));
sumfactor=0
for i in range(1,num):
	if num%i==0:
		sumfactor+=i
if sumfactor==num:
	print num," is perfect"
else:
	print num," is not perfect"

	
