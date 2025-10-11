                                                                #while loops
# count = 1
# while count <= 5:
#     print("hello")
#     count += 1 
# print(count)

# i = 1
# while i <= 5:
#     print("apnacollege", i)
#     i+=1
    
# print the number 1 to 10
# i = 1
# while(i <= 10):
#     print(i)
#     i+=1
# print("loop was ended")

# print the number 10 to 1
# i = 10
# while(i >= 1):
#     print(i)
#     i-=1
# print("loop was ended")

#practise questions

# print multiplication table of a number n
# n = int(input("enter your multiplication number : "))
# i = 1
# while i <= 10:
#     print(n * i)
#     i+=1
# print("ender mul")

# list under loop
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# while index < len(nums):
#     print(nums[index])
#     index +=1

# heros = ["iron man","raj","aman","zung"]
# index = 0
# while index < len(heros):
#     print(heros[index])
#     index += 1 

#serch for a x in this tupple
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36 
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#         print("found," ,i)
#         break
#     else:
#         print("loop lood")
#     i += 1
# print("end loop")
    
#break
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# else:
#     print("loop end")

#continue
# i = 1
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue #skip
#     print(i)
#     i+=1

#with the use of continue check the remove the even number in a tuple
# i = 1
# while i <= 20:
#     if(i%2 == 0):
#         i += 1
#         continue #skip
#     print(i)
#     i+=1

#odd remove
# i = 1
# while i <= 20:
#     if(i%2 != 0):
#         i += 1
#         continue #skip
#     print(i)
#     i+=1

                                                                 # forloop
# nums = [1,2,3,4,5]
# for val in nums:
#     print(val)

# nums = ["potato", "mango", "orange", "banana"]
# print(nums.index("potato"))

#list
# nums = ["potato", "mango", "orange", "banana"]
# for val in nums:
#     print(val)  

#tuples also print using the foloop
# tuple = (1,2,3,4,5,6,7)  
# for e in tuple:
#     print(e)

# text = "apnacollege "  
# for char in text:
#     if char == "o":
#         print("o found")
#         break
#     print(char)
  
# print("end")

#task found the x value
# numbers = [1,2,3,4,5,6,7,8,9,5,6]
# x = 6
# idx = 0
# for value in numbers:
#     if value == x:
#         print("number found at idx ", idx)
#         # break
#     idx += 1

                                                # range()
# range function return of number starting from 0 by default, and increment by 1 by default and stops before a aprecifies number
# range(start, stop, StopIteration)

# seq = range(5)
# for i in seq:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(2, 10, 3): #range(start, stop, step)
#     print(i)

#practise

#print the squre root of number using the for loop
# for i in range(1, 11, 1):
#     print(i*i)

# linear search
# tuple = (1,16,33,25,80)
# f = 25
# for i in  range(0, len(tuple), 1):
#     if f == tuple[i]:
#         print("found", i)
#         break
# else:
#     print("not found")

# list = "hello"
# for x in list:           
#     print(x)

                                                # palindrome number search chat gpt
# t = (1, 2, 3, 3, 2, 1)

# if t == t[::-1]:
#     print("palindrome integer")
# else:
#     print("not palindrome")

# t = (1, 2, 3, 3, 2, 1)
# is_palindrome = True

# for i in range(len(t)):
#     if t[i] != t[len(t) - 1 - i]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("palindrome integer")
# else:
#     print("not palindrome")

 # palindrome string search chat gpt
# text = "level"

# if text == text[::-1]:
#     print("palindrome string")
# else:
#     print("not palindrome")

#explanation
# Now in text[::-1]

# start → not given → means start from end

# stop → not given → means go till start

# step = -1 → move backward one step at a time

# # manually
# text = "madam"
# is_palindrome = True

# for i in range(len(text)):
#     if text[i] != text[len(text) - 1 - i]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("palindrome string")
# else:
#     print("not palindrome")

# text = "RaceCar"
# text = text.lower() # sometime text is not a proper way we need to coert into lower case first


# learn things basic first
# string = "levelup"

# for i in range(len(string)):
#     print(i, "→", string[len(string) - 1 - i])

#pass statement pass is null statement that does nothng it is used as placeholder for future code
# for i in range(5):
#     pass
# print("skipped using the pass keyword")

#print the sum of all number in n value

# sum = 0
# for i in range(0, 10, 1):
#     sum = i + sum
# print(sum)

# or

# n=5
# sum = 0
# for i in range(1, n+1): #range(start, stop)
#     sum += i
# print(sum)

# facotrial findout
# mul = 1
# for i in range(1,6,1):
#     mul = mul * i

# print(mul)

# or

# n = 5
# mul = 1  # start with 1
# for i in range(1, n+1):  # multiply 1*2*3*4*5
#     mul = mul * i

# print(mul)
