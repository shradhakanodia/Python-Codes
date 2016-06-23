sarr=raw_input("enter string to sort:")

for i in range(len(sarr)):
	for j in range(len(sarr)-1):
		if(sarr[j]>sarr[j+1]):
			sarr=sarr[:j]+sarr[j+1]+sarr[j]+sarr[j+2:]

print sarr

str=raw_input("enter string to sort:")
sarr=str.split(" ")
for i in range(len(sarr)):
	for j in range(len(sarr)-1):
		if(sarr[j]>sarr[j+1]):
			(sarr[j],sarr[j+1])=(sarr[j+1],sarr[j])

for i in range(len(sarr)):
	print sarr[i]+" "

