================================================================================
STRING OPERATIONS PROGRAM (Python)
================================================================================
Language : Python 3
Purpose  : Accept a string from the user and perform operations including length
           calculation, string reversal, equality check, palindrome check, and
           substring verification.


--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
Operations implemented:

    (i)   Length Calculation   len(list(s))
    (ii)  String Reversal      "".join(reversed(list(s)))
    (iii) Equality Check       s == s2
    (iv)  Palindrome Check     Reverses s3 and compares against s's reverse (sp)
    (v)   Substring Check      s3 in s

where s is the primary input string, s2 is the comparison string, and s3 is 
used for palindrome checking and subsequently overwritten for substring checking.

Example (from the sample run):
    Primary String s = "Sourabh"
      - Length           = 7
      - Reversed (sp)    = "hbaruoS"
    Comparison s2 = "Tanmay"
      - Equality         = "Sourabh" == "Tanmay" -> False (Strings are not equal)
    Palindrome Input s3 = "Sourabh"
      - Reversed (sq)    = "hbaruoS"
      - Comparison       = sq == sp ("hbaruoS" == "hbaruoS") -> True (Is a palindrome)
    Substring Input s3 = "hb"
      - Check            = "hb" in "Sourabh" -> False (Not a substring)

NOTE ON LOGIC & IMPLEMENTATION BUGS:
1. Palindrome Logic Bug: The code checks if the reversed version of `s3` (`sq`) 
   matches the reversed version of `s` (`sp`) from step (ii). It does NOT check 
   if `s3` is equal to its OWN reverse. In the sample run, entering "Sourabh" 
   for `s3` outputs "The string is a palindrome." because `sq` ("hbaruoS") matches 
   `sp` ("hbaruoS"), even though "Sourabh" is not a palindrome.
2. Variable Overwriting: `s3` is used as the variable name for both the 
   palindrome prompt and the substring prompt, overwriting the previous value.
3. Unused Variable: `l3 = list(s3)` is initialized in the substring section 
   but never used.


--------------------------------------------------------------------------------
2. HOW TO RUN
--------------------------------------------------------------------------------
  1. Save the code as string_ops.py
  2. Open a terminal in that folder
  3. Run:   python string_ops.py
  4. Follow the interactive prompts to enter strings for each test

Sample session:

    Enter the string: Sourabh
    7  is the length of the string entered.
    hbaruoS  is the reverse of the string entered.
    Enter the other string: Tanmay
    The strings are not equal.
    Enter the string to be checked for palindrome: Sourabh
    The string is a palindrome.
    Enter substring: hb
    Entered string is not a substring.

The program runs once sequentially and exits.


--------------------------------------------------------------------------------
3. WORKING, STEP BY STEP (input: s = "Sourabh")
--------------------------------------------------------------------------------

STEP 1 - Read main string and compute length
    s = input("Enter the string: ")
    li = list(s)
    print(len(li), " is the length of the string entered.")
    - Converts "Sourabh" to list ['S', 'o', 'u', 'r', 'a', 'b', 'h'].
    - `len(li)` returns 7 and prints the length.

STEP 2 - Reverse the main string
    l = []
    for i in reversed(li):
        l.append(i)
    a = ""
    sp = a.join(l)
    print(sp, " is the reverse of the string entered.")
    - Reverses character list to ['h', 'b', 'a', 'r', 'u', 'o', 'S'].
    - Joins into string `sp` = "hbaruoS" and prints it.

STEP 3 - Equality check
    s2 = input("Enter the other string: ")
    if s == s2: ... else: ...
    - Accepts `s2` ("Tanmay").
    - Compares "Sourabh" == "Tanmay" -> False, prints "The strings are not equal."

STEP 4 - Palindrome check (Contains Logic Bug)
    s3 = input("Enter the string to be checked for palindrome: ")
    l1 = list(s3)
    l2 = []
    for q in reversed(l1):
        l2.append(q)
    sq = ''.join(l2)
    if sq == sp: ... else: ...
    - Accepts `s3` ("Sourabh"), reverses it to `sq` ("hbaruoS").
    - Compares `sq` ("hbaruoS") with `sp` ("hbaruoS") instead of `s3` ("Sourabh").
    - Since `sq == sp` is True, prints "The string is a palindrome." (Incorrect).

STEP 5 - Substring check
    s3 = input("Enter substring: ")
    l3 = list(s3)
    if s3 in s: ... else: ...
    - Overwrites `s3` with "hb".
    - `l3` is created but unused.
    - Evaluates "hb" in "Sourabh" -> False, prints "Entered string is not a substring."


--------------------------------------------------------------------------------
4. DATA FLOW
--------------------------------------------------------------------------------

   Keyboard "Sourabh" ---> s = "Sourabh" ---> list(s) ---> li = ['S','o',...] ---> len(li) = 7
                                   |
                                   v
                             reversed(li) ---> l = ['h','b',...] ---> sp = "hbaruoS"
                                   |
   Keyboard "Tanmay"  ---> s2 = "Tanmay" ---> (s == s2?) ---------> "Not equal"
                                   |
   Keyboard "Sourabh" ---> s3 = "Sourabh" -> sq = "hbaruoS" ------> (sq == sp?) -> "Palindrome"
                                                                      (Bug: compared to sp)
                                   |
   Keyboard "hb"      ---> s3 = "hb" -------> (s3 in s?) ---------> "Not a substring"


Variables at a glance:

    s    primary input string (str)
    li   character list of primary string s (list of str)
    l    reversed character list of primary string (list of str)
    a    delimiter string used for joining (str)
    sp   reversed primary string (str)
    s2   secondary input string for equality check (str)
    s3   input string for palindrome, later overwritten for substring (str)
    l1   character list of palindrome input string (list of str)
    l2   reversed character list of palindrome input string (list of str)
    a1   delimiter string used for joining (str)
    sq   reversed palindrome input string (str)
    l3   unused character list of substring input (list of str)


--------------------------------------------------------------------------------
5. LIMITATIONS
--------------------------------------------------------------------------------
  - PALINDROME LOGIC ERROR: Does not properly check if the input string itself 
    is a palindrome; instead compares the input's reverse against a previously 
    reversed string (`sp`).
  - VARIABLE REUSE: Reusing `s3` for two different user inputs creates confusion 
    and discards the palindrome input string.
  - REDUNDANT CONVERSIONS: Unnecessary manual conversion to lists and loop-based 
    reversals when Python natively supports slice notation (`s[::-1]`).
  - CASE SENSITIVITY: Equality, palindrome, and substring checks are case-sensitive 
    ('hb' is not found in 'Sourabh' because of 'b' vs 'B' position/case context).
  - Single execution flow with no loop for repeated tests.


--------------------------------------------------------------------------------
6. SUGGESTED IMPROVEMENTS
--------------------------------------------------------------------------------
  - Refactor using idiomatic Python operations and fix the palindrome logic:

        # 1. Primary string input
        s = input("Enter the string: ")
        print(f"{len(s)} is the length of the string entered.")

        # 2. String Reversal
        s_rev = s[::-1]
        print(f"{s_rev} is the reverse of the string entered.")

        # 3. Equality Check
        s2 = input("Enter the other string: ")
        if s == s2:
            print("The two strings are equal.")
        else:
            print("The strings are not equal.")

        # 4. Palindrome Check (Corrected)
        s_pal = input("Enter the string to be checked for palindrome: ")
        if s_pal == s_pal[::-1]:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")

        # 5. Substring Check
        sub = input("Enter substring: ")
        if sub in s:
            print("Entered string is a substring.")
        else:
            print("Entered string is not a substring.")


--------------------------------------------------------------------------------
7. TEST CASES (behaviour of the code as written)
--------------------------------------------------------------------------------
    s        s2      s3 (Pal)   s3 (Sub)  Length  Equal?     Palindrome?    Substring?
    -------  ------  ---------  --------  ------  ---------  -------------  -----------------
    Sourabh  Tanmay  Sourabh    hb        7       Not equal  Is palindrome  Not a substring
    madam    madam   madam      ada       5       Equal      Is palindrome  Is a substring
    hello    world   racecar    hello     5       Not equal  Not palindrome Is a substring
    Python   Python  12321      th        6       Equal      Not palindrome Not a substring


================================================================================
END OF README
================================================================================