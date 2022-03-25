'''
To accept from user the numberof Fibonacci numbers to be generated and print the Fibonacci Series.
'''


n = int(input("Enter the range: "))                         # accept range from user
a = 0
b = 1
li = []
for i in range(n):
	c = a + b                                               # calculate next number in series
	li.append(c)
	a = b                                                   # swapping operand for subsequent iterations
	b = c
print(li,' is the required fibonacci series')


'''
Enter the range: 10
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  is the required fibonacci series
'''
