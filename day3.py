#list
# mark1 = 22.5
# mark2 = 88.5

# marks = [55.2, 88.2, 45.1]
# print(marks)
# print(type(marks))

# marks[2] = 55.5
# print(marks)

#multiple data stored in a list java and c also same procedure in array but not a python is list
# student = ["karan", 95.4, 17, "delhi"]
# print(type(student))
# print(len(student))
# print(type(student[1]))


# list are basically mmutable(change the value)
# print((student[1]))
# student[1] = 58.9
# print((student[1]))

# but strings are immutable(cant change the value) but in list is posible itschange in usual way we cant chnge
# print((student[0]))
# student[0] = "raj"
# print((student[0]))

# str = "hello"               this is immutable
# str[0] = "y"
# print(str)

#slicing in list

# marks =[1, 2, 3, 4, 5]
# print(marks[1:3])
# print(marks[-3:-1])




#list methods

# list = [2, 1, 3]
# list.append(4)
# print(list)

#ascending order
# list = [2, 1, 3]
# list.sort()
# print(list)

#dicending order
# list = [2, 1, 3]
# list.sort(reverse=True)
# print(list)

#reverse
# list1 = [2, 5, 8, 9]
# list1.reverse()
# print(list1)

#string sort
# list1 = ["haii", "xanoj", "abb"]
# list1.sort()
# print(list1)

#inset 
#same like append but it was use for particular index to ADD the value
# list1 = [2, 5, 8, 9]
# list1.insert(2, 1)
# print(list1)

# list1 = ["haii", "xanoj", "abb"]
# list1.insert(1, "baii")   # insert "baii" at index 1
# print(list1)

#remove   remove the particaular one value 
# list1 = [2, 5, 8, 9, 2]
# list1.remove(2)
# print(list1)

# pop the value remove element in idx
# list1 = [2, 5, 8, 9, 2]
# list1.pop(2)
# print(list1)


# tupples a built in data type create immutable sequnce of values (cant change value inside the tuple value)
# tup = (1,2,3,5,6,8,1,1,1)
# print(tup)
# print(tup[1])
# print(tup[2])
# print(tup.index(2))
# print(tup.count(1)) 


# task if we take the input from user starting its always string

# movie1 = input("enter your 1 movie: ")
# movie2 = input("enter your 1 movie: ")
# movie3 = input("enter your 1 movie: ")
# list = [movie1, movie2, movie3]
# print(list)

# another method

# movies = [] 
# movie1 =input("enter your 1 movie: ")
# movie2 =input("enter your 1 movie: ")
# movie3 =input("enter your 1 movie: ")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# another method

# movies = []

# movies.append(input("enter the 1movie name : "))
# movies.append(input("enter the 2movie name : "))
# movies.append(input("enter the 3movie name : "))

# print(movies)



# list1 = ["m", "a", "a", "m", "p"]

# copy_list1 = list1.copy()   #why we make the copy coz list is immutable so once we reverse the main text also revelse not copare properly so we nned to copy nad check
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("NOT palindrome")




word = "mom"
if word == word[::-1]:
    print(f"{word} is a palindrome ")
else:
    print(f"{word} is NOT a palindrome ")
