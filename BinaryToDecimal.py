'''
To input binary number from user and convert it into decimal number.
'''

n = int(input("Enter the binary number: "))                         # take binary number from user
s = str(n)                                                          # converting to string for traversal of digits
r =[]
for i in range(len(s)):
    d = n%10                                                        # seperating last digit from the input number
    d1 = n//10
    r += str(d)                                                     # reversing the binary input
    n=d1
print(r)                                                            # printing the reverse of binary input
t =[]
for g in range(len(r)):                                             # traversing the reverse input
    q = int(r[g])*2**g                                              # converting to decimal equivalent
    t.append(q)
print(t)                                                        
w =0
for p in range(len(t)):
    w = w + int(t[p])                                               # final decimal equivalent of input
print(w)


'''
Enter the binary number: 100011
['1', '1', '0', '0', '0', '1']
[1, 2, 0, 0, 0, 32]
35
'''
