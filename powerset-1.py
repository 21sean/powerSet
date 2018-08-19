
# Python syntax: recursion, for loop using range, if, random
#                print using the end parameter (see documentation)
#                lists and cloning

"""
    Preamble (why we are implementing sets using lists in this question):
    Since elements of Python sets must be hashable,
    a Python set cannot contain Python sets.
    For example, a powerset cannot be represented using Python sets.
    So, we will simulate a set using lists instead.
    For example, [[1,2], [1,3]] will represent the set {{1,2}, {1,3}}.
    This works, since lists do not have the immutability constraint.
    It is actually very common to have to model things in code creatively
    like this.
"""

from random import *

def randomSet (n, up):

    """Build a random 'set' of integers.

    A set will be implemented as a list.
    There are two differences between a list and a set to keep in mind:
    - a list has order (it is a sequence), but a set does not
      (this difference probably won't affect your code)
    - a list can have duplicate elements, but a set never does
      (this difference will definitely affect the code of this function)

    #>>> randomSet(4, 10)
    [5, 3, 2, 8]

    Params: 
        n (int): # of integers in the set
        up (int): upperbound 
    Returns: (list) random 'set' of n integers between 0 and up, inclusive
    """
    A = []
    for i in range(n):
        C = randint(0, (up)-1)
        a = (range(up)[C])
        if a not in A:
            A.append(a)
    return A

def powerset (A):

    """Build the powerset of A.
    Given a set A, the powerset of A is the set of all subsets of A.

    Hint: recursion, anyone? no, really, you need to use recursion
          see lecture for the way to think about powerset recursively
    Hint: there are two base cases to the recursion: 
          first base case: size of A is 0
          second base case: size of A is 1 
    Hint: when you are changing a list, cloning makes it safer
    Hint: you may not want to test this function on a set of size 40,
          unless you are very patient, are not concerned about the due date,
          and have a lot of spare cash for memory upgrades
          (if that is not clear, watch the Eames video again)

    #>>> powerset ([1,2])
    [[], [1], [2], [1,2]]
    
    Params: A (list): finite set of integers, represented internally as a list
    Returns: (list) powerset of A, represented internally as a list
    """

    B = []
    if A == []:
        return [[]]
    if len(A) == 1:
        return [A]
    else:
        ss = powerset(A[0:-1])
        B = B + ss
        B.append([A[-1]])
        for a in ss:
            B.append(a + [A[-1]])
        B = [[]] + B
        PS = []
        for i in B:
            if i not in PS:
                PS.append(i)
        return PS


def printSet (A):
    """Print a 'set', using standard set notation.
    Recall that we needed to represent a set internally using a list,
    so that we could represent a powerset.
    To restore the correct interpretation, this function prints the 'set'
    in true set notation.
    Note that the elements of a 'set' could be 'sets'.
    The set and only the set is printed: no newline character is printed.
    The lack of a newline character will allow recursion to work cleanly.

    Hint: recursion
    Hint: how would you know whether you were at the base case?
          This fact will be useful:
          the elements of A are of only two types: int or list.
    Hint: you can print without adding a newline (see print documentation
          and discussion in lecture)
    #>>> printSet ([1,2,3,4])
    {1, 2, 3, 4}

    #>>> printSet ([[1,2], [1,3]]
    {{1, 2}, {1, 3}}
    Params: A (list): set of integers, represented internally as a list
    """
    print("{", end="")
    for i in range(len(A)):
        if type(A[0]) != list:
            print(A[i], end="")
        else:
            printSet(A[i])
        if i < len(A) - 1:
            print(", ", end="")
    print("}", end="")



# ------------------------------------------------------------------------------