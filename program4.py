a=int(input("enter first number:"))
b=int(input("enter second number:"))

add = a+b

sub = a-b
mul = a*b

if b!=0:
  div = a/b
else:
  div = "undifined (division by zero)"

print("addition =",a+b)
print("subtraction=",a-b)
print("multiplication =",a*b)
print("division =",a/b)
