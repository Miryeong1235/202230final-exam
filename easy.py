"""

FUNCTION:
_________

Define a function called merge(first, second). This function accepts two sorted lists called
first and second and returns a new sorted list that contains the elements from first and second.

ASSUMPTIONS (PRECONDITIONS):
____________

The lists passed as parameters, first and second, may not be modified, not even temporarily.

The lists passed as parameters must be pre-sorted.

The lists will always be homogenous and the same types, so they are sortable and can be merged.

The lists can be strings or some other sortable like numbers.

Sample usage example 1:

some_list = [1, 5, 9]
some_other_list = [-10, 44, 100]
sorted_merge = merge(some_list, some_other_list)
print(sorted_merge)
[-10, 1, 5, 9, 44, 100]

Sample usage example 2:

some_list = ["apple", "orange", "tamarind"]
some_other_list = ["applesauce", "bread", "watermelon"]
sorted_merge = merge(some_list, some_other_list)
print(sorted_merge)
["apple", "applesauce", "bread", "orange", "tamarind", "watermelon"]

DOCSTRING:
__________

Yes. Docstrings are needed.

DOCTESTS:
_________

Yes. Two doctests are needed.

UNIT TESTS:
___________

No. No unit tests are needed.

MAIN FUNCTION AND IF-STATEMENT BELOW IT
_______________________________________

Yes. The main function should invoke your function with a simple example.

"""


def merge(first, second):
    """
    Merge two sorted list and sort it.

    :param first: a pre-sorted list
    :param second: a pre-sorted list
    :precondition: first and second must be a list
    :postcondition: merge two sorted list and sort it
    :return: a sorted list

    >>> some_list = [5, 8, 9, -7, 0]
    >>> some_other_list = [10, -77, 1, 3, 20]
    >>> merge(some_list, some_other_list)
    [-77, -7, 0, 1, 3, 5, 8, 9, 10, 20]
    >>> some_list = ["apple", "orange", "tamarind"]
    >>> some_other_list = ["applesauce", "bread", "watermelon"]
    >>> merge(some_list, some_other_list)
    ['apple', 'applesauce', 'bread', 'orange', 'tamarind', 'watermelon']
    """
    new_list = sorted(first + second)
    return new_list


def main():
    first = [1, 5, 9]
    second = [-10, 44, 100]
    sorted_merge = merge(first, second)
    print(sorted_merge)


if __name__ == '__main__':
    main()
