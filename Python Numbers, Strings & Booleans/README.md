# Python Numbers, Strings And Booleans

Numbers:

There are three numeric types in Python:

1. int:
   
   Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
2. float:
   
   Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
3. complex:

   Complex numbers are written with a "j" as the imaginary part
![img](https://user-images.githubusercontent.com/81376428/129203120-0eeb8d03-216b-439b-8b19-3dbfb623e10d.png)

   
Float can also be scientific numbers with an "e" to indicate the power of 10.

![img_1](https://user-images.githubusercontent.com/81376428/129203146-e5ba3f59-4de9-43a7-ac07-d8eae2c24bcf.png)


Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods

![img_2](https://user-images.githubusercontent.com/81376428/129203184-611a7a47-096a-4525-bac4-ba6818c800fc.png)


   
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

![img_3](https://user-images.githubusercontent.com/81376428/129203211-6cf2590c-0866-4b9c-971a-35275b20ba95.png)
![img_4](https://user-images.githubusercontent.com/81376428/129203241-fd867509-c17e-4f4e-9f71-04fbb59d2acf.png)
![img_5](https://user-images.githubusercontent.com/81376428/129203261-9a3b7499-bb69-48e3-a41d-1fd3ff409a30.png)


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

![img_6](https://user-images.githubusercontent.com/81376428/129203282-d5d59dbb-48cb-4d4b-9ca4-551e88f5998a.png)


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

![img_7](https://user-images.githubusercontent.com/81376428/129203316-44b75720-808b-4152-8538-421971f76c12.png)


D] String Concatenation

To concatenate, or combine, two strings you can use the + operator.

To add a space between them, add a " "

![img_8](https://user-images.githubusercontent.com/81376428/129203354-798eff5a-ee97-4222-ae32-c77641bbd175.png)

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

![img_9](https://user-images.githubusercontent.com/81376428/129203393-d8a247c6-acc7-43d7-8878-abcc08c4f3c8.png)


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

![img_10](https://user-images.githubusercontent.com/81376428/129203432-a03b0a3f-d2cd-4b13-a894-778d3393af41.png)


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

![img_11](https://user-images.githubusercontent.com/81376428/129203465-cab65a81-e538-4b60-b970-0a25a875bbbf.png)



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

![img_12](https://user-images.githubusercontent.com/81376428/129203498-9094f9f1-cfb3-490f-bf2c-05f5783bc4f4.png)












   






