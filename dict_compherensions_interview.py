#Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek isteniyor
#key'ler orjinal value'lar değiştirilmiş değerler olacak

numbers = range(20)

new_dict = {}

for number in numbers:
    if number % 2 == 0:
        new_dict[number] = number ** 2
    else:
        continue

#dict compherensions

{number: number ** 2 for number in numbers if number % 2 == 0}