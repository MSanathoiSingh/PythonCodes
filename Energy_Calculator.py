'''
To accept an object mass in kilograms and velocity in metres per second and display its momentum.
Momentum is calculated as e = mc^2 where m is mass of the object and c is its velocity.
'''


s = "Today we will be calculating energy and momentum of a body as instructed by you."
print(s)                                                                    #print fn is ued to display the number on the screen.
m = int(input('Please enter the mass of the body in "kg" '))                #int(input) is an function used to accept number form the user.
v = int(input('Please enter the velocity of the body in "m/s" '))
p = m * v
e = m*v**2/2
print('The momentum of the body is ',p,' kg m/s')
print('The energy of the body is ',e,' J')


'''
Today we will be calculating energy and momentum of a body as instructed by you.
Please enter the mass of the body in "kg" 52
Please enter the velocity of the body in "m/s" 23
The momentum of the body is  1196  kg m/s
The energy of the body is  13754.0  J
'''



