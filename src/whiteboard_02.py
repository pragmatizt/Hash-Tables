"""
Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175

You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""

"""
INPUTS:
Six separate lists in a list(array)

OUTPUT:
Containing one of the elements within a list, and then sums(?) it up.
Output would be a single value

RELATIONSHIP:


TOOLS:


"""

array_1 = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
empty_list = []

for i in array_1:
    empty_list.append(min(i))
print(sum(empty_list))