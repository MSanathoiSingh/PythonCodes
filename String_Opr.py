'''
Write a python program that accepts a string from user and perform following string operations:
(i) Calculate length of string,
(ii) String reversal,
(iii) Equality check of two strings,
(iv) Check for palindrome, and,
(v) Check substring.
'''


s = input("Enter the string: ")                                     #input() is used to accept entity from the user.
li = list(s)                                                        #list() is used to create an empty list.
print(len(li)," is the length of the string entered.")
l = [] 

for i in reversed(li):                                              #reversed() returns reverse value of parameter passed 
	l.append(i) 
a = ""
sp = a.join(l)                                                      #join() is used to join list element to form string.
print(sp," is the reverse of the string entered.")

s2 = input("Enter the other string: ")
if s==s2:                                                           #check if 2 strings are equal or not
	print("The two strings are equal.")
else:
	print("The strings are not equal.")

s3 = input("Enter the string to be checked for palindrome: ")       #palindrome check
l1 = list(s3)
l2 = []
for q in reversed(l1):
	l2.append(q)
a1 = ''
sq = a1.join(l2)
if sq==sp:                                                          #'==' is a relational operator
	print("The string is a palindrome.")
else:
	print("The string is not a palindrome.")

s3 = input("Enter substring: ")                                     #substring check
l3 = list(s3)
if s3 in s:                                                         #'in' is a membership operator
	print("Entered string is a substring.")
else:
	print("Entered string is not a substring.")


'''
Enter the string: Sourabh
7  is the length of the string entered.
hbaruoS  is the reverse of the string entered.
Enter the other string: Tanmay
The strings are not equal.
Enter the string to be checked for palondrome: Sourabh
The string is a palindrome.
Enter substring: hb
Entered string is not a substring.
'''



