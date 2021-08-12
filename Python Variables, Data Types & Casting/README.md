# Python Variables, Data Types And Casting

Variables:

Variables are containers for storing data values. Python has no command for declaring a variable.
1. A variable is created the moment you first assign a value to it.
2. Variables do not need to be declared with any particular type, and can even change type after they have been set.
3. You can get the data type of a variable with the type() function.
4. String variables can be declared either by using single or double quotes.
5. Variable names are case-sensitive.
![img.png](img.png)
   
Variable Names
1. A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
2. A variable name must start with a letter or the underscore character
3. A variable name cannot start with a number
4. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
5. Variable names are case-sensitive (age, Age and AGE are three different variables)

Legal variable Names
![img_2.png](img_2.png)

Illegal variable Names
![img_1.png](img_1.png)


Multi Words Variable Names
Variable names with more than one word can be difficult to read.
There are several techniques you can use to make them more readable:
1. Camel Case:
Each word, except the first, starts with a capital letter:
   
myVariableName = "John"

2. Pascal Case:
Each word starts with a capital letter:
   
MyVariableName = "John"

3. Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"

Assign Multiple Values

1. Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line

Note: Make sure the number of variables matches the number of values, or else you will get an error.

2. One Value to Multiple Variables

And you can assign the same value to multiple variables in one line

3. Unpack a Collection

If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

![img_3.png](img_3.png)

Output Variables:

The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character

If you try to combine a string and a number, Python will give you an error:

![img_4.png](img_4.png)


Global Variables:

Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

![img_5.png](img_5.png)



Data Types:

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str

Numeric Types:	int, float, complex

Sequence Types:	list, tuple, range

Mapping Type:	dict

Set Types:	set, frozenset

Boolean Type:	bool

Binary Types:	bytes, bytearray, memoryview

![img_6.png](img_6.png)
![img_7.png](img_7.png)
![img_8.png](img_8.png)
![img_9.png](img_9.png)


Casting:

There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

1. int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
2. float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
3. str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

![img_10.png](img_10.png)




