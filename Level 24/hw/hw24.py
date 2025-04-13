#01
skip_nums = [15, 27, 67, 32, 99, 93]

for i in range(101):
    if i in skip_nums:
        continue
    print(i)

#02
i = 0
while True:
    print(i)
    i += 1
    if i == 23:
        break

#03
my_list = ["Gio", "Nika", "Ana", "Luka", "Tako"]
my_list.append("Elene")
my_list.append("Saba")
print(my_list)

#04
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])
