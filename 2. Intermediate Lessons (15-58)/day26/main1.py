# Examples

numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

letters = "Gabriel"
new_list = [letter for letter in letters]
print(new_list)

new_list = [n*2 for n in range(1,5)]
print(new_list)

names = ['Gabriel', 'Gilson', 'Thiago', 'Marília', 'Maiana', 'Pedro']
m_names = [n.upper() for n in names if n.startswith('M') == True]
print(m_names)

   #  26.1

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n**2 for n in numbers]

print(squared_numbers)

    # 26.2

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [n for n in numbers if n % 2 == 0]

print(result)

   # 26.3

# ---------------------------------------------------------------------
# with open("day26-100daysofcode/file1.txt") as file_1:
#     numbers_file1 = [n.strip() for n in file_1.readlines()]
# with open("day26-100daysofcode/file2.txt") as file_2:
#     numbers_file2 = [n.strip() for n in file_2.readlines()]
# ---------------------------------------------------------------------
with open("day26/file1.txt") as file_1:
    numbers_file1 = [n for n in file_1.readlines()]
with open("day26/file2.txt") as file_2:
    numbers_file2 = [n for n in file_2.readlines()]

result = [int(number) for number in numbers_file1 if number in numbers_file2]
print(result)