'''
To check whether input number is Armstrong's number or not.
An Armstrong's numer is an integer with three digits such that the sum of cubes of its digits is equal to the number itself.
'''


no = int(input("Enter the number to be tested "))           #int(input) is an function used to accept number form the user.
li = [int(d) for d in str(no)]                              #[ ] denotes a list of similar or dissimilar enitities.
print(li)                                                   #print fn is ued to display the number on the screen.
s=0
for p in li:                                                #for is a function used for using iteration.
 s += p**3
print (s)
if s == no :                                                #used to test a particular condition
 print("The number is an Armstrong's Number.")
else :
 print("The number is not an Armstrong's Number.")


'''
Enter the number to be tested 370
[3, 7, 0]
370
The number is an Armstrong's Number.

Enter the number to be tested 562
[5, 6, 2]
349
The number is not an Armstrong's Number.
'''




