# Text Analyzer
# This is an example project, showing a program that analyzes a sample file to find what percentage of the text each character occupies.
# This section shows how a file could be open and read.


# Remember! With as f , you never have to close

filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()

print(text)


# They used the "with" function, meaning that there is no need to close the file.
# But the problem it is that we have stored everything into a variable and if we don't wan't to use memory,
# it will be better to delete the variable after using it. We can always reopen the file if we need it.

# If we want just to print what it is inside the file, a better option is:

# with open(filename) as f:
#   print(f.read())

# This part of the program shows a function that counts how many times a character occurs in a string.

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


# This function takes as its arguments the text of the file and one character, returning the number of times that character appears in the text.
# Now we can call it for our file.

# filename = input("Enter a filename: ")
# with open(filename) as f:
#  text = f.read()

# print(count_char(text, "r"))

# The character "r" appears 83 times in the file.



dic = {}
for c in "abcdefghijklmnopqrstuvwxyz":
    dic[c] = 0

doc = text.lower()
for c in doc:
    for char in "abcdefghijklmnopqrstuvwxyz":
        if c == str(char):
            dic[str(char)] += 1

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * dic[char] / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))


# The next part of the program finds what percentage of the text each character of the alphabet occupies.

# for char in "abcdefghijklmnopqrstuvwxyz":
#    perc = 100 * count_char(text, char) / len(text)
#    print("{0} - {1}%".format(char, round(perc, 2)))

# Let's put it all together and run the program:
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))