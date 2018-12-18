# tuple fix list
tuple_a = ('a', 'a', 'b', 'c', 'a')
tuple_b = ()

print(bool(tuple_a))
print(bool(tuple_b))

tuple_c = (1, 2, 3)
tuple_d = 1,

print(tuple_c)
print(tuple_d)

# TUPLE OPERATIONS
print(tuple_a.count('g'))
print(tuple_c.index(1))  # get position of '1'
print(tuple_a[0])
