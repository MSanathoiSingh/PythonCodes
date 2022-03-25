'''
To accpet the number and compute,
(a) Square root of number,
(b) Square of number,
(c) Cube of number,
(d) Checking for prime,
(e) Factorial of number, and,
(f) Prime factors of the number.
'''


fl = float(input("Enter any number: "))                                     # accepting input from users
st = fl**(1/2)                                                              # computing square root
print("The square root of ",fl," is ",st,".")
sq = fl**2                                                                  # computing square
print(sq," is the square of ",fl,".")
ce = fl**3                                                                  # computing cube
print("The cube of ",fl," is ",ce,".")
for i in range(int(fl),0,-1):                                               # computing prime or not
    if i%2==0:
        print(fl," is not a prime.")
        break
    else:
        print(fl," is a prime.")
        break
flag = 1
fl1 = int(fl)
li = []
for i in range(fl1,0,-1):                                                   # computing factorial
    flag = flag * i
    li.append(flag)
print(li[len(li)-1]," is the factorial of ",fl)
o = int(fl)
lr = list()
for i in range(o,0,-1):                                                     # computing the prime factors of input
    if i%2==0:
        lr.append(i)
    else:
        continue
nl = []
for i in reversed(lr):
    nl.append(i)
print(nl," are the prime factors of ",fl)


'''
Enter any number: 5
The square root of  5.0  is  2.23606797749979 .
25.0  is the square of  5.0 .
The cube of  5.0  is  125.0 .
5.0  is a prime.
120  is the factorial of  5.0
[2, 4]  are the prime factors of  5.0
'''



