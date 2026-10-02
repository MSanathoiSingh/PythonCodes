================================================================================
FIBONACCI SERIES GENERATOR (Python)
================================================================================
Language : Python 3
Purpose  : Accept the number of terms from the user and generate the Fibonacci 
           series.


--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
Formulas implemented:

    Next term      c = a + b
    State update   a = b, b = c

where a and b are initialized to 0 and 1 respectively, and c represents the 
next term added to the series.

Example (from the sample run): n = 10
    Generates 10 numbers in sequence starting from c = 0 + 1 = 1:
    [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

NOTE ON THE IMPLEMENTATION: The code starts generating sequence numbers 
starting with c = a + b = 1[cite: 1]. Standard Fibonacci definitions often start 
with 0 or [0, 1]. In this code's current implementation, it appends the sum 
c directly to the list[cite: 1], producing the sequence beginning with 1, 2, 3, 5...


--------------------------------------------------------------------------------
2. HOW TO RUN
--------------------------------------------------------------------------------
  1. Save the code as fibonacci.py
  2. Open a terminal in that folder
  3. Run:   python fibonacci.py
  4. Enter the range (number of terms), then press Enter

Sample session:

    Enter the range: 10
    [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  is the required fibonacci series

The program runs once and exits. Run it again for another range.


--------------------------------------------------------------------------------
3. WORKING, STEP BY STEP (input: n = 10)
--------------------------------------------------------------------------------

STEP 1 - Read the range
    n = int(input("Enter the range: "))
    - input() returns the typed text as a string ("10").
    - int() converts it to the integer 10 and stores it in n.

STEP 2 - Initialize variables
    a = 0
    b = 1
    li = []
    - Sets initial values for state tracking and initializes an empty list `li`.

STEP 3 - Loop and compute sequence
    for i in range(n):
        c = a + b
        li.append(c)
        a = b
        b = c
    - In iteration 1 (i=0): c = 0 + 1 = 1; li = [1]; a becomes 1, b becomes 1.
    - In iteration 2 (i=1): c = 1 + 1 = 2; li = [1, 2]; a becomes 1, b becomes 2.
    - Repeats for n times (10 iterations) to accumulate 10 terms in `li`.

STEP 4 - Display the results
    print(li, ' is the required fibonacci series')
    - Prints the populated list alongside the descriptor message.


--------------------------------------------------------------------------------
4. DATA FLOW
--------------------------------------------------------------------------------

   Keyboard "10" ---- int() ----> n = 10
                                    |
                                    v
                             Loop n times:
                                c = a + b  -----> li.append(c)
                                a = b, b = c
                                    |
                                    v
                     print(li) -> "[1, 2, 3, 5, ...] is the required fibonacci series"

Variables at a glance:

    n   number of terms to generate (int)
    a   first operand / previous term state (int)
    b   second operand / current term state (int)
    c   sum of a and b / newly generated term (int)
    li  list holding the calculated Fibonacci terms (list of ints)


--------------------------------------------------------------------------------
5. LIMITATIONS
--------------------------------------------------------------------------------
  - WHOLE NUMBERS ONLY: int() rejects non-integer inputs (like decimals or text) 
    and raises ValueError.
  - NO INPUT VALIDATION: Entering 0 or a negative number yields an empty list 
    `[]` without a descriptive warning message.
  - NON-STANDARD STARTING VALUES: Skipping 0 in the output list might not match 
    standard mathematical representations where 0 is included as F(0).
  - Single use: the program exits after one run.


--------------------------------------------------------------------------------
6. SUGGESTED IMPROVEMENTS
--------------------------------------------------------------------------------
  - Add input validation and support zero/negative entries gracefully:

        try:
            n = int(input("Enter the range: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                a, b = 0, 1
                li = []
                for _ in range(n):
                    a, b = b, a + b
                    li.append(a)
                print(li, 'is the required fibonacci series')
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


--------------------------------------------------------------------------------
7. TEST CASES (behaviour of the code as written)
--------------------------------------------------------------------------------
    n     Output Series
    ----  ------------------------------------
    1     [1]
    5     [1, 2, 3, 5, 8]
    10    [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    0     []
    -3    []
    3.5   ValueError (int() rejects decimals)


================================================================================
END OF README
================================================================================