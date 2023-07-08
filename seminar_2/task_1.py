a: int = 10
b: str = 'New string'
c: bool = False

print(type(a))
print(type(b))
print(type(c))

if type(b) == str:
    print("OK")
else:
    print("NOT A STRING")

isinstance(b, str)
