================================================================================
ARMSTRONG NUMBER CHECKER (Python)
================================================================================
Language : Python 3
Purpose  : Read an integer from the user and report whether it is an
           Armstrong number (three-digit definition: the sum of the cubes of
           its digits equals the number itself).


--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
Example: 370
    3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370   -> Armstrong number

Example: 562
    5^3 + 6^3 + 2^3 = 125 + 216 + 8 = 349  -> not an Armstrong number

The three-digit Armstrong numbers are 153, 370, 371 and 407.


--------------------------------------------------------------------------------
2. HOW TO RUN
--------------------------------------------------------------------------------
  1. Save the code as armstrong.py
  2. Open a terminal in that folder
  3. Run:   python armstrong.py
  4. Type an integer and press Enter

Sample sessions:

    Enter the number to be tested 370
    [3, 7, 0]
    370
    The number is an Armstrong's Number.

    Enter the number to be tested 562
    [5, 6, 2]
    349
    The number is not an Armstrong's Number.

The program prints three things: the list of digits, the sum of cubes, and the
final verdict.


--------------------------------------------------------------------------------
3. WORKING, STEP BY STEP (input: 370)
--------------------------------------------------------------------------------

STEP 1 - Read the input
    no = int(input("Enter the number to be tested "))
    - input() shows the prompt and returns the typed text as a string ("370").
    - int() converts it to the integer 370 and stores it in no.

STEP 2 - Split the number into digits
    li = [int(d) for d in str(no)]
    - str(no) turns 370 into the string "370", which can be walked through
      character by character.
    - The list comprehension takes each character ("3", "7", "0"), converts it
      back to an integer, and collects the results: li = [3, 7, 0].

STEP 3 - Show the digits
    print(li)        ->  [3, 7, 0]

STEP 4 - Sum the cubes
    s = 0
    for p in li:
        s += p**3
    - s starts at 0 and accumulates each digit cubed (p**3 = p raised to 3).

    Trace:
        p = 3 -> s = 0   + 27  = 27
        p = 7 -> s = 27  + 343 = 370
        p = 0 -> s = 370 + 0   = 370

STEP 5 - Show the sum
    print(s)         ->  370

STEP 6 - Compare and report
    if s == no:
        print("The number is an Armstrong's Number.")
    else:
        print("The number is not an Armstrong's Number.")
    - "==" tests equality ("=" would be assignment).
    - 370 == 370, so the first message is printed.


--------------------------------------------------------------------------------
4. DATA FLOW
--------------------------------------------------------------------------------

   Keyboard input "370"  (string)
          |
          v
   no = 370              (int)
          |
          v   str(no) -> "370" -> each character converted back to int
   li = [3, 7, 0]        (list of digits)
          |
          v   loop: cube each digit and add to running total
   s = 370               (sum of cubes)
          |
          v   compare s with no
   Output: "The number is an Armstrong's Number."

Variables at a glance:

    no   the number entered by the user (integer)
    li   list of its digits
    p    the current digit inside the loop
    s    running total of the cubes


--------------------------------------------------------------------------------
5. LIMITATIONS
--------------------------------------------------------------------------------
  - ONLY CORRECT FOR THREE-DIGIT NUMBERS. The code always cubes each digit.
    The general definition raises each digit to the power of the number of
    digits, e.g. 9474 = 9^4 + 4^4 + 7^4 + 4^4. A single-digit number such as 5
    is reported as "not Armstrong" (5^3 = 125), while under the general rule
    every single-digit number is Armstrong.
  - NO INPUT VALIDATION: text such as "abc" raises ValueError. A negative number
    such as -153 fails too, because the "-" sign cannot be converted by int().
  - Only whole numbers are supported (decimals raise ValueError).


--------------------------------------------------------------------------------
6. GENERALISED VERSION
--------------------------------------------------------------------------------
Works for any number of digits (153, 9474, 54748, ...):

    no = int(input("Enter the number to be tested "))
    digits = [int(d) for d in str(no)]
    n = len(digits)
    s = sum(p**n for p in digits)
    if s == no:
        print("The number is an Armstrong's Number.")
    else:
        print("The number is not an Armstrong's Number.")


--------------------------------------------------------------------------------
7. TEST CASES (three-digit rule, as in the original code)
--------------------------------------------------------------------------------
    Input   Sum of cubes   Result
    -----   ------------   ----------------
    153     153            Armstrong
    370     370            Armstrong
    371     371            Armstrong
    407     407            Armstrong
    562     349            Not Armstrong
    100     1              Not Armstrong
    999     2187           Not Armstrong


================================================================================
END OF README
================================================================================
