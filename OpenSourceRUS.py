#Выбор слогаемых / Selected components
first = input("Первое число (число или x): ") 
second = input("Действие (+ - * :): ") 
tried = input("Второе число (число или x): ") 
five = input("Чему равно: ") 
#Перевод уравнения в формат цифр и знаков из текста / Converting an equation to the format of numbers and signs from the text
try: 
    first = float(first) 
except ValueError: 
    pass 
try: 
    tried = float(tried) 
except ValueError: 
    pass 
five = float(five) 
#Вычисление неизвестного / Math operation
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
#Экранирование второй части уравнение / Escaping the second part of the equation
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
#Экранирование уравнения / Escaping the equation
print(firststr)
print(secondstr) 
print(f"x = {reshenie}") 
print(fourstr)
print(fivestr)

input("Напишите любой символ для завершения: ")