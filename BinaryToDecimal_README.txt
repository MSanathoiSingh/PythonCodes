================================================================================
BINARY TO DECIMAL CONVERTER (Python)
================================================================================
Language : Python 3
Purpose  : Read a binary number from the user and convert it to its decimal
           (base-10) equivalent, showing the intermediate steps.


--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
A binary number is written in base 2, where each digit (bit) is worth a power
of 2 depending on its position, counting from the RIGHT starting at 0:

    position :   5    4    3    2    1    0
    weight   :  32   16    8    4    2    1
    bit      :   1    0    0    0    1    1     (binary 100011)

    decimal  = 1*32 + 0*16 + 0*8 + 0*4 + 1*2 + 1*1 = 35

The program automates this: it splits the number into digits, reverses them so
the rightmost bit comes first, multiplies each bit by 2^position, and adds up
the results.


--------------------------------------------------------------------------------
2. HOW TO RUN
--------------------------------------------------------------------------------
  1. Save the code as binary_to_decimal.py
  2. Open a terminal in that folder
  3. Run:   python binary_to_decimal.py
  4. Type a binary number (digits 0 and 1 only) and press Enter

Sample session:

    Enter the binary number: 100011
    ['1', '1', '0', '0', '0', '1']
    [1, 2, 0, 0, 0, 32]
    35


--------------------------------------------------------------------------------
3. WORKING, STEP BY STEP (input: 100011)
--------------------------------------------------------------------------------

STEP 1 - Read the input
    n = int(input("Enter the binary number: "))
    - input() returns a string; int() converts it to the integer 100011.
    - NOTE: Python reads this as the decimal number one hundred thousand and
      eleven. It is only treated as binary by the logic that follows.

STEP 2 - Count the digits
    s = str(n)
    - Converts the number back to a string, "100011".
    - It is used only for len(s), which gives the digit count (6), so the next
      loop knows how many times to run.

STEP 3 - Extract digits in reverse order
    r = []
    for i in range(len(s)):
        d  = n % 10        # last digit of n
        d1 = n // 10       # n with the last digit removed
        r += str(d)        # append the digit (as a character) to the list
        n  = d1

    - n % 10 gives the last digit; n // 10 chops it off.
    - Repeating this peels digits from right to left, so r holds the bits
      in reverse (least significant bit first).
    - r += str(d) works because "+=" on a list with a one-character string
      appends that character (list.extend behavior).

    Trace:
        n = 100011 -> d = 1, n = 10001, r = ['1']
        n = 10001  -> d = 1, n = 1000,  r = ['1','1']
        n = 1000   -> d = 0, n = 100,   r = ['1','1','0']
        n = 100    -> d = 0, n = 10,    r = ['1','1','0','0']
        n = 10     -> d = 0, n = 1,     r = ['1','1','0','0','0']
        n = 1      -> d = 1, n = 0,     r = ['1','1','0','0','0','1']

    print(r) shows:  ['1', '1', '0', '0', '0', '1']

STEP 4 - Multiply each bit by its power of 2
    t = []
    for g in range(len(r)):
        q = int(r[g]) * 2**g
        t.append(q)

    - g is both the index in r and the bit position (0 = rightmost bit).
    - 2**g is 2 raised to the power g.

    Trace:
        g=0: 1 * 2^0 = 1
        g=1: 1 * 2^1 = 2
        g=2: 0 * 2^2 = 0
        g=3: 0 * 2^3 = 0
        g=4: 0 * 2^4 = 0
        g=5: 1 * 2^5 = 32

    print(t) shows:  [1, 2, 0, 0, 0, 32]

STEP 5 - Add everything up
    w = 0
    for p in range(len(t)):
        w = w + int(t[p])

    - w is a running total: 0 -> 1 -> 3 -> 3 -> 3 -> 3 -> 35
    - print(w) shows the final decimal value:  35


--------------------------------------------------------------------------------
4. DATA FLOW
--------------------------------------------------------------------------------

   User types "100011"
          |
          v
   n = 100011  (int)  ---------------->  s = "100011"  (only used for length)
          |
          v
   Digit extraction loop (n % 10, n // 10)
          |
          v
   r = ['1','1','0','0','0','1']        (bits, least significant first)
          |
          v
   Weighting loop (bit * 2**position)
          |
          v
   t = [1, 2, 0, 0, 0, 32]              (value contributed by each bit)
          |
          v
   Summation loop
          |
          v
   w = 35                               (decimal result, printed)

Variables at a glance:

    n   integer being consumed digit by digit (ends at 0)
    s   string form of the input, used for its length
    r   list of digit characters, reversed
    t   list of integer contributions (bit * power of 2)
    w   final decimal result
    d   current last digit        d1  remaining digits
    i, g, p   loop counters


--------------------------------------------------------------------------------
5. LIMITATIONS
--------------------------------------------------------------------------------
  - NO VALIDATION: input such as 102 or 2 is accepted and gives a meaningless
    answer (the code never checks that every digit is 0 or 1). Non-numeric
    input crashes with ValueError.
  - LEADING ZEROS ARE LOST: int("00101") becomes 101, so the length shrinks.
    The result is still correct, because leading zeros add nothing.
  - NEGATIVE NUMBERS: "-101" is not handled; the sign breaks the digit loop.
  - Fractions (e.g. 10.11) are not supported; whole binary numbers only.


--------------------------------------------------------------------------------
6. SIMPLER ALTERNATIVES
--------------------------------------------------------------------------------
Built-in conversion (Python reads the string directly as base 2):

    b = input("Enter the binary number: ")
    print(int(b, 2))              # int("100011", 2) -> 35

Manual version with validation, no reversing needed:

    b = input("Enter the binary number: ")
    if b and set(b) <= {"0", "1"}:
        w = 0
        for bit in b:
            w = w * 2 + int(bit)      # shift left, then add the new bit
        print(w)
    else:
        print("Not a valid binary number.")

The "w = w * 2 + bit" method (Horner's method) reads left to right, so it needs
no reversal and no powers of 2.


--------------------------------------------------------------------------------
7. TEST CASES
--------------------------------------------------------------------------------
    Input      Expected output
    -------    ---------------
    0          0
    1          1
    101        5
    1111       15
    100011     35
    11111111   255
    10000000   128


================================================================================
END OF README
================================================================================
