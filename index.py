import math

def is_power_of_three(number):
    if number > 0:
        power = math.log(number, 3)
    else:
        return False

    if power % 1 == 0:
        return True
    else:
        return False

# Проверка

number = 9

print(is_power_of_three(number))
