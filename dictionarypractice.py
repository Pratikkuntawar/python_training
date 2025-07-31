# dictionary in python is used to store key value pairs and key must be unique in dictionary
dict={
    "name":"pratik",
    "age":25,
    "College":"SSGMCE"
}
print(dict.get("name"))
print(dict["name"])
dict["name"]="Ritik"
print(dict)
#dict.clear()#remove dictionary
print(dict.pop("name"))
print(dict)

for key in dict.keys():# to print keys of dictionary
    print(key)

for value in dict.values():# to print value of key
    print(value)

for key,value in dict.items():#to print key value pair
    print(key,value)

dict["name"]="Pratik"#add key vaue pair in dictionary
print(dict)
dict.popitem()
dict.pop("age")
print(dict)