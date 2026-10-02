================================================================================
SMALLEST AND GREATEST COMMON DIVISOR CALCULATOR (Python)
================================================================================
Language : Python 3
Purpose  : Accept two integers from the user and compute their smallest common 
           divisor (greater than 1) and greatest common divisor (GCD).


--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
Logic implemented:

    Smallest Common Divisor : Iterates n from 2 up to min(x, y). Checks if both 
                              x % n == 0 and y % n == 0.
    Greatest Common Divisor  : Iterates m from min(x, y) down to 2. Checks if 
                              both x % m == 0 and y % m == 0.

where x and y are two user-provided integers.

Example (from sample run 1): x = 864, y = 128
    min(864, 128) = 128
    Smallest common divisor loop: checks n = 2 -> 864 % 2 == 0 and 128 % 2 == 0
      -> Smallest common divisor = 2
    Greatest common divisor loop: checks m = 128, 127, ... down to 32
      -> 864 % 32 == 0 and 128 % 32 == 0
      -> Greatest common divisor = 32

NOTE ON LOGIC & OUTPUT ISSUES:
1. Spurious "Else" Output inside Loop: The code prints "No common lowest/greatest 
   multiple found..." inside the `else:` block on the VERY FIRST iteration if 
   the first checked value fails. For example, if min(x,y) isn't a common divisor, 
   it prints "No common greatest multiple..." immediately on `m = min(x,y)` and 
   then keeps searching in subsequent iterations.
2. Terminology: The messages refer to "lowest/greatest multiple", but the code 
   actually computes common divisors (factors), not multiples.
3. Coprime Numbers: For coprime inputs (like 458 and 253), the loops complete 
   without finding any common factor > 1, resulting in printed error lines on 
   every non-matching iteration (or first iteration) rather than a single summary.


--------------------------------------------------------------------------------
2. HOW TO RUN
--------------------------------------------------------------------------------
  1. Save the code as common_divisors.py
  2. Open a terminal in that folder
  3. Run:   python common_divisors.py
  4. Enter the first number, press Enter, then enter the second number

Sample session 1:

    Enter the first number 864
    Enter the second number 128
    The common lowest divisor for 'x' and 'y' is  2
    The greatest common multiple for 'x' and 'y' is  32

Sample session 2:

    Enter the first number 458
    Enter the second number 253
    No common lowest multiple found for the combination.
    No common greatest multiple found for the given combination.

The program runs once and exits. Run it again for another pair of numbers.


--------------------------------------------------------------------------------
3. WORKING, STEP BY STEP (input: x = 864, y = 128)
--------------------------------------------------------------------------------

STEP 1 - Read the inputs
    x = int(input("Enter the first number "))
    y = int(input("Enter the second number "))
    - Accepts typed strings ("864", "128") and converts them to integers.

STEP 2 - Find Smallest Common Divisor
    for n in range(2, min(x, y) + 1):
        if x % n == 0 and y % n == 0:
            print("The common lowest divisor for 'x' and 'y' is ", n)
            break
        else:
            print('No common lowest multiple found for the combination.')
    - Loop checks n = 2: 864 % 2 == 0 and 128 % 2 == 0 is True.
    - Prints divisor message with n = 2, then executes `break` to exit loop.

STEP 3 - Find Greatest Common Divisor
    for m in range(min(x, y), 1, -1):
        if x % m == 0 and y % m == 0:
            print("The greatest common multiple for 'x' and 'y' is ", m)
            break
        else:
            print("No common greatest multiple found for the given combination.")
    - Loop starts at m = 128: 864 % 128 != 0 -> prints "No common..." message.
    - Decrements m down until m = 32: 864 % 32 == 0 and 128 % 32 == 0 is True.
    - Prints greatest common factor message with m = 32, then executes `break`.


--------------------------------------------------------------------------------
4. DATA FLOW
--------------------------------------------------------------------------------

   Keyboard "864" ---- int() ----> x = 864 --+
                                            |--> min(x, y) = 128
   Keyboard "128" ---- int() ----> y = 128 --+
                                            |
            +-------------------------------+-------------------------------+
            |                                                               |
            v                                                               v
   Smallest Divisor Loop                                          Greatest Divisor Loop
   (n = 2 to 128)                                                 (m = 128 down to 2)
            |                                                               |
    x%n==0 and y%n==0?                                             x%m==0 and y%m==0?
            |                                                               |
     [True at n=2]                                                   [True at m=32]
            |                                                               |
            v                                                               v
   print("... lowest divisor... 2")                               print("... greatest multiple... 32")


Variables at a glance:

    x   first input number (int)
    y   second input number (int)
    n   loop variable for smallest common divisor search (int)
    m   loop variable for greatest common divisor search (int)


--------------------------------------------------------------------------------
5. LIMITATIONS
--------------------------------------------------------------------------------
  - LOGICAL BUG IN ELSE-BLOCK: The `else:` statement is executed inside the 
    loop on any non-matching iteration, causing premature/repeated "not found" 
    messages. Using Python's `for...else` construct outside the loop body would 
    fix this.
  - INEFFICIENT GCD COMPUTATION: Linear search from min(x,y) down to 2 takes 
    O(N) time. Standard Euclidean algorithm (`math.gcd`) runs in O(log(N)).
  - WHOLE NUMBERS ONLY: Non-integer entries crash with ValueError.
  - NEGATIVE NUMBERS / ZERO:
    - Zero inputs cause division by zero or invalid range errors.
    - Negative inputs lead to empty loop ranges or infinite loops depending on signs.
  - Single use: program terminates after one execution.


--------------------------------------------------------------------------------
6. SUGGESTED IMPROVEMENTS
--------------------------------------------------------------------------------
  - Correct the loop structure, use mathematical conventions, and add validation:

        import math

        try:
            x = int(input("Enter the first positive integer: "))
            y = int(input("Enter the second positive integer: "))

            if x <= 0 or y <= 0:
                print("Please enter positive integers greater than 0.")
            else:
                # Smallest Common Divisor (> 1)
                for n in range(2, min(x, y) + 1):
                    if x % n == 0 and y % n == 0:
                        print(f"The lowest common divisor for {x} and {y} is {n}")
                        break
                else:
                    print("No common divisor > 1 found for the given combination.")

                # Greatest Common Divisor (GCD)
                gcd_val = math.gcd(x, y)
                if gcd_val > 1:
                    print(f"The greatest common divisor for {x} and {y} is {gcd_val}")
                else:
                    print("No greatest common divisor > 1 found (numbers are coprime).")

        except ValueError:
            print("Invalid input! Please enter valid integers.")


--------------------------------------------------------------------------------
7. TEST CASES (behaviour of the code as written)
--------------------------------------------------------------------------------
    x      y      Lowest Divisor Output        Greatest Divisor Output
    -----  -----  ---------------------------  ---------------------------------------
    864    128    2                            32 (with 1 false "Not found" line before)
    458    253    No common lowest... (at n=2) No common greatest... (at m=253)
    10     5      5                            5
    7      13     No common lowest... (at n=2) No common greatest... (range empty)
    abc    10     ValueError (int() rejects non-numeric input)


================================================================================
END OF README
================================================================================