#loops
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
i = 1
while i <= 20:
    if(i%2 != 0):
        i += 1
        continue #skip
    print(i)
    i+=1