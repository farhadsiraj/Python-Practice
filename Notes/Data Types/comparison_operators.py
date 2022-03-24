# ***** Booleans

print(type(True))
print(type(False))
print(1 > 2)
print(2 == 2)

# use the None datatype to create an empty var
emptyVar = None

# Operator                            Description                                                                                            Example
#   ==	    If the values of two operands are equal, then the condition becomes true.	                                                (a == b) is not true.
#   !=	    If values of two operands are not equal, then condition becomes true.	                                                    (a != b) is true
#   >	    If the value of left operand is greater than the value of right operand, then condition becomes true.	                    (a > b) is not true.
#   <	    If the value of left operand is less than the value of right operand, then condition becomes true.	                        (a < b) is true.
#   >=	    If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	        (a >= b) is not true.
#   <=	    If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	            (a <= b) is true.


print(1 < 2 < 3)
print(1 < 2 and 2 < 3)
print(1 < 3 > 2)
print(1 < 3 and 3 > 2)
print(1 == 2 or 2 < 3)
print(1 == 1 or 100 == 1)

# not returns the opposite boolean
print(not 1 == 1)
