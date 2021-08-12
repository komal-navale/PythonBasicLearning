# Python Numbers, Strings And Booleans

Numbers:

There are three numeric types in Python:

1. int:
   
   Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
2. float:
   
   Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
3. complex:

   Complex numbers are written with a "j" as the imaginary part
![img.png](img.png)
   
Float can also be scientific numbers with an "e" to indicate the power of 10.

![img_1.png](img_1.png)

Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods

![img_2.png](img_2.png)

   
Strings:

A] 
1. Assign String to a Variable

    Assigning a string to a variable is done with the variable name followed by an equal sign and the string

2. Multiline Strings

    You can assign a multiline string to a variable by using three double quotes or three single quotes.

3. Strings are Arrays

    Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

    However, Python does not have a character data type, a single character is simply a string with a length of 1.

    Square brackets can be used to access elements of the string.
   
4. Looping Through a String

    Since strings are arrays, we can loop through the characters in a string, with a for loop.

5. String Length

    To get the length of a string, use the len() function.

6. Check String

    To check if a certain phrase or character is present in a string, we can use the keyword in.

7. Check if NOT

    To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

![img_3.png](img_3.png)
![img_4.png](img_4.png)
![img_5.png](img_5.png)

B] Python - Slicing Strings

1. Slicing

   You can return a range of characters by using the slice syntax.

   Specify the start index and the end index, separated by a colon, to return a part of the string.

2. Slice From the Start

   By leaving out the start index, the range will start at the first character

3. Slice To the End

   By leaving out the end index, the range will go to the end

4. Negative Indexing

   Use negative indexes to start the slice from the end of the string

   ![img_6.png](img_6.png)

C] Python - Modify Strings

Python has a set of built-in methods that you can use on strings.

1. Upper Case

   The upper() method returns the string in upper case

2. Lower Case

   The lower() method returns the string in lower case

3. Remove Whitespace

   Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

4. Replace String

   The replace() method replaces a string with another string

5. Split String

   The split() method returns a list where the text between the specified separator becomes the list items

   ![img_7.png](img_7.png)

D] String Concatenation

To concatenate, or combine, two strings you can use the + operator.

To add a space between them, add a " "

![img_8.png](img_8.png)

E] Python - Format - Strings

we cannot combine strings and numbers like this:

Example

age = 36

txt = "My name is John, I am " + age

print(txt)

But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are.

The format() method takes unlimited number of arguments, and are placed into the respective placeholders

You can use index numbers {0} to be sure the arguments are placed in the correct placeholders

![img_9.png](img_9.png)

F] Escape Character

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes.

txt = "We are the so-called "Vikings" from the north."

To fix this problem, use the escape character \"

Other Escape characters in Python are

Code	     Result

\' -	     Single Quote	

\\ -	     Backslash	

\n -	     New Line	

\r -	     Carriage Return

\t -	     Tab	

\b -	     Backspace	

\f -	     Form Feed	

\ooo -	     Octal value

\xhh -	     Hex value

![img_10.png](img_10.png)

G] Python - String Methods

String Methods

Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

Method	Description

capitalize()-	Converts the first character to upper case

casefold()-	Converts string into lower case

center()-	Returns a centered string

count()-	Returns the number of times a specified value occurs in a string

encode()-	Returns an encoded version of the string

endswith()-	Returns true if the string ends with the specified value

expandtabs()-	Sets the tab size of the string

find()-	Searches the string for a specified value and returns the position of where it was found

format()-	Formats specified values in a string

format_map()-	Formats specified values in a string

index()-	Searches the string for a specified value and returns the position of where it was found

isalnum()-	Returns True if all characters in the string are alphanumeric

isalpha()-	Returns True if all characters in the string are in the alphabet

isdecimal()-	Returns True if all characters in the string are decimals

isdigit()-	Returns True if all characters in the string are digits

isidentifier()-	Returns True if the string is an identifier

islower()-	Returns True if all characters in the string are lower case

isnumeric()-	Returns True if all characters in the string are numeric

isprintable()-	Returns True if all characters in the string are printable

isspace()-	Returns True if all characters in the string are whitespaces

istitle()-	Returns True if the string follows the rules of a title

isupper()-	Returns True if all characters in the string are upper case

join()-	Joins the elements of an iterable to the end of the string

ljust()-	Returns a left justified version of the string

lower()-	Converts a string into lower case

lstrip()-	Returns a left trim version of the string

maketrans()-	Returns a translation table to be used in translations

partition()-	Returns a tuple where the string is parted into three parts

replace()-	Returns a string where a specified value is replaced with a specified value

rfind()-	Searches the string for a specified value and returns the last position of where it was found

rindex()-	Searches the string for a specified value and returns the last position of where it was found

rjust()-	Returns a right justified version of the string

rpartition()-	Returns a tuple where the string is parted into three parts

rsplit()-	Splits the string at the specified separator, and returns a list

rstrip()-	Returns a right trim version of the string

split()-	Splits the string at the specified separator, and returns a list

splitlines()-	Splits the string at line breaks and returns a list

startswith()-	Returns true if the string starts with the specified value

strip()-	Returns a trimmed version of the string

swapcase()-	Swaps cases, lower case becomes upper case and vice versa

title()-	Converts the first character of each word to upper case

translate()-	Returns a translated string

upper()-	Converts a string into upper case

zfill()-	Fills the string with a specified number of 0 values at the beginning

![img_11.png](img_11.png)


Booleans:

Booleans represent one of two values: True or False.

1. When you compare two values, the expression is evaluated and Python returns the Boolean answer

2. When you run a condition in an if statement, Python returns True or False

3. The bool() function allows you to evaluate any value, and give you True or False in return

4. Most values are true

   Almost any value is evaluated to True if it has some sort of content.

   Any string is True, except empty strings.

   Any number is True, except 0.

   Any list, tuple, set, and dictionary are True, except empty ones.

5. Some values are false

   There are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
   
   One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False

6. You can create functions that returns a Boolean Value

![img_12.png](img_12.png)











   






