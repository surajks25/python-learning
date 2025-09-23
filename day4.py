#dictonary in python: it means store the value and data key:value pairs
#mutable and dont allow the multiple value, same key value not valid in dictonary
dict = {
    "key" : "value",
    "name" : "suraj",
    "sub": ["maths", "sciende", "kannda"],
    "sub2": ("maths", "english","hindi"),
    "learning" : "coding" ,  
    "age": 35,
    "is_adult": True,
    "marks":  85.2
}     
print(dict)
print(type(dict))

#access the dic Value
print(dict["name"])
print(dict["sub"])

# change the value inside the dic coz dict is an mutable works
dict["name"] = "sowju"
print(dict["name"])
print(dict)

# adding new value
dict["surname"] = "ks"
print(dict)

#empty dic creation
empty_dic = {} 
empty_dic["name"] = "suri"
print(empty_dic)

#nested dictionary
dict2 = {
    "name" : "RAJ",
    "sub": {
        "maths": 50, 
        "sciende": 55,
        "kannda": 65,
    }
}     
print(dict2)
print(dict2["sub"])
print(dict2["sub"]["maths"])

#dictionary methods
#find the all keys in a dictonary
std = {
    "name" : "RAJ",
    "sub": {
        "maths": 50, 
        "sciende": 55,
        "kannda": 65,
    }
}  
print(std.keys())

#convert into list
print(list(std.keys()))

# leght findout
print(len(std))
print(len(list(std.keys())))

#values
print(std.values())
print(list(std.values()))

#items
print(std.items())
print(list(std.items()))

pairs = list(std.items())
print(pairs[0])

#return the according to value
#taking the value both are same but if code is not proper below the code working but u use getfunction the output showig like none and below the code is working
print(std["name"])  
# this one show the error print(std("name2")) missmatches

print(std.get("name"))
# if you missmatch the value like print(std.get("name2")) this is not throw a error but

#update the value
# std.update({"kannda":"30"})
val = {"kannda":"30", "name":"jan"}
std.update(val)
print(std)

#set in python

# set is  a collection of unordered iteams each element set must be unique & immutable
collection = {1,5,3,4,"xello", "aam"}
print(collection)
print(type(collection))
print(len(collection))
collection1 = set()
print(collection1)

#empty set also possible but not this type collection={}, this type collection = set()

coll = set()
coll.add(1)
coll.add(2)
coll.add(4)
coll.add("haii")
coll.add((1,2,3,4))
# coll.add([1,2,3]) this is not possiblke becuase list is a mutable value,hash value will not match 
print(coll)

coll.remove(1)
print(coll)

print(len(coll))
coll.clear()
print(len(coll))

#pop the value  random vaue will remove the set
setValues = {"apnacollege","suraj","codevita","node","react"}
print(setValues.pop() )

#union in set
set1 = {1,2,3}
set2 = {3,5,6}
print(set1.union(set2))
print(set1.intersection(set2))

#activity
dictionary = {
    "cats" : "a small animal",
    "table" : ["a peace of furniture", "list of facts and figures"]
}

print(dictionary)

#find the total classroom req each sub
setDic = {
    "python", "java", "c++", "javascript", "java",
    "python", "java", "c++", "c"
}

print(len(setDic))

#input

# value1 =int(input("enter the valu1 "))
# value2 =int(input("enter the valu2 "))
# value3 =int(input("enter the valu3 "))

# dictVal = {
#     "chem" : value1,
#     "sci" : value2,
#     "math" : value3
#     }
# print(dictVal)

# marks = {}

# value1 =int(input("enter the valu1 "))
# marks.update({"chem" : value1})
# value2 =int(input("enter the valu2 "))
# marks.update({"sc" : value2})
# value3 =int(input("enter the valu3 "))
# marks.update({"math" : value3})

# print(marks)

#we can save value same
values = {9, 9.0 } 
# it will show only 9 coz python will detech both are same thats why we save as like this string formate one one value
values = {9, "9.0" } 
# another way 
valuess = {
    "int" , 6,
    "flot" , 6.5
}
print(valuess)