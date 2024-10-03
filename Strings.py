Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string is made using double or single quotations (be consistent in your documentation)
x = "Homer Simpson" #this is similar to x = 'Homer Simpson'

#to check what data type you're working with, use the type() function
type(x)
<class 'str'>

#the str() function can be used convert other data types into string
y = 45367
str (y)
'45367'

>>> #some modifications include upper(), lower(), title()
>>> print(x.lower())
homer simpson
>>> print(x.upper())
HOMER SIMPSON
>>> print("the okay gatsby".title())
The Okay Gatsby
>>> 
>>> #one can also replace a line or character in a string with another
>>> print(x.replace("Homer", "Bart"))
Bart Simpson
>>> 
>>> #to split string, use their index positions
>>> print(x[5:11])
 Simps
>>> 
>>> #strings can be joined using the + operator
...  
>>> a = x + " "+ "and" + "Marge Simpson"
>>> print(a)
Homer Simpson andMarge Simpson
>>> a = x + " " + "and" + " "+ "Marge Simpson"
>>> print(a)  #note that this rewrites the value of a
Homer Simpson and Marge Simpson
>>> 
>>> #to oin string with other data types, use f-strings
>>> f_name = James
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    f_name = James
NameError: name 'James' is not defined
>>> f_name ="James"
>>> age = 33
>>> print(f"My name is {f_name} and I am {age} years old")
My name is James and I am 33 years old
>>> txt = f"My name is {f_name} and I am {age:.2f} years old"
>>> #note that the .2f sets the age to 2 decimal places
>>> print(txt)
My name is James and I am 33.00 years old
