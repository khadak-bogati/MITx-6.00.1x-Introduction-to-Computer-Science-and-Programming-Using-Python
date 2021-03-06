Problem 1 - Is the Word Guessed
10.0/10.0 points (graded)
Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(isWordGuessed(secretWord, lettersGuessed))
False
For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

Code Editor
1
def isWordGuessed(secretWord, lettersGuessed):
2
    '''
3
    secretWord: string, the word the user is guessing
4
    lettersGuessed: list, what letters have been guessed so far
5
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
6
      False otherwise
7
    '''
8
    # FILL IN YOUR CODE HERE...
9
    for i in secretWord:
10
        if i not in lettersGuessed:
11
            return False
12
    return True
13
​
