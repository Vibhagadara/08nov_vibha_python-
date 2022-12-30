#swap with using temp.

a=10
b=20

print("before swap a=",a)
print("before swap b=",b)

temp=a
a=b
b=temp

print("after swap a=",a)
print("after swap b=",b)

# -------------------------------------

#swap without using temp.

a,b=b,a

print("after swap a=",a)
print("after swap b=",b)