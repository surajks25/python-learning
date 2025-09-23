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