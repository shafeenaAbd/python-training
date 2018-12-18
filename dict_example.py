dict_a = dict()  # if dict_a -> False

# DICT OPERATIONS
dict_a['hello'] = 'world'
dict_a['shafeena'] = 'sha'

print(dict_a)
print(dict_a['hello'])
# print(dict_a['error'])

print(dict_a.get('error', 'Not Found.'))

