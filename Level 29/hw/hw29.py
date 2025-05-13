#01
def sum_odd(numbers):
    return sum(num for num in numbers if num % 2 == 1)

#02
def four_letters(names):
    return [name for name in names if len(name) == 4]

#03
def divisible_35(numbers):
    return [num for num in numbers if num % 3 == 0 and num % 5 == 0]

#04
# f-სტრინგი (formatted string) საშუალებას გვაძლევს ტექსტში ჩავსვათ ცვლადები მარტივად.
# სინტაქსი: f"ტექსტი {ცვლადი}"
name = "ანა"
age = 25
print(f"გამარჯობა, მე ვარ {name} და ვარ {age} წლის")
