# 01
def multiply(a, b):
    return a * b

# 02
def greet(name):
    return f"გამარჯობა, {name}"

# 03
def sum_three(a, b, c):
    return a + b + c

# 04
def concatenate(a, b):
    return str(a) + str(b)

# 05
# replace() ანაცვლებს სტრინგის ნაწილს სხვა მნიშვნელობით
example1 = "hello world".replace("world", "python")
example2 = "banana".replace("a", "o")

# 06
# .upper() აბრუნებს სტრინგს დიდი ასოებით
upper1 = "hello".upper()
upper2 = "test123".upper()
# .lower() აბრუნებს სტრინგს პატარა ასოებით
lower1 = "HELLO".lower()
lower2 = "PyThOn".lower()

# 07
# find() პოულობს სიმბოლოს ან სიტყვას სტრინგში და აბრუნებს მის ინდექსს
find1 = "hello world".find("world")
find2 = "banana".find("n")

# 08
# capitalize() ამაღლებს პირველი სიმბოლოს დიდ ასოდ და დანარჩენს პატარა ასოებად აქცევს
cap1 = "python".capitalize()
cap2 = "hELLO".capitalize()

# 09
# swapcase() ცვლის დიდ ასოებს პატარა ასოებად და პირიქით
swap1 = "Python".swapcase()
swap2 = "hELLO wORLD".swapcase()
