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
