"""
03.1.1 True or False. For each of the following pairs of values, perform an equality test, assign the 
result to a variable, and display it. Try to predict what the result of each test will be.
I. 1, 1;
II. 1, 1.0;
III. 2.0, sqrt(4);
IV. '1', 1;
V. 'hello', 'Hello'.
"""

from math import sqrt

value_1 = (1==1)
print(f"The first comparison is: {value_1}")

value_2 = (1 == 1.0)
print(f"The second comparison is: {value_2}")

value_3 = (2.0 == sqrt(4))
print(f"The third comparison between {2.0} and {sqrt(4)}is : {value_3}")

value_4 = ('1' == 1)
print(f"The fourth comparison between '1' and 1 is: {value_4}")

value_5 = ('hello' == 'Hello')
print(f"The fifth comparison between 'hello' and 'Hello' is: {value_5}")
