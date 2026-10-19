# Variables

# name  = "usman";
# Class = 10;
# height = 10.5 ;
# student = True;
# print("My Name is", name)
# print("My Class is", Class)
# print("My Height is", height)
# print("I am a student", student)

# if/elif/else

# age = 17
# if age > 18:
#      print("tum vote kr skty ho")
# elif age == 18:
#       print("tum bilkul vote kr skty ho")
# else:
#       print("tum vote nhi kr skty")

# (exp 02) Marks = 45 hai. 50 se kam hai toh "Fail" print ho. Kaunsa code sahi hai?

# Marks = 45
# if Marks < 50:
#     print("tum fail ho")
# else:
#     print("tum pass ho")
    

# Loops (for & while)

# 1 se 5 tak print karo
# for a in range(1 , 6):
#     print("number:", a)

# List ke har element pe kaam karo

# Fruits = ["usman" , "faiza" , "danish"]
# for s in Fruits:
#     print("Fruits:" , s) 

# While Loop

# count = 1
# while count <= 7:
#     print("count is :" ,count)
#     count = count + 1

# Function

# Return/Print Difference
# def double_print(x):
#     return(x * 2)
# result = double_print(5)
# print(result)
# print(result*3)
# Agar return nahi likha toh function None return karta hai. None ka matlab hai "kuch nahi".

# def double_print(x):
#     print(x * 2)
# result = double_print(5)
# print(result)
# print(result*3) Error show kry ga 

# Return k bad function khatm hojata hy 

# def check(n):
#     if n > 0:
#         return"nikal gya hy"
#     return"nhi nikla"
# print(check(5))
# print(check(-1))

# *args aur **kwargs / *args – kitne bhi arguments pass karo
# def args(*number):
#     return sum(number)
# args(1,2,3)

# Default Parameters
# def salam (name , time="subha"):
#     print(f"{time} bakhair, {name}")
# salam("usman")
# salam("Faiza","dupaher")

# Rule: default value wale parameters aakhir mein aate hain.
# def f(a=1, b) → GALAT
# def f(a, b=1) → SAHI

# def salam (time="subha" ,name):
#     print(f"{time} bakhair, {name}")
# salam("usman")
# salam("Faiza","dupaher")  Shows Error

# Keyword Arguments
# def address (name , age , city="muzaffargarh"):
#     print(f"My name is {name}, My Age is {age} and My City is {city}")
# address("usman",23) Normal way
# address(age="24",name="danish") Keywords argument

# *args – Kitne Bhi Arguments
# def subject_marks(subject , *marks):
#     avg = sum (marks)/len(marks)
#     print(f"{subject} average: {avg:.1f}")
# subject_marks("Math", 22,44,55)

# Lambda Function (lambda parameters: expression)
# normal function
# def x(a,b):
#     print(a+b)
# x(2,3)

# Now lambda Function
# double = lambda x: x * 6
# print(double(4))

# Lambda ka asli use – Sorting mein (Interview mein puchha jaata hai!)

# student = [
#     {
#         "name":"usman" , "Marks":99 
#     },
#     {
#         "name":"danish" , "Marks":98 
#     }
#     ,
#     {
#         "name":"faiza" , "Marks":97 
#     }
# ]
# print(student)
# student.sort(key=lambda sorting:sorting["Marks"])

# print(student)


# Exercise Function
# 1 = Ek function banao jiska naam ho greet. Yeh ek naam lega aur 'Salam, [naam]! Kaisa haal hai?' print karega.

# def greet(name):
#     print(f"salam {name} kya haal hy?")
# greet("ali")
# greet("usman")

# 2 = Function banao check_number(n) jo bataaye ke number Even hai ya Odd. Function result return kare, print nahi.

# def check_number(n):
#     if n % 2 == 0:
#         return("even")
#     else:
#         return("odd")
# print(check_number(2))

# 3 = Function banao calculator(a, b, operation) jo teen parameters le — do numbers aur operation (+, -, *, /). Sahi result return kare. Division mein b=0 ka bhi khayal rakho!

# def calculator (a,b,operator):
#     if operator == "+":
#         return a+b
#     elif operator =="-":
#         return a-b
#     elif operator == "*":
#         return a*b
#     elif operator == "/":
#         return a/b
#     #     if b == 0:
#     #         return "error"
#     #     return a/b
#     # else:
#     #     return "unknown operator"
# print(calculator(1,1,"/"))


# 4 = Function banao find_max(numbers) jo ek numbers ki list le aur sabse bada number return kare. Built-in max() use mat karo — khud loop lagao!

# def find_max(numbers):
#     max = numbers[0]
#     for num in numbers:
#         if num > max :
#             max = num
#     return max
# List=[2,4,9]
# print(find_max(List))


# List Methods
# Method ek built-in function hai jo list pe directly kaam karta hai. list.method() – dot lagao aur method ka naam lo.

# List = ["usman","faiza","danish"]

# Add krna

# List.append("faizaa") #end mn add krta hy 
# List.insert(2,"ali") #insert expected 2 arguments 
# List.extend(["ali",2]) #dosri list add kr dyta hy 

# Hatana

# List.remove("faiza") #value se hatao (pehla match)
# List.pop() #Alkhari hatao 
# List.pop(1) #Index wala hatao
# List.clear() #List clear kr do.. khali kr do 

# Dhundna aur Janna

# print(List.index("faiza"))# kis index pr hy
# print(List.count("usman")) # kitni bar hy 
# print("usman" in List) #List mn wo hy k nhi
# print(len(List)) # lenght kitni hy 

# Sort aur Organize

# num = [2,1,4,5,7,3,2,0]

# num.sort() # number sort hogyn gy 0 sy end tk 
# num.sort(reverse=True) # reverse mn sort kr dy ga list ko
# num.reverse() #list ko ulti kr do 
# print(sorted(num))  #new list bna kr dy ga or sort b kr dy ga porani wasy he rhy gi
# print(min(num)) #sub sy chota number dy ga list ka 
# print(max(num)) #sub sy bara number dy ga list ka
# print(sum(num)) # list k  numbers ko sum kr k dy ga

# List comprehension – Python ka superpower

# # Normal loop
# square = []
# for x in range(1,10):
#     square.append(x**2)
# print(square)

# # Comprehension Loop
# Comp_loop = [x**2 for x in range(1,10)]
# print(Comp_loop)

# 50 se upar marks filter karo
# Total_Marks = [23,40,88,99,67,89]
# Marks = [n for n in Total_Marks if n > 50]
# print(Marks)


# Dictionary 
# Dictionary mein data key-value pairs mein hota hai.

user = {"name":"Usman" , "Age":23 , "Blood_Group":"B+"}
# print(user["name"]) # not safe Method
# print(user.get('name')) # safe method
# print(user.get('Age'))
# print(user.get('Blood_Group'))

# Exp Why not safe 
# print(user["phone"])
# print(user.get("phone"))

# Naya key add karo
# user["City"] = "Muzaffargarh"
# print(user.items())

# Value update karo
# user["Age"] = 24
# print(user.items())

# Multiple updates ek saath
# user.update({"Phone":"03011933637" , "Address":"Purni Chungi No 2"})
# print(user.items())

# List of Dictionaries
# Result  = [
#     {
#         "name" : "Usman" , "Class" : "10th" , "Marks" : 100
#     },
#     {
#         "name" : "Danish" , "Class" : "10th" , "Marks" : 250
#     },
#     {
#         "name" : "Arslan" , "Class" : "10th" , "Marks" : 99
#     }
# ]
# print(Result[0])
# print(Result[1]["name"])
# print(Result[2]["Marks"])

# Loop se sab print karo
# for Loop in Result:
    # print(f"{Loop['name']} : {Loop['Class']} : {Loop['Marks']}")

# Sirf pass students (marks >= 50)
# Pass_Students_List = [ Pass_Students for Pass_Students in Result if Pass_Students["Marks"] >= 100 ]
# print(Pass_Students_List)

# Tuple & Set – chhote lekin important
# point = (1,2,3)
# print(point[0])
# point[0] = 24
# print(point[0])

# Set – sirf unique values
# Set mein duplicate values nahi hoti. Automatically remove ho jaati hain. Order guarantee nahi.

# Set = {1,2,3,4,5,2,3,4}
# print(Set)

# Set = [1,2,3,4,5,2,3,4]
# print(Set)
# Set_01 = list(set(Set))
# print(Set_01)

# Interview 2 lists ko combine karna – 3 tarike
# a = [1,2]; b = [3,4]
# print(a+b)
# a.extend(b)
# print(a)
# print([*a,*b])

# Exercise 1

# fruits = ['mango','apple','banana','grape'] # last item print karo, phir 'strawberry' add karo, phir 'apple' hatao.
# print(fruits[3])
# fruits.append("strawberry")
# print(fruits)
# fruits.remove("apple")
# print(fruits)

# Exercise 2

# List = [1,2,3,4,5,6,7,8,9,10] # ki list mein se sirf even numbers ki nai list banao – list comprehension use karo.
# list_comprehension = [m for m in List if m%2 == 0]
# print(List)
# print(list_comprehension)

# Exercise 3

# Ek student dict banao naam, marks, sheher ke saath. Phir marks update karo, naya 'grade' key add karo (A/B/C marks ke hisaab se).
# student = { "name":"Usman" , "marks" : 99 , "sheher" : "Muzaffargarh" }
# student["marks"] = 100
# if student["marks"] == 100:
#     student["grade"] = "A+"
# elif student["marks"] >= 90:
#     student["grade"] = "B+"
# else:
#     student["grade"] = "C"

   
# print(student)

# Exercise 4

# 3 students ki list of dicts banao. Phir loop se sirf woh students print karo jinke marks 80 se zyada hain.
# students = [
#     { "name":"Usman" , "marks" : 99 , "sheher" : "Muzaffargarh" },
#     { "name":"Danish" , "marks" : 100 , "sheher" : "Muzaffargarh" },
#     { "name":"Faiza" , "marks" : 55 , "sheher" : "Burawala" }
# ]
# s = [marks for marks in students if marks["marks"] > 80]
# print(s)

# try/except ke saath – safe program
# try:
    # Age = int(input("Umer kya hy ...?"))
    # print(f"Tum Vote kr skty ho kyn k tumhari Age {Age} hy")
# except:
#     print("Numbers mn Age Likho")

# Specific exception pakadna
# try:
#     Age = int(input("Umer kya hy ...?"))
#     print(f"Tum Vote kr skty ho kyn k tumhari Age {Age} hy")
# except ValueError:
#     print("Sirf Number Allow hy")

# Type Error
# try:
#     a = "ALi" + 2
#     print(a)
# except TypeError:
#     print("Number Add kro bss")

# else aur finally
# else block tab chalta hai jab try mein koi error nahi aai.
# finally hamesha run hota hai – chahe error aaye ya na aaye.

# try:
#     Name = input("Apna Name Likho = ")
# except:
#     print("Only Alphabets allow hy ")
# else:
#     print(f"wow tumhara name to bhut acha hy {Name}")
# finally:
#     print("ya code hamaysha run hoga ")

# Exception object
# except ErrorType as e likhne se hum error ki detail pakad sakte hain. e mein exact message hota hai jo Python ne bheja.

# try:
#     converter = int("abc")
# except ValueError as e:
#     print("dhyko kon aya hy .... error aya hy" , e)

# Bare projects mein except Exception se bachna chahiye – specific exceptions pakadna better hai. Warna bugs chhup jaate hain.

# Raise Error
# Kabhi kabhi hum khud error uthana chahte hain – jab koi galat value aaye jo technically crash nahi karti lekin logic galat hai.

# def Age (age):
#     if age < 0:
#         raise ValueError ("Umer 0 sy kam nhi ho sakti")
#     if age >=18:
#         print("tum vote dy skty ho")
#     if age > 90:
#         raise ValueError ("itni kyn jee rhy ho")
# Age(-5)
# print("dhykty hn ya chly ga ya nhi") #raise error k bad ka code nhi chly ga 

# raise + except – combine karna
# def divide(a,b):
#     if b==0:
#         raise ZeroDivisionError ("Zero sy divide nhi kr skty")
#     return a/b
# # a=divide(0,2)
# # print(a)
# try:
#     ans = divide(10/0)
# except ZeroDivisionError as e:
#     print(f"error ayn hn ({e})")
# ZeroDivisionError as e:
    
# Custom exceptions – apni khud ki errors
# Python ke built-in errors kaafi hain beginners ke liye. Lekin bade projects mein apni khud ki error classes banate hain – taaki code aur readable ho.
# Yeh OOP ka concept hai – baad mein detail mein padhenge, abhi basic samjho. 

# class AgeError(Exception):
#     pass

# def Voting(age):
#     if age >= 18:
#         print("tum vote kr skty ho")
#     if age < 18 :
#         print("tum vpte nhi kr skty")
#     if age <= 0:
#         raise AgeError("0 sy kam age nhi hoti tw pagal hy kya bay")
#         return age
# # Age = Voting(23)
# # print(Age)
# try:
#     New_Age = Voting(-5)
# except AgeError as e:
#     print(f"pagal hy kya bay loray  ({e})")

# with statement – better file handling
# File handling ka sabse safe tarika with hai – automatically band ho jaati hai, finally likhne ki zaroorat nahi.

# f = open("test.txt")
# data = f.read()
# print(data)
# print(f.closed)
# f.close() # bhool gaye? resource leak!
# print(f.closed)

# with open("test.txt") as file:
#     data = file.read() # block khatam → file auto close ho gayi
#     print(file.closed)
# print(data)
# print(file.closed)

# try:
#     with open("test.txts") as file:
#         data = file.read() # block khatam → file auto close ho gayi
# except FileNotFoundError as e:
#     print(e)


# Hamza
# variable and its types, string, float, integer and also boolean. string (any name, statemnet, any sentence eytc), flaot (any  number with decimal point like 12.5 etc), Integer (any number without decimal point like 12 etc), boolean (it depend on situation like true and false. for instance i am playing if i am playing its true on the other hand, if i am styding then it is false. 
# name = False
# print("name")
# name = "abdullah"
# print(name) 
# print(type(name))
# age = 17.7
# print(age)
# print(type(age))
# size = 78
# print(size)
# print(type(size))
# names = False
# print(names)
# print(type(names))
# age = 30
# print(age>=25)