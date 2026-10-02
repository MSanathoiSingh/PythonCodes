================================================================================
MENU-DRIVEN CALCULATOR (Python)
================================================================================
Language : Python 3
Purpose  : A simple calculator that takes two numbers and one menu choice, and
           performs addition, subtraction, division, multiplication,
           exponentiation (x^y) or factorial (x!).


--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
The program asks for:
    1. the first number
    2. the second number
    3. an operation code from the menu

It then runs the chosen operation once and prints the result. It does not loop:
to do another calculation, run the program again.

Menu:
    1  Add
    2  Subtract
    3  Divide
    4  Multiply
    5  Exponential (x^y)
    6  Factorial (x!)

IMPORTANT BEHAVIOURS (they differ from a standard calculator):
    - Subtract (2) always gives LARGER minus SMALLER, so the result is never
      negative.
    - Divide (3) always divides the LARGER number by the SMALLER one.
    - Exponential (5) asks for one extra value and applies it to BOTH numbers.
    - Factorial (6) is computed for BOTH numbers.


--------------------------------------------------------------------------------
2. HOW TO RUN
--------------------------------------------------------------------------------
  1. Save the code as calculator.py
  2. Open a terminal in that folder
  3. Run:   python calculator.py
  4. Answer the three prompts (and a fourth if you choose Exponential)

Sample sessions:

    Enter the first number: 45
    Enter the second number: 36
    Enter the operation[...]: 1
    81.0  is the sum of two number.

    Enter the first number: 563
    Enter the second number: 458
    Enter the operation[...]: 2
    105.0  is the difference.

    Enter the first number: 563
    Enter the second number: 789
    Enter the operation[...]: 3
    1.4014209591474245  is the quotient of the two number.
    (789 / 563, because the larger number is the dividend)

    Enter the first number: 458
    Enter the second number: 312
    Enter the operation[...]: 4
    142896.0  is the product of two numbers.

    Enter the first number: 45
    Enter the second number: 36
    Enter the operation[...]: 5
    Enter the exponential value: 4
    4100625.0 is the exponential of 1st no.&  1679616.0  is exponential of 2nd no.

    Enter the first number: 23
    Enter the second number: 10
    Enter the operation[...]: 6
    25852016738884976640000  is the factorial of 1st number.
    3628800  is the factorial of 2nd number.

Results print with a decimal (81.0) because the inputs are read as floats.
Factorial results print as whole numbers because they are computed with ints.


--------------------------------------------------------------------------------
3. WORKING, STEP BY STEP
--------------------------------------------------------------------------------

STEP 1 - Read the inputs
    n  = float(input("Enter the first number: "))
    n1 = float(input("Enter the second number: "))
    s  = int(input("Enter the operation[...]: "))
    - n and n1 are floats, so decimals such as 2.5 are accepted.
    - s is an integer menu code, which selects the branch below.

STEP 2 - Choose the branch with if / elif / else
    The value of s is compared in order with 1, 2, 3, 4, 5 and 6.
    Exactly one branch runs; any other value falls through to the final else.

BRANCH s == 1 : Addition
    add = n + n1
    Prints the sum.

BRANCH s == 2 : Subtraction
    if n > n1:  sub  = n - n1
    else:       sub1 = n1 - n
    Prints the larger number minus the smaller number (absolute difference).

BRANCH s == 3 : Division
    if n > n1:  q  = n / n1
    else:       q1 = n1 / n
    Prints the larger number divided by the smaller number.

BRANCH s == 4 : Multiplication
    m = n * n1
    Prints the product.

BRANCH s == 5 : Exponential
    p  = int(input("Enter the exponential value: "))
    a  = n  ** p
    a1 = n1 ** p
    Asks for a whole-number exponent p, then prints n^p and n1^p.
    Example: 45^4 = 4100625.0 and 36^4 = 1679616.0.

BRANCH s == 6 : Factorial
    e = 1
    for i in range(1, int(n + 1)):
        e = e * i
    The same loop is repeated for n1 (result y).
    - range(1, int(n+1)) produces 1, 2, ..., n.
    - e multiplies up: 1 * 2 * 3 * ... * n = n!
    - A decimal input is truncated: 5.7 is treated as 5 (5! = 120).
    Trace for n = 5:  e = 1 -> 1 -> 2 -> 6 -> 24 -> 120

ELSE : invalid menu choice
    Prints an empty line. There is no error message.


--------------------------------------------------------------------------------
4. DATA FLOW
--------------------------------------------------------------------------------

   Keyboard                                  Variables
   --------                                  ---------
   first number   ---- float() ---------->   n
   second number  ---- float() ---------->   n1
   menu choice    ---- int() ------------>   s
                                              |
                          +-------+-------+---+---+-------+-------+------+
                          |       |       |       |       |       |      |
                         s==1    s==2    s==3    s==4    s==5    s==6   else
                          |       |       |       |       |       |      |
                       n + n1  larger -  larger /  n * n1  n**p,   n!, n1!  blank
                                smaller   smaller          n1**p              line
                          |       |       |       |       |       |      |
                          +-------+-------+-------+-------+-------+------+
                                              |
                                              v
                                    print(result, message)

For option 5 there is one extra input:
   exponent  ---- int() ---------->  p     (used for both n and n1)

Variables at a glance:

    n, n1   the two numbers entered (floats)
    s       menu choice (int)
    add, sub, sub1, q, q1, m, a, a1
            results of the arithmetic branches
    p       exponent for option 5
    e, y    factorial results for n and n1
    i       loop counter inside the factorial loops


--------------------------------------------------------------------------------
5. LIMITATIONS AND KNOWN ISSUES
--------------------------------------------------------------------------------
  - DIVISION BY ZERO crashes the program (ZeroDivisionError). Because the
    larger number is always the dividend, this happens when the smaller number
    is 0, e.g. 5 and 0, or 0 and 0.
  - SUBTRACTION AND DIVISION IGNORE ORDER. Entering 3 and 10 gives 10 - 3 = 7
    and 10 / 3, not 3 - 10 or 3 / 10. A proper calculator would use n - n1
    and n / n1.
  - FACTORIAL of a negative number returns 1 (the loop does not run), which is
    mathematically undefined. Decimal inputs are silently truncated.
  - FACTORIAL is always computed for both numbers, even if only one is wanted.
  - EXPONENT must be a whole number (int() rejects "2.5"). Zero raised to a
    negative power raises ZeroDivisionError.
  - NO INPUT VALIDATION: non-numeric input raises ValueError.
  - INVALID MENU CHOICE prints a blank line, with no message.
  - SINGLE USE: the program exits after one calculation.
  - Menu prompt text lists the order Add, Subtract, Divide, Multiply, which is
    not the usual order; the codes are 3 = Divide and 4 = Multiply.


--------------------------------------------------------------------------------
6. SUGGESTED IMPROVEMENTS
--------------------------------------------------------------------------------
  - Use n - n1 and n / n1 directly, and guard against zero:
        if n1 == 0:
            print("Cannot divide by zero.")
        else:
            print(n / n1)
  - Use math.factorial() and validate that the input is a non-negative integer.
  - Print "Invalid choice" in the final else branch.
  - Wrap the program in a while loop so the user can run several calculations.
  - Wrap conversions in try / except ValueError for non-numeric input.


--------------------------------------------------------------------------------
7. TEST CASES (behaviour of the code as written)
--------------------------------------------------------------------------------
    n     n1    Option   Output
    ----  ----  ------   ---------------------------------------
    45    36    1        81.0
    563   458   2        105.0
    458   563   2        105.0   (order does not matter)
    563   789   3        1.4014209591474245   (789 / 563)
    458   312   4        142896.0
    45    36    5, p=4   4100625.0 and 1679616.0
    23    10    6        25852016738884976640000 and 3628800
    5     0     3        ZeroDivisionError
    5     3     9        (blank line)


================================================================================
END OF README
================================================================================
