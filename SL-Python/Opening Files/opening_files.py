opening_of_da_files = """
Opening Files
You can use Python to read and write the contents of files.
Text files are the easiest to manipulate. Before a file can be edited, it must be opened, using the open function.
myfile = open("filename.txt")

The argument of the open function is the path to the file. 
If the file is in the same directory as the program, you can specify only its name.


What's the most elegant and Pythonic way to open files and make sure they get closed when you're done?
Use the 'with' keyword:

http://eng.handshake.com/python/2014/08/07/close-yr-files/

http://www.tutorialspoint.com/python/python_files_io.htm


Example:
with open(name, 'w+') as f:
    f.write(data)


Remember to use \\ while defining path of the file..
Like
myfile = open("E:\\file1.txt")

You can open any file type, with the open function you can open .txt and .csv, if
you want to open up another file type, you would need to use a specific module to 
that type.

with open("lo.txt","w") as a:
    a.write("lo write this program")
a=open("lo.txt","r")
print a.read()
a.close()
this program is  easy to create and write a text file


FILE MODES:
===========
"r"
Read from file - YES
Write to file - NO
Create file if not exists - NO
Truncate file to zero length - NO
Cursor position - BEGINNING

"r+"
Read from file - YES
Write to file - YES
Create file if not exists - NO
Truncate file to zero length - NO
Cursor position - BEGINNING

"w"
Read from file - NO
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - YES
Cursor position - BEGINNING

"w+"
Read from file - YES
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - YES
Cursor position - BEGINNING

"a"
Read from file - NO
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - NO
Cursor position - END

"a+"
Read from file - YES
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - NO
Cursor position - END



Opening Files
=============
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default. 
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
For example:
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")


Once a file has been opened and used, you should close it.
This is done with the close method of the file object.
file = open("filename.txt", "w")
# do stuff to the file
file.close()



Reading Files
=============
The contents of a file that has been opened in text mode can be read using the read method.
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

This will print all of the contents of the file "filename.txt".


To read only a certain amount of a file, you can provide a number as an argument to the read function. 
This determines the number of bytes that should be read. 
You can make more calls to read on the same file object to read more of the file byte by byte. 
With no argument, read returns the rest of the file.
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()



Is a byte equal to a character (in this context)?
=================================================
With no information given about text encoding, assuming that 1 byte corresponds to 1 character is the usual (and often correct) guess.

if you're in need of computation per single character and unsure about the input encoding, you can still read the entire file and then further process the read result character by character.

Solutions such as this one can be found here, at one particularly popular spot:
http://stackoverflow.com/questions/2988211/how-to-read-a-single-character-at-a-time-from-a-file-in-python

And in case you want to get it right while you're on the subject, give this a read:

http://www.joelonsoftware.com/articles/Unicode.html
(Popular article titled "The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!).")

...so to answer your question, in a nutshell: 

Yup, at least there's a good chance you're right. (;



After all contents in a file have been read, any attempts to read further from that file will return an empty string, because you are trying to read from the end of the file.
file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

Result:
/>>>
Re-reading

Finished
/>>>


In order to avoid this pain of calling the open function again and again, Save the file.read() to a variable.
x=file.read() 
Now you can access the contents of the file anytime by printing x.

Note: if the file is modified, x won't be updated. It's just a copy of the state of the file when we assigned it.

How to reset the file so that it can be reread from the first line
==================================================================
Just imagine the reading "cursor" is at the end of file after having read it. So there is nothing left to read.
But we can reset the "cursor" by another way. This is not the only one way,which sololearn introduced.
Here is example of reseting file to read it again:
name_of_file.seek(0)
By using this method "cursor" will go to start of the file,and after you print 
name_of_file.read()
File will be read again.




To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.
For example:
file = open("filename.txt", "r")
print(file.readlines())
file.close()

Result:
/>>>
['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']
/>>>

You can also use a for loop to iterate through the lines in the file:
file = open("filename.txt", "r")

for line in file:
    print(line)

file.close() 

Result:
/>>>
Line 1 text

Line 2 text

Line 3 text
/>>>


In the output, the lines are separated by blank lines, as the print function automatically adds a new line at the end of its output.

How to get rid of empty lines when calling the open function along with the readlines method.
=============================================================================================
To avoid the extra lines skipped. do this. 
file = open("filename.txt" , "r")
lines = file.readlines()
for line in lines:
    print(line, end="")   #This is the part that does it.
file.close()



Actually there are two new lines generated. One of them was caused by the print and the other one is because of \n at the end of each element of our list. If you don't want that \n at the end to exist( in case you want check that string for matching) you can use the splitline() method:

file = open("filename.txt", "r")
lines = file.read().splitlines()

Now your list has the following contents:

['Line 1 text', 'Line 2 text', 'Line 3 text']

As you see, \n has been removed!



file.readline() returns a string, whereas file.readlines() retuns a list


what if we want to print line 5 to 10 of the file?
==================================================

One way is to read all the lines of the file into an array of strings and then print between the range of 5 and 10:

f = open("file.txt", "r")

contents = f.readlines()

for i in range(5,11):
    print(contents[i])

remember, the range function doesn't include the upper limit (in this case 11), so always put where you want it to stop *plus one*.
"""

print(opening_of_da_files)