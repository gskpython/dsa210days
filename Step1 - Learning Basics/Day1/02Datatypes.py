# Demonstrates the data types
i = 10
f1, f2, f3 = 6.3, 0.0, -1.7e-6
b1, b2 = True, False
s = 'Hello'
b = b"Hello\xfe\776"

print(i)
print(f1,f2,f3)
print(b1,b2)
print(s)
print(b)

print(type(i))
print(type(f1), type(f2), type(f3))
print(type(b1))
print(type(s))
print(type(b))


c1 = 3 + 5j
c2 = 5j
c3 = -5j

print(c1)
print(c2)
print(c3)

print(type(c1))
print(type(c2))
print(type(c3))

# Lets cast these
if1 = float(i)
istr = str(i)
f1i = int(f1)
f2i = int(f2)
f3i = int(f3)

print(type(if1) , if1)
print(type(f1i), f1i, f2i, f3i)
print(type(b1))
print(type(s), istr)
print(type(b))




