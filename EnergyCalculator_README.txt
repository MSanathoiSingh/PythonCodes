================================================================================
MOMENTUM AND KINETIC ENERGY CALCULATOR (Python)
================================================================================
Language : Python 3
Purpose  : Accept the mass (kg) and velocity (m/s) of a body and display its
           momentum and its kinetic energy.


--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
Formulas implemented:

    Momentum        p = m * v            (unit: kg m/s)
    Kinetic energy  e = (m * v^2) / 2    (unit: joules, J)

where m = mass in kilograms and v = velocity in metres per second.

Example (from the sample run): m = 52 kg, v = 23 m/s
    p = 52 * 23            = 1196 kg m/s
    e = 52 * 23^2 / 2      = 52 * 529 / 2 = 13754.0 J

NOTE ON THE DOCSTRING: the comment at the top of the source says "e = mc^2,
where c is the velocity". That is incorrect. E = mc^2 is Einstein's mass-energy
equivalence, where c is the speed of light, and it is not what the code does.
The code computes ordinary momentum (m*v) and classical kinetic energy
(1/2 * m * v^2). The docstring should be corrected accordingly.


--------------------------------------------------------------------------------
2. HOW TO RUN
--------------------------------------------------------------------------------
  1. Save the code as momentum.py
  2. Open a terminal in that folder
  3. Run:   python momentum.py
  4. Enter the mass, press Enter, then enter the velocity and press Enter

Sample session:

    Today we will be calculating energy and momentum of a body as instructed by you.
    Please enter the mass of the body in "kg" 52
    Please enter the velocity of the body in "m/s" 23
    The momentum of the body is  1196  kg m/s
    The energy of the body is  13754.0  J

The program runs once and exits. Run it again for another body.


--------------------------------------------------------------------------------
3. WORKING, STEP BY STEP (input: m = 52, v = 23)
--------------------------------------------------------------------------------

STEP 1 - Print the introduction
    s = "Today we will be calculating energy and momentum of a body ..."
    print(s)
    - Stores a greeting string in s and displays it.

STEP 2 - Read the mass
    m = int(input('Please enter the mass of the body in "kg" '))
    - input() returns the typed text as a string ("52").
    - int() converts it to the integer 52 and stores it in m.

STEP 3 - Read the velocity
    v = int(input('Please enter the velocity of the body in "m/s" '))
    - Same process; v = 23.

STEP 4 - Compute the momentum
    p = m * v
    - 52 * 23 = 1196
    - Both operands are ints, so p is an int and prints as 1196.

STEP 5 - Compute the kinetic energy
    e = m*v**2/2
    - Operator precedence: ** is evaluated first, then *, then /.
    - v**2 = 529; m * 529 = 27508; 27508 / 2 = 13754.0
    - "/" is true division in Python 3, so e is always a float (13754.0).

STEP 6 - Display the results
    print('The momentum of the body is ', p, ' kg m/s')
    print('The energy of the body is ', e, ' J')


--------------------------------------------------------------------------------
4. DATA FLOW
--------------------------------------------------------------------------------

   Keyboard "52"  ---- int() ---->  m = 52  --+
                                              |-->  p = m * v        = 1196
   Keyboard "23"  ---- int() ---->  v = 23  --+
                                              |-->  e = m * v**2 / 2 = 13754.0
                                                          |
                                                          v
                                    print(p) -> "... momentum ... 1196 kg m/s"
                                    print(e) -> "... energy ... 13754.0 J"

Variables at a glance:

    s   introductory text (string, printed only)
    m   mass in kg (int)
    v   velocity in m/s (int)
    p   momentum in kg m/s (int)
    e   kinetic energy in joules (float)


--------------------------------------------------------------------------------
5. LIMITATIONS
--------------------------------------------------------------------------------
  - WHOLE NUMBERS ONLY: int() rejects decimals such as 52.5 or 1.5 and raises
    ValueError. Use float() to allow real-valued mass and velocity.
  - NO INPUT VALIDATION: text or an empty entry crashes with ValueError.
  - NEGATIVE MASS is accepted and gives physically meaningless results.
  - NEGATIVE VELOCITY is accepted. Momentum comes out negative (it is a vector
    quantity, so the sign means direction), while energy stays positive
    because v is squared.
  - CLASSICAL PHYSICS ONLY: the formulas are valid for speeds much smaller than
    the speed of light (about 3 x 10^8 m/s).
  - The introductory line says "as instructed by you", but the program only
    asks for mass and velocity.
  - Single use: the program exits after one calculation.


--------------------------------------------------------------------------------
6. SUGGESTED IMPROVEMENTS
--------------------------------------------------------------------------------
  - Accept decimals and reject invalid values:

        try:
            m = float(input('Please enter the mass of the body in "kg" '))
            v = float(input('Please enter the velocity of the body in "m/s" '))
        except ValueError:
            print("Please enter numeric values.")
        else:
            if m < 0:
                print("Mass cannot be negative.")
            else:
                print("Momentum:", m * v, "kg m/s")
                print("Kinetic energy:", 0.5 * m * v**2, "J")

  - Correct the docstring to describe p = mv and E_k = 1/2 mv^2.


--------------------------------------------------------------------------------
7. TEST CASES (behaviour of the code as written)
--------------------------------------------------------------------------------
    m     v     Momentum (kg m/s)   Energy (J)
    ----  ----  ------------------  ----------
    52    23    1196                13754.0
    10    5     50                  125.0
    2     3     6                   9.0
    1     1     1                   0.5
    0     10    0                   0.0
    5     -4    -20                 40.0
    1.5   2     ValueError (int() rejects decimals)


================================================================================
END OF README
================================================================================
