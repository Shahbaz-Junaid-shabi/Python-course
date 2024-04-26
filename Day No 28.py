# String formatting

intro = "Hi am {0} and I am from {1}"
name = "shahbaz Junaid"
province = "GB"

print(intro.format(name,province))

# first we use the string format but nowsaday we use the f- string 

# f-string 

print(f"Hi am {name} and I am from {province}")
print(f"{2*2}")
print(type(f"{2*2}"))

# If you want to print exists than 
print(f"Hi am {{name}} and I am from {{province}}")
