#HOW TO RUN TEST

- Install dependencies: pip install -r requirements.txt
- Run the tests: python -m pytest -v

#WHY AN EQUILATERAL CANT BE RIGHT

- An equilateral cant be right because if all sides are equal to eachother then two squared sides can never equal the third side squared. For example for 2^2 2^2 2^2, 4+4=8 not 4

#THE EQUIVALENCE CLASSES

- Zero or Negative sides -> Invalid
- Inequality Fails -> Invalid
- Equilateral
- Isosceles
- Scalene
- Right (Scalene or Isosceles)

#BOUNDARIES IDENTIFIED

- Degenerate case
- Non whole number right triangle

#COPILOT REVIEW LOG
|Test|Copilot-suggested?|Kept / Edited / Rejected|Why|
|---|---|---|---|
|test_is_valid_triangle|yes|Kept|Matched the Spec, 3,4,5 is True|
|test_equilateral|yes|Kept|Matched the Spec, 3,3,3 is equilateral|
|test_isosceles|yes|Kept|Matched the Spec, 3,3,4 is isosceles|
|test_scalene|yes|Edited|3 of the cases were right scalene triangles 3,4,5 -> changed them to scalene for exmaple 4,5,6 is scalene|
|test_right_triangle|yes|Kept|Matches the spec, 3,4,5 is right scalene|
|test_invalid_zero_or_negative_side|yes|Kept|Matches the Spec, 3,-1,4 is invalid|
|test_invalid_inequality_fails|yes|Edited|All cases were degenerate-> changed the numbers for example 12,13,26 is invalid|
|test_degenerate_is_invalid|yes|Kept|Matches the Spec, 1,1,2 is invalid|
|test_right_isosceles_non_integer|yes|Kept|Matched the Spec, 1, math.sqrt(2), 1 is right isosceles|

#ACCEPTANCE CRITERIA

- Given three lengths, if it is a non right triangle, it will return Equilateral or Isosceles or Scalene
- Given three lengths, if it includes a 0, negative number or two smaller sides that dont surpass the 3rd side, it will return invalid instead of an error
- Given three lengths, if it is a right triangle including when the sides aren't whole numbers, it will return Right Scalene or Right Isosceles

#AI-Use Disclosure section

- Copilot Assisted in drafting the bodies of the methods for test_triangle.py, code was then reviewed and edited if needed. Also listed in Copilot Review Log
