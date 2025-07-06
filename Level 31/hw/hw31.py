
#01
# სტრინგის ფუნქციები:
# lower() – გარდაქმნის სტრინგს პატარა ასოებად
# upper() – გარდაქმნის სტრინგს დიდ ასოებად
# capitalize() – მხოლოდ პირველი ასოს დიდ ასოდ გადაქცევა
# replace() – ცვლის ერთ მნიშვნელობას მეორეთი
# split() – ყოფს სტრინგს
# find() – პოულობს სიმბოლოს პოზიციას სტრინგში
# count() – ითვლის რამდენჯერ ჩნდება სიმბოლო ან სიტყვა სტრინგში

# სიის ფუნქციები:
# append() – ამატებს ელემენტს სიის ბოლოში
# pop() – შლის ელემენტს მითითებული ინდექსით
# remove() – შლის მითითებულ მნიშვნელობას სიიდან
# insert() – ამატებს ელემენტს კონკრეტულ ინდექსზე
# index() – პოულობს ელემენტის ინდექსს სიაში
# sort() – ალაგებს სიას ზრდადობით
# reverse() – აბრუნებს სიის ელემენტების მიმდევრობას
# clear() – ცარიელებს სიას

#02
my_surname = "manguashvili"
user_surname = input("machavariani")

if my_surname.lower() == user_surname.lower():
    print("Our surnames are similar.")
else:
    print("We have different surnames.")
	
#03
food = ["burger", "pizza", "fries", "chips"]
food.pop(2)
food.append("broccoli")
food.pop(2)
food.append("apple")

print(food)

#04
my_name = "nika"
user_name = "david"

if my_name[0].lower() == user_name[0].lower() and my_name[-1].lower() == user_name[-1].lower():
    print(2)
elif my_name[0].lower() == user_name[0].lower() or my_name[-1].lower() == user_name[-1].lower():
    print(1)
else:
    print(0)

#BOSS
names = []

while True:
    name_input = "stop"
    if name_input.lower() == 'stop':
        break
    capitalized_name = name_input.capitalize()
    names.append(capitalized_name)
    print(names)
