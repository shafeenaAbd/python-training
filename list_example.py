list_a = {'a', 'b', 'c'}
list_b = list()

print(list_a)
print(list_b)

print(len(list_a))
print(len(list_b))


list_c = {1, 2, 3, 4, 5}
for i in list_c:
    print(i*2)

# LIST COMPREHENSION
list_d = [i*i for i in list_c]
print(list_d)

print(list_a.extend(list_c))
# LIST OPERATIONS
empty_list = list()
empty_list.append('a')
empty_list.append('b')  # append -data ditambah
print(empty_list)

