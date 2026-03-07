# def cal_avg(*nums):
#     avg=sum(nums)/len(nums)
#     return avg

# print(cal_avg(1,2))


# def full_name(**name):
#     print(name)
#     print(f"My full name is {name["fname"]} {name["mname"]} {name["lname"]}")

# full_name(lname="Ali",mname="Muhammad")


# def create_user(**details):
#     print(f"ID: {details["id"]}\n")
#     print(f"Name: {details["name"]}\n")
#     print(f"Department: {details["department"]}\n")
#     print(f"Phone Number: {details["phone"]}\n")

# create_user(id=1,name="Ali",department="Software",phone=121212,city="hyd")

# try:
#     num=input("enter a number")
#     sq=num**2
#     print(sq)
# except TypeError:
#     print("The provided value is incorrect")
#     num=int(input("Enter again"))
#     # num=int(num)
#     print(f"now its correct: {num**2}")



# num= int(input("enter a number(9-5): "))
# if num<8 or num>15:
#     raise ("The number is not between 9-5 range")
# lt=["q","w","e"]
# mt="&&".join(lt)
# print(mt)

# def name(**n):
#     # print(names)
#     names=[n.get("fname"),n.get("mname"),n.get("lname")]
#     valid_words=[]
#     for name in names:
#         if name:
#             valid_words.append(name)
#     full_name=" ".join(valid_words)
#     print(full_name)

# name(fname="Ali",lname="Shaikh",mname="Muhammad")
# name(lname="Shaikh",mname="Muhammad")
# name(fname="Ali")

# users={}

# def create_user(id,**details):
#     if not id:
#         raise ValueError("Id is required")
#     users[id]=(details)

# def read_user(id):
#     if not id:
#         raise ValueError("Id is required")
#     print(users[id])

# def update_user(id,**updates):
#     if not id:
#         raise ValueError("Id is required")    
#     users[id].update(updates)

# def delete_user(id):
#    del users[id]

# create_user(1,Name="Ali",Department="Physics") 
# create_user(2,Department="Physics") 

# print(users)

# class NumberisGreater(Exception):
#     pass

# num=int(input("Enter a number: "))
# if num > 15:    
#     raise NumberisGreater("Number is greater than 15")

# import os

# for i in range(1,100):
#     os.makedirs(f"Folder ")

# a= [1,2,3]
# b= [1,2,3]

# print("same") if a is b else print("different")

# try: 
#     lt=[1,2,3,4]
#     print(lt[6])
# except IndexError:
#     print("Wrong")

# import os
# print(os.removedirs("new_foler/new_dolfer2"))

# num= int(input("Enter a number: "))
 
# while num==2:
#     print("Yes")
# else:
#     print("no")

# from new_file import text
# text()

# num=2

# try:
#     num.lower()
# except:
#     print("No")
# finally:
#     print("This will always execute")


# File Handling

# # Creating Mode

# file= open("note.txt","x")

# # Reading Mode

# file=open("note.txt","r")
# print(file.read())

# # Writing Mode

# file=open("note.txt","w")
# file.write("hello")

# # Appending Mode

# file=open("note.txt","a")
# file.write("world")
# file.close()

# with open ("note.txt","a") as file:
#     nums=[1,2,3,4]
#     file.write("1,2,3")    


# with open("file.xml") as file:
#     print(file.readable())

# with open("note.txt") as file:
#     text=file.readlines()
#     marks=text[0]
#     names=text[1]
#     marks=marks.split(",")
#     names=names.split(",")
#     for i in range(3):
#         print(f"Student {names[i]} have {marks[i]} .")
    # print(marks)
    # print(names)

# def write_text(filename,text):
#     with open(filename,"w") as file:
#         file.write(text)
#         print("Content wrote successfully")
#     with open(filename) as file:
#         print(f"The content written in {filename} is: \n{file.read()}")

# seek(), tell() and truncate()

# Seek and Tell Demonstation: 

# with open("note.txt","r") as file:
#     print(file.tell())
#     print(file.read())
#     file.seek(6)
#     print(file.tell())
#     print(file.read())

# Truncate Demonstration:

# with open("note.txt","r+") as file:
#     # file.truncate(4)
#     # file.seek(6)
#     # text=file.read()
#     # print(list(text))

# import os
# class text_not_present():
#     pass

# if os.path.exists("data"):
#     pass
# else:
#     os.mkdir("data")

# if os.path.exists("data/notes.txt"):
#     pass
# else:
#     with open("data/notes.txt","x") as file:
#         pass

# def add_note(**kwargs):
#     if "text" not in kwargs or not kwargs["text"]:
#         raise text_not_present("Text was not provided")
#     with open("data/notes.txt","a") as file:
#         file.write(kwargs["text"]+"\n")
#         print("Content Added Successfully")


# def view_notes():
#     with open("data/notes.txt") as file:
#         print(f"Output: {file.read()}")

# def process_user(func):
#     with open("data/notes.txt","r") as file:
#         content=file.read()
#         print(f"{func(content)}")

# while True:
#     print("1. Add Note")
#     print("2. View Notes")
#     print("3. Process Notes")
#     print("4. Exit\n")

#     choice=input("Choose an option from above: ")

#     if choice=="1":
#         content=input("Enter the text you would like to add: ")
#         add_note(content)

#     elif choice=="2":
#         view_notes()

#     elif choice==3:
#         print("1. Length")
#         print("2. Lower")
#         print("3. Upper")
#         choice=int(input("Pick any function from above: "))

#         if choice=="1":
#             lambda note: len(note)

#         elif choice=="2":
#             lambda note: note.lower()

#         elif choice=="3":
#             lambda note: note.upper()

#         else:
#             print("Unknown number, so exiting")
#             break
    
#     elif choice=="4":
#         print("Exiting")
#         break

    
# Map, Filter and Reduce

nums=[1,2,3,4,5]

# #Way 1
# def sqr(num):
#     return num ** 2

# emp_nums=[]
# for n in nums:
#     emp_nums.append(sqr(n))

# print(emp_nums)

# Way 2
# print(list(map(sqr,nums)))

# Way 1
# def divisible_2(num):
#     if num%2==0:
#         return num 

# emp_nums=[]
# for n in nums:
#     emp_nums.append(divisible_2(n))
# # print(emp_nums)

# # Way 2
# print(tuple(filter(divisible_2,nums)))

# from functools import reduce

# nums=(1,2,3,4)
# # Way 1

# total=0
# for n in nums:
#     total+=n
# # print(total)

# # Way 2

# print(reduce(lambda a,b:a+b ,nums))

# class Student:
#     def __init__(self):
#         pass
#         # self.name=0
#         # id=0
#         # self.age=0
#         print("Object created successfully")

#     def intro(self):
#         print(f"The student name is: {self.name} and age is {self.age}")

#     def greet(self):
#         print(f"Hello there, my name is {self.name} and age is {self.age}")

#     def id_check(self,id):
#         print(f"The student id is {id}")

# s1=Student()

# s1.intro()
# s1.greet()
# s1.id_check(5)

# class Other_students:
#     name="ali"
#     age=12
#     id=0
#     def intro(self,name,age):
#         print(f"Hey, I'am {name} and age is {age}")

#     def show_id(id):
#         print(f"The good student's id is {id}")

# s2=Other_students()

# s2.intro(21)
# # s2.show_id(111)

# class Student:
#     def __init__(self,name,age):
#         print("This is __init__")
#         if name=="":
#             raise ValueError("Name was not provided")
#         if age<=0:
#             raise ValueError("Age can't be negative")
#         self.name=name
#         self.age=age

#     def info(self):
#         return(f"The student name is {self.name} and age is: {self.age}")

#     def greet(self):
#         print(f"Hello, \n{self.info()}")

# s1=Student("ali",22)

# s1.greet()


# class Bank:
#     def __init__(self,balance):
#         self.balance=balance

#     def add_amount(self,value):
#         self.balance+=value
#         self.add_15()

#     def show_balance(self):
#         print(self.balance)

#     def add_15(self):
#         self.balance+=15

# b1=Bank(200)
# b1.show_balance()

# b1.add_amount(300)
# b1.show_balance()

# # s1.custom()
# # s1.info()
# import time

# def dec(func):
#     def wrapper(*args,**kwargs):

#         print(f"The function name is {func.__name__} and the arguments its taking are {args,kwargs}")
#         func(*args,**kwargs)
#     return wrapper

# @dec
# def rand(**kwargs):
#     return (kwargs)

# @dec
# def greet():
#     print("Hello, there")
# # greet()

# @dec
# def sum(a,b):
#     return a+b

# # sum(1,6)


# rand(semester=6)

# class Animal:
#     def __init__(self,name):
#         self.name=name


# class Birds(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed=breed

#     def show(self):
#         print(self.name,self.breed)

# a1=Animal("cuckoo")
# a1=Birds("crow")

# a1.show()

# class Person:
#     def __init__(self):
#         self.name="ali"
#         self.age=8

#     def info(self):
#         print(f"The person's name is: {self.name}")


# # p1=Person()


# class Programmer(Person):
#     def __init__(self, language):
#         # parent class content
#         super().__init__()
#         # child class content
#         self.language=language

#     def show(self):
#         print(f"{self.name} is a programmer in {self.language} and age is {self.age}")


# p1=Programmer("c++")

# p1.show()
# p1.info()


# class Person:
#     def __init__(self):
#         self.name="Abdullah"
#         self._age=21
#         self.__university="UOS"

# class Programmer(Person):
#     pass

# class Employee:
#     pass

# p1=Person()
# p2=Programmer()
# e1=Employee()

# print(p1._Person__university)
# print(p1.name)

# print(p2._age)

# print(p2._age)
# print(e1._Person__university)

# print(e1.)


# class Student:
#     def __init__(self):
#         pass

#     @staticmethod
#     def average(a,b,c):
#         return ((a+b+c)/3)
    
# s1=Student()
# print(s1.average(1,2,3))


# class MyClass:
#     def __init__(self,name):
#         self.name=name

#     def info(self):
#         print(f"The user name is {self.name}")
    # @staticmethod
    # def get_max_value(x, y):
    #     return max(x, y)

# m1=MyClass("ali")
# m1.info()



# print(MyClass.get_max_value(20, 30))  
# print(m1.get_max_value(200,300))

# Create an instance of MyClass
# obj = MyClass(10)


# print(obj.get_max_value(20, 30))


# class Student:
#     grade="8th" # Class variable

#     def __init__(self,name,age):
#         self.name=name # Instance variables
#         self.age=age

#     def info(self):
#         print(f"The student's name is: {self.name} their age is {self.age} and the class they study in is {self.grade}")

#     @classmethod
#     def change_grade(cls,new_grade):
#         if len(new_grade)<3:
#             raise ValueError("Incorrect value for grade provided")
#         else:
#             cls.grade=new_grade
    

# s1=Student("Ali",18)


# print(s1.__dict__)
# help(s1)
# print(dir(s1))

# import os
# help(os)
# import time
# print(dir(time))

# print()
# s1.info()
# stud1=s1.__dict__



# import time
# print(dir(time))

# help(time)



# s2=Student("Aleeza",21)
# s2.change_grade("9th")
# s2.info()
# Student.grade=""

# print(f"The original class variable: {Student.grade}")

# s3=Student("Zaid",24)
# s2.info()

# print(s1.__dict__)
# print(s1.help())

# class Student:
#     def __init__(self,name):
#         self.name=name

#     def __str__(self):
#         return(f"This is __Str__ running and the student name is {self.name}")

# s1=Student("Ali")


# print(str(s1))


# num=str(12)
# print(type(num))
# print(s1.__str__)



# class User:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

#     # def info(self):
#     #     print(f"The user's name is {self.name} and id is {self.id}")

#     def __str__(self): # Overwites print
#         return(f"The user's name is {self.name} and id is {self.id}")
    
#     def __eq__(self, other):
#         return(self.name==other.name,self.id==other.id)
    
#     # def __len__(self):
#     #     return len(self.name)
    
#     # def __add__(self,other):
#     #     return User(self.name+other.name , self.id + other.id)
    

# u1=User("Abdullah",21)
# u2=User("Abdullah",21)

# print(u1==u2)

# print(f"The length of the name of the object is : {len(u1)}")

# u3=u1+u2
# print(u3)

# name="Ali"
# print(len(name))
# u3=u1+u2
# print(u3)

# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         self.name="ali"

#     def __str__(self):   # overwites print 
#         return(f"the vector is ({self.x},{self.y})")
    
#     def __add__(self,other):                            # overwrites the operation for "+" operator
#         return Vector(self.x + other.x, self.y + other.y)
                           
#     def __sub__(self,other):                            # overwrites the operation for "-" operator      
#         return(self.x - other.x, self.y - other.y)
        
#     def __mul__(self,other):                            # overwrites the operation for "*" operator
#         return(self.x * other.x, self.y * other.y)

#     def __truediv__(self,other):                        # overwrites the operation for "/" operator
#         return(self.x / other.x, self.y / other.y)
    
#     def __len__(self):
#         return (f"the name is: ",self.name)


# v1=Vector(1,2)
# v2=Vector(2,3)

# print(v1)
# print(len(v1))

# name="fahad"
# print(f"the length of name is: {len(v1)}")

# v3=v1+v2
# print(type(v3))

# print("Addition ",v1+v2)
# print("Substraction ",v1-v2)
# print("Multiplication",v1*v2)
# print("Division",v1/v2)
# print(v1+v2)



# class Animal:
#     species="general"
#     def __init__(self):
#         pass
    
#     def speak(self):
#         print("The Animal is making a sound and")


# class Dog(Animal):
#     species="Dog"
#     def __init__(self):
#         pass

#     def speak(self):
        
#         print(f"{super().species} The Dog barks")


# class Cat(Animal):
#     def __init__(self):
#         pass

#     def speak(self):
#         print("The cat meows")


# d1=Dog()
# d1.speak()

# c1=Cat()
# c1.speak()

# class Calculator:

#     def add(self,*args):
#         return sum(args)
    
# c1=Calculator()
# print(c1.add(1,2,3,4,5,6,7,8))


# def average(*args):
#     print (sum(args)/len(args))


# average(1,2,3,4)


# def greet(**kwargs):
#     # print(kwargs)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# g1=greet(name="abdullah",age=21,Teacher=True)

# dt={"name":"Abdullah"}
# print(dt)

# def intro(name,**kwargs):
#     print(f"Hello, my name is {name} \n and the other key-value passed are {kwargs.items()}")

# i=intro(age=22,siblings=2)


# class student:

#     def intro(self,name):
#         print(f"Arguments: {name}")

# s1=student()

# # print(s1)
# # s1.intro("Gaurav")


# class studenttt:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def intro(self):
#         print(f"my name is {self.name}")

# s2=studenttt("gaurav",21)
# s2.intro()

# class Person:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

#     def info(self):
#         print("This is a person")
    
# class Employee(Person):
#     def __init__(self,name,id):
#         super().__init__(name,id)

#     def info(self):
#         super().info()
#         print(f"This is an employee having name: {self.name} and id: {self.id}")

# e1=Employee("Ali",16)
# e1.info()

# class Father:
#     father_name="Alex"
#     def __init__(self):
#         pass

# class Mother:
#     mother_name="Sara"
#     def __init__(self):
#         pass

# class Son(Father,Mother):
#         def __init__(self):
#             print(f"This is inherited from {self.father_name} and {self.mother_name} and This is son class")

# # s1=Son()

# # Multilevel
# class Grandfather:
#     age=81
#     def __init__(self):
#         pass

# class Father(Grandfather):
#     age=61
#     def __init__(self):
#         pass

# class Son(Father):
#         def __init__(self):
#             print(f"This is inherited from and This is son class")

# s1=Son()
# print(Son.mro())

# # Heirarchical 
# class Grandfather:
#     age=81
#     def __init__(self):
#         pass

# class Father(Grandfather):
#     age=61
#     def __init__(self):
#         pass

# class Son(Grandfather):
#         def __init__(self):
#             print(f"This is inherited from and This is son class")

# print(Son.mro())

# class Grandfather:
#     def __init__(self):
#         pass

#     def info(self):
#          print("Im a grandfather")

# class Father:
#     def __init__(self):
#         pass

#     def info(self):
#         print("Iam a father")

# for obj in Grandfather(),Father():
#      obj.info()




    
# class Employee(Person):
#     def __init__(self,name,id):
#         super().__init__(name,id)

#     def info(self):
#         print(f"This is an employee having name: {self.name} and id: {self.id}")

# e1=Employee("Ali",16)
# e1.info()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

# class Student:
#     def __init__(self,id,name):
#         # if id<0:
#         #     raise ValueError("Id cannot be negative (constructor)")
#         self.name=name
#         self.id=id # setter is running # 0...9999

#     @property       # Initial Getter
#     def id(self):
#         print("Getter runs")
#         return self._id
    
#     @id.setter      # Setter
#     def id(self,value):
#         print("Setter runs")
#         if value<0:
#             raise ValueError("Id cannot be negative (setter)")
#         self._id=value # Execute Setter

#     @id.deleter      # Deleter
#     def id(self):
#         del self._id
#         print("id is deleted")

# s1=Student(1,"Ali")
# s1.id

    # @id.getter   # Overwrites or redefines the initial getter
    # def id(self):
    #     print("Getter runs (getter)")
    #     return self._id

    # def show(self):
    #     print(f"The student {self.name} has id: {self.id}")




# del s1.id
# s1.id

# s2=Student(2,"Anas")


# class Bank:
#     def __init__(self,name,id,balance):
#         self.name=name
#         self.id=id
#         self._balance=balance

#     @property
#     def balance(self):
#         return self._balance
    
#     @balance.setter
#     def balance(self,value):
#         if value<0:
#             raise ValueError("Wrong value assigned")
#         self._balance+=value

#     def user_info(self):
#         print(f"This user's name is: {self.name} and has id: {self.id} {self.balance}")

    
# b=Bank("ali",1,200)
# b.balance=2000
# print(b.balance)

# b.user_info()

# from abc import ABC,abstractmethod

# class Blueprint(ABC):
#     @abstractmethod
#     def area():
#         pass


# class Circle(Blueprint):
#     def area(self):
#         return

# c=Circle()    


# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __add__(self,other):
#         return (self.x-other.x , self.y-other.y)
    
# v1=Vector(5,4)
# v2=Vector(2,3)
# print(v1+v2)


# class Grandfather:
#     def intro(self):
#         print("this is grandfather")

# class Father:
#     def intro(self):
#         print("this is father")

# class Son:
#     def intro(self):
#         print("this is son")

# classes=[Grandfather(),Father(),Son()]

# for cls in classes:
#     cls.intro()

# print(len("abdullah"))

# print(len(["ali","abdullah","sara"]))

# import shutil as sh

# # sh.copy2("library.py","new_library.py")

# sh.rmtree("__pycache__")

# sum=0
# for i in range(100000):
#     sum+=i
# print(sum)

# def counting(n):
#     sum=0
#     for i in range(n):
#         yield sum
#         sum+=i

# ctr=counting(100)
# print(next(ctr))
# print(next(ctr))
# print(next(ctr))
# print(next(ctr))
# print(next(ctr))
# print(next(ctr))
# print(next(ctr))
# print(next(ctr))
# print(next(ctr))
# print(next(ctr))


# def counting():
#     for i in range(1000000):
#         if i==4:
#             break
#         print(i)
    

# count=counting()


# def large_sequence(n):
#   for i in range(n):
#     yield i

# # This doesn't create a million numbers in memory
# gen = large_sequence(1000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def read_file(filepath):
#     with open(filepath,"r") as file:
#         for line in file:
#             yield line

# path="file2.csv"

# xml_file=read_file(path)


# for i in range(25):
#         print(next(xml_file))

# Function Caching
# from sys import maxsize
# import time
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def add(a,b):   
#     time.sleep(4)
#     return a+b

# print(add(1,2))
# # print("After")
# print(add(1,2))

# # Multithreading
import time
import threading
def func(seconds):
    time.sleep(seconds)
    print(f"Sleeping for {seconds} seconds.")

# # Normal way
# time1=time.perf_counter()
# func(4)
# func(2)
# func(3)
# time2=time.perf_counter()
# print(f"Total time taken is {time2-time1}")

# # Multithreading way

time1=time.perf_counter()
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[3])
t1.start()
t1.run()
t2.start()
# t3.start()

t1.join()
t2.join()
t3.join()
time2=time.perf_counter()
print(f"Total time taken is {time2-time1}")

# Multiprocessing 

