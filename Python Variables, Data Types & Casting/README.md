# Python Variables, Data Types And Casting

**Variables:**

Variables are containers for storing data values. Python has no command for declaring a variable.
1. A variable is created the moment you first assign a value to it.
2. Variables do not need to be declared with any particular type, and can even change type after they have been set.
3. You can get the data type of a variable with the type() function.
4. String variables can be declared either by using single or double quotes.
5. Variable names are case-sensitive.
![img](https://user-images.githubusercontent.com/81376428/129181337-673d7edc-b2ca-40c9-81d0-6aaa55926742.png)
   
Variable Names
1. A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
2. A variable name must start with a letter or the underscore character
3. A variable name cannot start with a number
4. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
5. Variable names are case-sensitive (age, Age and AGE are three different variables)

Legal variable Names
![img_2](https://user-images.githubusercontent.com/81376428/129181409-06842b8a-ef04-40cc-90d6-605ccaa8cc37.png)

Illegal variable Names
![img_1](https://user-images.githubusercontent.com/81376428/129181384-b1f66396-403a-44ea-8063-b79f670fbb7e.png)


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

![img_3](https://user-images.githubusercontent.com/81376428/129181448-b7fabe28-323c-488d-a25d-d772051dc50a.png)

Output Variables:

The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character

If you try to combine a string and a number, Python will give you an error:

![img_4](https://user-images.githubusercontent.com/81376428/129181476-ee0161eb-07f9-42fa-b6ab-2148e22466b0.png)


Global Variables:

Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

![img_5](https://user-images.githubusercontent.com/81376428/129181522-95b500fd-3eb7-4b1b-9381-26a302e13d4a.png)



**Data Types:**

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str

Numeric Types:	int, float, complex

Sequence Types:	list, tuple, range

Mapping Type:	dict

Set Types:	set, frozenset

Boolean Type:	bool

Binary Types:	bytes, bytearray, memoryview

![img_6](https://user-images.githubusercontent.com/81376428/129181636-0efa7516-3493-4b11-b421-e8d7af422ec7.png)
![img_7](https://user-images.githubusercontent.com/81376428/129181657-bcc68534-f731-49e3-a982-225c5c85f2c3.png)
![img_8](https://user-images.githubusercontent.com/81376428/129181669-76c1f6a6-28b0-479f-bb02-4e8d167ca6d2.png)
![img_9](https://user-images.githubusercontent.com/81376428/129181688-7afbbd5b-4d3d-4f06-8cb0-f5e25cc514e6.png)



**Casting:**

There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

1. int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
2. float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
3. str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

![img_10](https://user-images.githubusercontent.com/81376428/129181719-ae678da8-4a92-4d7a-95c7-0848fceda3ab.png)




