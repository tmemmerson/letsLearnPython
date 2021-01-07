import datetime
myNow = datetime.datetime.now()
print(myNow)

myNumber =3
myText = "Tristan's favorite number is"

x=10
y="10"
z=10.1
sum1=x+x
sum2=y+y
sum3=z+z


print(myText, myNumber)

print(sum1, sum2, sum3)

print(type(x), type(y), type(z))

list1=list(range(1,10))
""" gives output of 1,2,3,4,5,6,7,8,9 """
list2=list(range(1,10,2)) 
""" gives output of 1,3,5,7,9 because the 3rd arguement is the step """ 

print(list1,list2)

""" dir(datatype) provides list of all the methods you can use with that type """

student_grades=[9.1,8.8,7.5]

gradeSum=sum(student_grades)
print(gradeSum)
length=len(student_grades)
mean=gradeSum/length
print(mean)

monday_temperatures = [9.1, 8.8, 7.5]
""" this is a list """
student_grades2={"Marry": 9.1, "Sim": 8.8, "John": 7.5}
""" this is a dictionary """

""" tuples are immutable
lists are mutable """


""" Integers are for representing whole numbers:

rank = 10
eggs = 12
people = 3
Floats represent continuous values:

temperature = 10.2
rainfall = 5.98
elevation = 1031.88
Strings represent any text:

message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
Lists represent arrays of values that may change during the course of the program:

members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
Dictionaries represent pairs of keys and values:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
Keys of a dictionary can be extracted with:

phone_numbers.keys()
Values of a dictionary can be extracted with:

phone_numbers.values()
Tuples represent arrays of values that are not to be changed during the course of the program:

vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
To find out what attributes a type has:

dir(str)
dir(list)
dir(dict)
To find out what Python builtin functions there are:

dir(__builtins__)
Documentation for a Python command can be found with:

help(str)
help(str.replace)
help(dict.values) """