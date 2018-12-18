# function definition
# def function(a,b,c)
# <body or function >
# return <return_value>


def add_num(a, b):
    total = a+b
    return total


def total(*args, **kwargs):
    ...


nama = 'JERRY'
umur = 20

total(nama=nama, umur=umur)
total(1, 2, 3, 4, 5)

add_a = add(1, 2)
add_b = add('hello', 'world')
add_c = add(1.0, 3)
# add_d = add(3, 'hello')

print(add_a, add_b, add_c)
# print(add_d)
