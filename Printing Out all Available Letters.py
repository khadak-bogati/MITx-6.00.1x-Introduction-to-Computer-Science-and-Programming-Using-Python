Problem 3 - Printing Out all Available Letters
10.0/10.0 points (graded)
Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:

>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
Code Editor
1
def getAvailableLetters(lettersGuessed):
2
    '''
3
    lettersGuessed: list, what letters have been guessed so far
4
    returns: string, comprised of letters that represents what letters have not
5
      yet been guessed.
6
    '''
7
    # FILL IN YOUR CODE HERE...
8
    string = "abcdefghijklmnopqrstuvwxyz"
9
    temp = ""
10
    for i in string:
11
        if i not in lettersGuessed:
12
            temp += i
13
    return temp
