
testu = [1, 2, 3, 4]
bla = [num for num in testu if num > 2]
print(bla)


foo = [
    { 'hello': 'world' },
    { 'hello': 'bar' },
]
baz = [item['hello'] for item in foo]
print(baz)