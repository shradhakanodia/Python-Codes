import string
str=raw_input("enter a string");
alpha=string.letters+"_"
digits=string.digits

if str[0] not in alpha:
	print "invalid identifier"
else:
	for i in str[1:]:
		if i not in alpha+digits:
			print "invalid identifier"
			break
	else:
		print "valid identifier"
		
		


