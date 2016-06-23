fp=open("file2.txt","w+")
i=1
print "enter 4 lines to enter into file" 
while i<=4:
	line=raw_input("")+"\n"
	fp.write(line);
	i+=1
fp.seek(0,0)
lines=fp.readlines()
n=len(lines)
for i in range(n):
	if (i+1)%2!=0:
		print lines[i].upper()	
