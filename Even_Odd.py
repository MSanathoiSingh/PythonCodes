'''
To accept list of N integers and partition list into two sub lists even and odd number.
'''


main = [ ]                                              #[ ] denotes a list of similar or dissimilar enitities.
even = [ ]
odd = [ ]
r = int(input("Enter the range of list "))              #int(input) is a method used to accept number form the user.
for i in range(r):                                      #used for using iteration.
 e = int(input('Enter the list element '))
 main.append(e)                                         #append function is used to enter elements in a list.
print('The list is ',main)
for l in range(0,len(main)):
 if main[l]%2==0:
  even.append(main[l])
 else:                                                  #execute a statement if a given condition is not met
  odd.append(main[l])
print('The even element of "main" list is ',even)       #print ued to display the number 
print('The odd element of "main" list is ',odd)


'''
Enter the range of list 9
Enter the list element 55
Enter the list element 23
Enter the list element 45
Enter the list element 89
Enter the list element 125
Enter the list element 598
Enter the list element 451
Enter the list element 789
Enter the list element 236
The list is  [55, 23, 45, 89, 125, 598, 451, 789, 236]
The even element of "main" list is  [598, 236]
The odd element of "main" list is  [55, 23, 45, 89, 125, 451, 789]
'''






  

  
   
