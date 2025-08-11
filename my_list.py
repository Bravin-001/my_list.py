# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert 15 at the second positin
my_list.insert(1, 15)

# Extend with anaother list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop(-1)

# Sort in ascending order
my_list.sort

#Find and print index of value 30
index_30 =my_list.index(30)
print("The index of 30 is:", index_30)

print("Final list:", my_list)