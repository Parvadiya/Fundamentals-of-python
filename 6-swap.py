a=int(input("Enter a number :"))
b=int(input("Enter a number :"))

# swap two number with temp variable
print(a,b)

c=a
a=b
b=c

print(a,b)

# swap two number without temp variable
print(a,b)

a,b=b,a

print(a,b)