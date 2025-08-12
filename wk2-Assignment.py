my_list = []
print(f"Empty list created: {my_list}")

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending elements: {my_list}")

my_list.insert(1, 15)
print(f"After inserting 15 at the second position: {my_list}")

my_list.extend([50, 60, 70])
print(f"After extending with [50, 60, 70]: {my_list}")

my_list.pop()
print(f"After removing the last element: {my_list}")

my_list.sort()
print(f"After sorting in ascending order: {my_list}")

index_of_30 = my_list.index(30)
print(f"The index of 30 in the list is: {index_of_30}")