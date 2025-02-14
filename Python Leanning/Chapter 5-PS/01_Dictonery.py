
## The dictionary is an unordered set of comma-separated key:value pairs, within {}, 
# with the requirement that within a dictionary, no two keys can be the same.
# 
#<dictionary-name> = {<key>: value, <key>: value ...}

''' Propert of dictonery
-- unordered, mutable, indexed, cannot contain duplicate keys'''

# Dictonery is mutable
# We  can use Int & String
marks = {
    "marry":100,
    "bum":56,
    "rohan":25}
print(marks,type(marks))

# Method 1 to print Itmes.
marks = {
    "marry":100,
    "bum":56,
    "rohan":25
}
print(marks.items())
## In  left side it is keys ex-Harry & Right side is values ex-100"
# Method 2 to print list.
marks = {
    "marry":100,
    "bum":56,
    "rohan":25
}
print(marks.keys())


# Update Dictonery
marks = {
    "marry":100,
    "bum":56,
    "rohan":25}
marks.update({"marry": 85})
# print(marks)
###############################################
print(marks.get("marry2"))   ## prints None
print(marks["harry2"])    # Returns an error

# adding one entry in dictionery
marks = {
    "marry":100,
    "bum":56,
    "rohan":25}
marks.update({"marry": 85, "Amit": 101})
print(marks)

marks = {
    "marry":100,
    "bum":56,
    "rohan":25}
#print(marks.get("marry"))
print(marks["marry"])

