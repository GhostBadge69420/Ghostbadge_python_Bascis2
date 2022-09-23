customer = {
    "name": "Canniest Badger",
    "age": 2000,
    "is_verified": True
}
print(customer["name"])
print(customer["age"])

################################################

customer = {
    "name":"Canniest Badger",
    "age":2000,
    "is_verified": True
}
print(customer.get("name"))
print(customer.get("age"))

###############################################

customer = {
    "name": "Canniest Badger",
    "age": 2000,
    "is_verified": True
}
print(customer.get("birthdate", "Dec 16 1991"))

################################################

customer = {
    "name": "Canniest Badger",
    "age": 2000,
    "is_verified": True
}
customer["name"] = "Canniest Badger"
print(customer["name"])

##################################################

customer = {
    "name": "Canniest Badger",
    "age": 2000,
    "is_verified": True
}
customer["birthdate"] = "Dec 16 1991"
print(customer["birthdate"])

##################################################

phone = input("phone:")
digits_mapping = {
    "6":"six",
    "9":"nine",
    "6":"six",
    "9":"nine",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + ""
print(output)