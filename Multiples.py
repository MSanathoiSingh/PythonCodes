'''
To accept two number from user and compute smallest divisor and greatest common divisor of these two numbers.
'''


x = int(input("Enter the first number "))   
y = int(input("Enter the second number "))

for n in range(2,min(x,y)+1):                                                   #used for using iteration.
 if x%n==0 and y%n==0:                                                          #used to test a condition
  print("The common lowest divisor for 'x' and 'y' is ",n)  
  break
 else:                                                                          #used if a given condition is false.
  print('No common lowest multiple found for the combination.')

for m in range(min(x,y),1,-1):
 if x%m==0 and y%m==0:                                                          #% returns the value of remainder only.
  print("The greatest common multiple for 'x' and 'y' is ",m)
  break #'break' statement is used to exit the control from the loop.
 else:
  print("No common greatest multiple found for the given combination.")


'''
Enter the first number 864
Enter the second number 128
The common lowest divisor for 'x' and 'y' is  2
The greatest common multiple for 'x' and 'y' is  32

Enter the first number 458
Enter the second number 253
No common lowest multiple found for the combination.
No common greatest multiple found for the given combination.
'''






