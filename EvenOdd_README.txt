================================================================================
EVEN / ODD LIST PARTITIONER (Python)
================================================================================
Language : Python 3
Purpose  : Accept N integers from the user, store them in a list, and split
           that list into two sub-lists: one with the even numbers and one
           with the odd numbers.


--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
The program works in three phases:

    1. INPUT      ask how many numbers there are (N), then read N integers
    2. PARTITION  go through the list once, sending each number to either the
                  "even" list or the "odd" list
    3. OUTPUT     print the original list, the even list and the odd list

A number is even if it leaves remainder 0 when divided by 2 (n % 2 == 0).
Otherwise it is odd. The original order of the numbers is preserved inside
each sub-list.


--------------------------------------------------------------------------------
2. HOW TO RUN
--------------------------------------------------------------------------------
  1. Save the code as partition.py
  2. Open a terminal in that folder
  3. Run:   python partition.py
  4. Enter N (how many numbers), then enter the numbers one at a time,
     pressing Enter after each

Sample session (N = 9):

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

The program runs once and exits.


--------------------------------------------------------------------------------
3. WORKING, STEP BY STEP
--------------------------------------------------------------------------------

STEP 1 - Create three empty lists
    main = []     # every number entered by the user
    even = []     # will hold the even numbers
    odd  = []     # will hold the odd numbers

STEP 2 - Read how many numbers to enter
    r = int(input("Enter the range of list "))
    - input() returns text; int() converts it to an integer.
    - r is N, the number of elements (9 in the sample run).

STEP 3 - Read the elements
    for i in range(r):
        e = int(input('Enter the list element '))
        main.append(e)
    - range(r) makes the loop run exactly r times (i = 0 ... r-1).
    - Each pass reads one integer into e and appends it to the end of main.
    - After the loop, main = [55, 23, 45, 89, 125, 598, 451, 789, 236].

STEP 4 - Display the full list
    print('The list is ', main)

STEP 5 - Partition into even and odd
    for l in range(0, len(main)):
        if main[l] % 2 == 0:
            even.append(main[l])
        else:
            odd.append(main[l])
    - l is the index, running from 0 to len(main) - 1.
    - main[l] is the element at that position.
    - % is the modulo (remainder) operator. A remainder of 0 means even.
    - Even numbers go to the even list; everything else goes to the odd list.

    Trace (first four elements and the evens):
        l=0  55   55 % 2 = 1   -> odd   = [55]
        l=1  23   23 % 2 = 1   -> odd   = [55, 23]
        l=2  45   45 % 2 = 1   -> odd   = [55, 23, 45]
        l=3  89   89 % 2 = 1   -> odd   = [55, 23, 45, 89]
        ...
        l=5  598  598 % 2 = 0  -> even  = [598]
        ...
        l=8  236  236 % 2 = 0  -> even  = [598, 236]

STEP 6 - Display the results
    print('The even element of "main" list is ', even)
    print('The odd element of "main" list is ', odd)


--------------------------------------------------------------------------------
4. DATA FLOW
--------------------------------------------------------------------------------

   Keyboard "9"  ---- int() ---->  r = 9  (how many elements)
                                      |
                                      v
   Keyboard "55", "23", ... ---- int() ---->  e  --- append --->  main
                                      (repeated r times)       [55, 23, 45, ...]
                                                                   |
                                                                   v
                                         for each element: element % 2 == 0 ?
                                                  |                     |
                                                 YES                    NO
                                                  |                     |
                                                  v                     v
                                          even.append(...)       odd.append(...)
                                                  |                     |
                                                  v                     v
                                             [598, 236]    [55, 23, 45, 89, 125, 451, 789]
                                                  \                    /
                                                   v                  v
                                                     print(even), print(odd)

Variables at a glance:

    main   list of all numbers entered
    even   list of the even numbers
    odd    list of the odd numbers
    r      number of elements to read (N)
    i      loop counter for input (not otherwise used)
    e      the number just typed in
    l      index used while partitioning

Note: the original list main is NOT modified by the partitioning. Elements are
copied into even or odd, so main still holds all values at the end.


--------------------------------------------------------------------------------
5. LIMITATIONS
--------------------------------------------------------------------------------
  - NO INPUT VALIDATION: entering text or a decimal (e.g. "abc", "4.5")
    raises ValueError and the program stops.
  - A NEGATIVE OR ZERO N is accepted: range(r) is then empty, so the program
    prints three empty lists without any warning.
  - Negative numbers work correctly. In Python, -4 % 2 is 0 and -3 % 2 is 1.
  - Zero counts as even (0 % 2 == 0).
  - Each element is typed on a separate line, so very large lists are tedious
    to enter.
  - Single use: the program exits after one run.
  - The variable name "l" (lowercase L) is easy to confuse with the digit 1;
    "i" or "index" would be clearer.


--------------------------------------------------------------------------------
6. SHORTER ALTERNATIVE
--------------------------------------------------------------------------------
Using list comprehensions and reading all numbers on one line:

    main = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    even = [x for x in main if x % 2 == 0]
    odd  = [x for x in main if x % 2 != 0]
    print("The list is", main)
    print("Even:", even)
    print("Odd:", odd)

Looping directly over the elements, instead of by index, is also more idiomatic:

    for x in main:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)


--------------------------------------------------------------------------------
7. TEST CASES
--------------------------------------------------------------------------------
    Input (N, elements)         even            odd
    --------------------------  --------------  ---------------
    4: 1 2 3 4                  [2, 4]          [1, 3]
    3: 2 4 6                    [2, 4, 6]       []
    3: 1 3 5                    []              [1, 3, 5]
    1: 0                        [0]             []
    4: -2 -3 0 7                [-2, 0]         [-3, 7]
    0 (no elements)             []              []
    9: sample from above        [598, 236]      [55, 23, 45, 89, 125, 451, 789]


================================================================================
END OF README
================================================================================
