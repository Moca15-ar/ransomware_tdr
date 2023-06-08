# Python3 code to demonstrate working of 
# Remove None value types in dictionaries list
# Using filter() + lambda + list comprehension
# initializing list
test_list = [{'gfg' : 4, 'is' : '', 'best' : []}, {'I' : {}, 'like' : 5, 'gfg' : 0}]

# printing original list
print("The original list is : " + str(test_list))

# Remove None value types in dictionaries list
# Using filter() + lambda + list comprehension
res = list(filter(None, ({key : val for key, val in sub.items() if val} for sub in test_list)))

# printing result 
print("The filtered list : " + str(res))