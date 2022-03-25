'''
To simulate simple calculator that performs basic tasks such as addition, subtraction,multiplication and division with special operations like computing x^y and x!.
'''


n = float(input("Enter the first number: "))                                        # menu driven program
n1 = float(input('Enter the second number: '))
s = int(input("Enter the operation[Add(1),Subtract(2),Divide(3),Multiply(4),Exponential(5),Factorial(6): "))
if s==1 :                                                                           # addition
   add = n + n1
   print(add,' is the sum of two number.')
elif s==2 :                                                                         # subtraction
   if n>n1:
     sub = n - n1
     print(sub, ' is the difference.')
   else:
     sub1 = n1-n
     print(sub1,' is the difference.')
elif s==3:                                                                          # division
   if n>n1:
     q = n/n1
     print(q,' is the quotient of the two number.')
   else:
     q1 = n1/n
     print(q1,' is the quotient of the two number.')
elif s==4:                                                                          # multiply
   m = n * n1
   print(m,' is the product of two numbers.')
elif s==5:                                                                          # compute exponential values
   p = int(input("Enter the exponential value: "))
   a = n**p
   a1 = n1**p
   print(a,'is the exponential of 1st no.& ',a1,' is exponential of 2nd no.')
elif s==6:                                                                          # compute factorial
   e = 1
   for i in range(1,int(n+1)):
      e = e*i
   print(e,' is the factorial of 1st number.')
   y = 1
   for i in range(1,int(n1+1)):
      y = y *i
   print(y,' is the factorial of 2nd number.')
else:
   print(' ')


'''
Enter the first number: 45
Enter the second number: 36
Enter the operation[Add(1),Subtract(2),Divide(3),Multiply(4),Exponential(5),Factorial(6): 1
81.0  is the sum of two number.

Enter the first number: 563
Enter the second number: 458
Enter the operation[Add(1),Subtract(2),Divide(3),Multiply(4),Exponential(5),Factorial(6): 2
105.0  is the difference.

Enter the first number: 563
Enter the second number: 789
Enter the operation[Add(1),Subtract(2),Divide(3),Multiply(4),Exponential(5),Factorial(6): 3
1.4014209591474245  is the quotient of the two number.

Enter the first number: 458
Enter the second number: 312
Enter the operation[Add(1),Subtract(2),Divide(3),Multiply(4),Exponential(5),Factorial(6): 4
142896.0  is the product of two numbers.

Enter the first number: 45
Enter the second number: 36
Enter the operation[Add(1),Subtract(2),Divide(3),Multiply(4),Exponential(5),Factorial(6): 5
Enter the exponential value: 4
4100625.0 is the exponential of 1st no.&  1679616.0  is exponential of 2nd no.

Enter the first number: 23
Enter the second number: 10
Enter the operation[Add(1),Subtract(2),Divide(3),Multiply(4),Exponential(5),Factorial(6): 6
25852016738884976640000  is the factorial of 1st number.
3628800  is the factorial of 2nd number.
'''


   
