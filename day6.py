#function is a block statement that perform a specific task
# def func_name(param1, param2):
#     return val
# func_name(arg1,arg2)

# def cal(a, b): 
#     sum = a +b
#     print(sum)
#     return(sum)
# cal(1,2)
# cal(5,8)
# cal(7,4)

# def func (a,b): parameters
#     return a+b
# sum = func(2,5) function call : arguments
# print(sum)

# def printHello():
#     print("hellofunction")
# printHello()
# printHello()
# printHello()

#average of 3 numbers
# def average(a,b,c):
#     sum = a+b+c
#     print("printed val",sum/3 )
#     return(sum/3)

# val = average(1,2,3)
# print("return val" ,val)

# there are 2 type of function 1 is 
# builtin func > print() len() type() range()
# userdefiend func we made func like above code

# print("suraj","kulal") #automaticaly space came coz of inbuilt print defined

# print("suraj")
# print("kulal") #not came in one line so below code made that add end it will came same line

# print("suraj",end="")
# print("kulal")

#userfunction
# def cal(a=1,b=9): # this is default value set inside the function
#     print(a*b)
#     return a*b
# cal(5,5)

#practise q
#print the length of list
# list = [1,2,3,4,5,6,7,8,9]
# print(len(list))

# num = [1,2,3,4,5,6,7,8,9]
# cities = ["raj", "koj", "kar", "hio"]
# def func(list):
#     print(len(list))
# func(num)
# func(cities)

# num = [1,2,3,4,5,6,7,8,9]
# cities = ["raj", "koj", "kar", "hio"]
# def func(x):
#     print(len(x))
# func(num)
# func(cities)

# tuple = (1,2,3,4,5,6)
# def fuc(tuple):            insted of tuple place use any letter it will detect work perfect no problem
#     print(len(tuple))
# fuc(tuple)


# text = "haii my name is suraj"
# raplace = text.replace(" ", "")
# print(raplace)

    
# text = "haii my name is suraj"

# for i in range(len(text)):
#     if text[i] == " ":
#         replace = text[i].replace(" ", "_")
#         print(replace, end="")
#     else:
#         print(text[i], end="")

#     or

#     for i in range(len(text)):
#     if text[i] == " ":
#         new_text += "_"
#     else:
#         new_text += text[i]

# text = "haii my name is suraj"
# for i in range(0, len(text), 1):
#     if text[i] == " ":
#         text = text.replace(" ", "_")
# print(text)

#factorail find out my logic
# n=5
# fact  = 1
# for i in range(1, n+1):
#     # fact = i * fact
#     #  or 
#     fact *= i
# print("factorial value of :" ,n ,"=",fact)


# same factorail inside the function
# def func(n):
#     fact  = 1
#     for i in range(1, n+1):
#     # fact = i * fact
#     #  or 
#         fact *= i
#     print("factorial value of :" ,n ,"=",fact)
# func(5)

# find the usd to inr
# def usd_find(usd):
#     print(usd, "USD IS EQUAL TO ", usd*88.72, "INR" )
# usd_find(4)

#check number is odd or even using function
# def oddEven(n):
#     if n%2 == 0:
#         print("even")
#     else:
#         print("odd")

# oddEven(645454)

                                                            #recursion
#recursion is a function it calling itself rapidley means one function inside calling same function at a sametime
# def recu(n):
#     if n == 0: 
#         #  if n == 0: this is base case like for loop you mention start end plus right so same where the loop will stop this will deside this is called basecase act like where to stop
#         return
#     print(n)
#     recu(n-1)
#     print("end")
# recu(5)
#also called as calstack like stack wise work if you gave number like 5 first 5store in astck then 5 above 4 then 4 above 321 etc,,,

# def fun(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fun(n-1)*n #first done the fun(n-1) done all no next check n==0 or n ==1 return 1 then start 1*1,2*2,3*2,
# print(fun(4))

#write the recurstion function cal sum of  the first natural numbers
# def fun(n):
#     if(n==0):
#         return
#     print(n)
#     fun(n-1)
# fun(5)

# print the list values inside the recursion
# def fuction_rec(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx], end="")
#     fuction_rec(list, idx+1)
    
# list = ["a","b","c","d","e","f","g"]

# fuction_rec(list)

# def fuction_rec(list, idx=7):
#     if(idx == len(list)):
#         return 1
#     print(list[idx], end="")
#     fuction_rec(list, idx+1)
    
# list = ["a","b","c","d","e","f","g"]

# v = fuction_rec(list)
# print(v)

# def show_numbers():
#     for i in range(5):
#         if i == 3:
#             return  # stops the whole function
#         print(i)
#     print("Loop finished")  # this will NOT run

# show_numbers()
