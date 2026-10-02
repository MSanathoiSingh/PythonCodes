================================================================================
NUMBER OPERATIONS AND MATHEMATICAL COMPUTATIONS (Python)
================================================================================
Language : Python 3
Purpose  : Accept a number from the user and calculate its square root, square,
           cube, prime check, factorial, and prime factors.


--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
Formulas and operations implemented:

    (a) Square root     st = fl ** (1/2)     (unit: pure number)
    (b) Square          sq = fl ** 2
    (c) Cube            ce = fl ** 3
    (d) Prime Check     Checks divisibility by 2 in loop
    (e) Factorial       Product of all integers from fl1 down to 1
    (f) Prime Factors   Gathers even numbers down to 0 and reverses list

Example (from the sample run): fl = 5.0
    st = 5.0 ** 0.5           = 2.23606797749979
    sq = 5.0 ** 2             = 25.0
    ce = 5.0 ** 3             = 125.0
    Prime check               = 5.0 is a prime
    Factorial                 = 5! = 120
    Prime factors (as coded)  = [2, 4]

NOTE ON THE LOGIC & IMPLEMENTATION BUGS:
1. Prime Checking: The code only checks if the integer conversion of `fl` is 
   even or odd on its first loop iteration (`i%2 == 0`). It breaks immediately, 
   incorrectly categorizing any odd number (like 9 or 15) as prime and 2 as not prime.
2. Prime Factors: The code appends all even numbers from `int(fl)` down to 1 and 
   prints them as "prime factors". For `5.0`, it outputs `[2, 4]`, where 4 is 
   not prime and neither 2 nor 4 are factors of 5.
3. Factorial on Floats: Inputs with decimal parts (e.g., 5.5) are truncated 
   to integer (`int(fl)`) before computing factorial and prime factors.


--------------------------------------------------------------------------------
2. HOW TO RUN
--------------------------------------------------------------------------------
  1. Save the code as number_ops.py
  2. Open a terminal in that folder
  3. Run:   python number_ops.py
  4. Enter a number, then press Enter

Sample session:

    Enter any number: 5
    The square root of  5.0  is  2.23606797749979 .
    25.0  is the square of  5.0 .
    The cube of  5.0  is  125.0 .
    5.0  is a prime.
    120  is the factorial of  5.0
    [2, 4]  are the prime factors of  5.0

The program runs once and exits. Run it again for another number.


--------------------------------------------------------------------------------
3. WORKING, STEP BY STEP (input: fl = 5.0)
--------------------------------------------------------------------------------

STEP 1 - Read the input number
    fl = float(input("Enter any number: "))
    - Accepts typed input ("5") and converts it to float `5.0`.

STEP 2 - Compute Square Root, Square, and Cube
    st = fl**(1/2)   -> 5.0**0.5 = 2.23606797749979
    sq = fl**2       -> 5.0**2 = 25.0
    ce = fl**3       -> 5.0**3 = 125.0
    - Prints each computed power value.

STEP 3 - Prime Check (Logic Bug Present)
    for i in range(int(fl), 0, -1):
        if i % 2 == 0: ... break
        else: ... break
    - Checks only `i = 5`. Since `5 % 2 != 0`, prints "5.0 is a prime" and breaks.

STEP 4 - Compute Factorial
    flag = 1
    fl1 = int(fl)
    li = []
    for i in range(fl1, 0, -1):
        flag = flag * i
        li.append(flag)
    - Iterates `i` from 5 down to 1:
      i=5: flag=5,   li=[5]
      i=4: flag=20,  li=[5, 20]
      i=3: flag=60,  li=[5, 20, 60]
      i=2: flag=120, li=[5, 20, 60, 120]
      i=1: flag=120, li=[5, 20, 60, 120, 120]
    - Accesses `li[len(li)-1]` (last element = 120) and prints as factorial.

STEP 5 - Prime Factors Computation (Logic Bug Present)
    o = int(fl)
    lr = []
    for i in range(o, 0, -1):
        if i % 2 == 0: lr.append(i)
    - Collects all even numbers <= 5: `lr = [4, 2]`.
    - Reverses `lr` into `nl`: `nl = [2, 4]`.
    - Prints `[2, 4]` as the prime factors.


--------------------------------------------------------------------------------
4. DATA FLOW
--------------------------------------------------------------------------------

   Keyboard "5" ---- float() ----> fl = 5.0
                                    |
            +-----------------------+-----------------------+
            |                       |                       |
            v                       v                       v
      st = fl**(1/2)             sq = fl**2              ce = fl**3
   (2.23606797749979)             (25.0)                  (125.0)
            |                       |                       |
            +-----------------------+-----------------------+
                                    |
                                    v
                               fl1 = int(fl)  -->  5
                                    |
                 +------------------+------------------+
                 |                                     |
                 v                                     v
         Factorial Loop                        Even Numbers Loop
      (flag = flag * i)                       (if i % 2 == 0)
                 |                                     |
                 v                                     v
      li = [5, 20, 60, 120, 120]              lr = [4, 2] -> reversed -> nl = [2, 4]
                 |                                     |
                 v                                     v
            print(120)                             print([2, 4])


Variables at a glance:

    fl     input value cast to float (float)
    st     square root of input (float)
    sq     square of input (float)
    ce     cube of input (float)
    flag   accumulated factorial result (int)
    fl1    integer cast of fl used for factorial loop (int)
    li     list of intermediate factorial products (list of ints)
    o      integer cast of fl used for prime factor loop (int)
    lr     list of even numbers in descending order (list of ints)
    nl     reversed list of even numbers (list of ints)


--------------------------------------------------------------------------------
5. LIMITATIONS
--------------------------------------------------------------------------------
  - INCORRECT PRIME LOGIC: Odd composite numbers (e.g., 9, 15, 21) are wrongly 
    reported as prime because only divisibility by 2 is checked.
  - INCORRECT PRIME FACTOR LOGIC: Generates all even numbers up to N instead 
    of actual prime factors.
  - NO INPUT VALIDATION: Entering non-numeric text crashes with ValueError.
  - NEGATIVE NUMBERS & ZERO:
    - Negative numbers produce complex numbers or crashes during integer range operations.
    - Zero/negative factorial logic yields empty lists or incorrect initial values.
  - MEMORY INEFFICIENT: Storing intermediate factorial steps in list `li` is 
    unnecessary when only the final product is needed.


--------------------------------------------------------------------------------
6. SUGGESTED IMPROVEMENTS
--------------------------------------------------------------------------------
  - Correct the prime check, factorial, and prime factorization algorithm:

        import math

        try:
            val = float(input("Enter a positive integer: "))
            if val < 0 or not val.is_integer():
                print("Please enter a non-negative whole number.")
            else:
                n = int(val)
                print(f"Square root: {math.sqrt(n)}")
                print(f"Square: {n**2}")
                print(f"Cube: {n**3}")

                # Prime check
                is_prime = n > 1 and all(n % i != 0 for i in range(2, int(math.isqrt(n)) + 1))
                print(f"{n} is {'a prime' if is_prime else 'not a prime'}.")

                # Factorial
                print(f"Factorial: {math.factorial(n)}")

                # Actual Prime Factors
                temp = n
                factors = []
                d = 2
                while d * d <= temp:
                    while temp % d == 0:
                        factors.append(d)
                        temp //= d
                    d += 1
                if temp > 1:
                    factors.append(temp)
                print(f"Prime factors: {factors}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")


--------------------------------------------------------------------------------
7. TEST CASES (behaviour of the code as written)
--------------------------------------------------------------------------------
    Input  Sqrt    Square  Cube    Prime Output   Factorial  Prime Factors Output
    -----  ------  ------  ------  -------------  ---------  --------------------
    5      2.2361  25.0    125.0   5.0 is prime   120        [2, 4]
    4      2.0     16.0    64.0    4.0 not prime  24         [2, 4]
    9      3.0     81.0    729.0   9.0 is prime   362880     [2, 4, 6, 8]
    2      1.4142  4.0     8.0     2.0 not prime  2          [2]
    abc    ValueError (invalid literal for float())


================================================================================
END OF README
================================================================================