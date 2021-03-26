def generate_dict(*args, **kwargs):
    return kwargs

print(generate_dict(first_key='a', second_key='b', last_key='z'))
print(generate_dict(a='a', b='b', c='z'))
print(generate_dict(a='Primer elemento', b='Segundo elemento', c='Tercer elemento'))
