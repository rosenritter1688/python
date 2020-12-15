
## Dictionary Items
#* Dictionary items are unordered, changeable, and does not allow duplicates.
#* Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

## {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# Example
# Duplicate values will overwrite existing values: 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
