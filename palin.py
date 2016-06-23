import string
def palindrome(word):
	rev=""
	for i in word:
		rev=i+rev

	if word==rev:
		print word," is palindrome"
	else:
		print word," is not palindrome"

str=raw_input("enter string")
words=str.split(" ")
for w in words:
	palindrome(w) 
		
