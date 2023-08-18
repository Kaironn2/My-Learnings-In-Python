def count_hundred_for():
    for num in range(1, 101):
        print('for', num, end=' - ')


def count_hundred_while_true():
    count = 1
    while True:
        print('while True', count, end=' - ')
        count += 1

        if count == 100:
            break


def count_hundred_while():
    count = 1
    while count is not 101:
        print('while', count, end=' - ')
        count += 1


count_hundred_for()
print('\n\n')
count_hundred_while()
print('\n\n')
count_hundred_while_true()
