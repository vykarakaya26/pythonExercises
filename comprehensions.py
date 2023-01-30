#List Compherension

#klasik yol-->

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

print(null_list)

# List Compherension yapısı ile -->

salaries = [1000, 2000, 3000, 4000, 5000]

null_list = []

[salary * 2 for salary in salaries if salary < 3000]

[new_salary(salary*2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 if salary < 3000 else salary for salary in salaries]


students = ['John', 'Mark', 'Venessa', 'Mariam']

students_no = ['John', 'Mariam']

[student.lower() if student in students_no else student.upper() for student in students]
#or
[student.upper() if student not in students_no else student.lower() for student in students]


# Dict Compherensions

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v ** 2 for (k, v) in dictionary.items()}