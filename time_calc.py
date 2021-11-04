x=int(input("Enter you seconds: "))
a=x//86400
b=x%86400
c=b//3600
d=b%3600
e=d//60
f=d%60
print (a, "days", c, "hours", e, "minutes", f, "seconds")
