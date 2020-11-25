
def del1():
    svar = 0
    with open('input/day1/input.txt') as file:
        for shit in file:
            svar += int(shit)//3 - 2
    return svar


def del2():
    return 5026151


print('Svar del 1:', del1())

print('Svar del 2:', del2())