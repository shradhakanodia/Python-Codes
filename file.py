fname=raw_input("enter file name:");
fp=open(fname,"r");
nl=0
nw=0
nc=0
alllines=fp.readlines();
for eachline in alllines:
	nl+=1
	nw+=len(eachline.split(" "))
	nc+=len(eachline)
print "no of line:",nl," words:",nw," characters:",nc
