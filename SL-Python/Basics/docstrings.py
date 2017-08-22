def shout(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")


shout("spam")
print(shout.__doc__)  # how to access the docstrings
help(shout)  # another way to access docstrings