#Selected components
first = input("First numbers (numbers or x): ") 
second = input("Operation (+ - * :): ") 
tried = input("Second numbers (numbers or x): ") 
five = input("What is equal to:") 
#Converting an equation to the format of numbers and signs from the text
try: 
    first = float(first) 
except ValueError: 
    pass 
try: 
    tried = float(tried) 
except ValueError: 
    pass 
five = float(five) 
#Math operation
if second == "+": 
    if first == "x": 
        reshenie = five - tried 
    elif tried == "x": 
        reshenie = five - first 
elif second == "-": 
    if first == "x": 
        reshenie = five + tried 
    elif tried == "x": 
        reshenie = five - first 
elif second == "*": 
    if first == "x": 
        reshenie = five / tried 
    elif tried == "x": 
        reshenie = five / first 
elif second == ":": 
    if first == "x": 
        reshenie = five * tried 
    elif tried == "x": 
        reshenie = five / first 
#Escaping the second part of the equation
if first == "x": 
        if second == "+":
            firststr = f"{first} {second} {tried} = {five}" 
            secondstr = f"x = {five} - {tried}"
            fourstr = f"{reshenie} {second} {tried} = {five}" 

if first == "x": 
        if second == "-":
            firststr = f"{first} {second} {tried} = {five}" 
            secondstr = f"x = {five} + {tried}"
            fourstr = f"{reshenie} {second} {tried} = {five}" 

if first == "x": 
        if second == "*":
            firststr = f"{first} {second} {tried} = {five}" 
            secondstr = f"x = {five} / {tried}"
            fourstr = f"{reshenie} {second} {tried} = {five}" 

if first == "x": 
        if second == ":":
            firststr = f"{first} {second} {tried} = {five}" 
            secondstr = f"x = {five} * {tried}"
            fourstr = f"{reshenie} {second} {tried} = {five}" 

if tried == "x": 
        if second == "+":
            firststr = f"{first} {second} {tried} = {five}" 
            secondstr = f"x = {five} - {first}"
            fourstr = f"{first} {second} {reshenie} = {five}"

if tried == "x": 
        if second == "-":
            firststr = f"{first} {second} {tried} = {five}" 
            secondstr = f"x = {first} - {five}"
            fourstr = f"{first} {second} {reshenie} = {five}"

if tried == "x": 
        if second == "*":
            firststr = f"{first} {second} {tried} = {five}" 
            secondstr = f"x = {first} / {five}"
            fourstr = f"{first} {second} {reshenie} = {five}"

if tried == "x": 
        if second == ":":
            firststr = f"{first} {second} {tried} = {five}" 
            secondstr = f"x = {five} / {first}"
            fourstr = f"{first} {second} {reshenie} = {five}"

fivestr = f"{five} = {five}"
#Escaping the equation
print(firststr)
print(secondstr) 
print(f"x = {reshenie}") 
print(fourstr)
print(fivestr)

input("Write any character to complete: ")