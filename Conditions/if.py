import time


for i in range(10):
    print('Iteration number ' + str(i + 1))
    time.sleep(1)

    j = 1
    while j != 10:
        if j == 5:
            print('NESTED: Iteration number ' + str(j))
        elif j == 4:
            print('NESTED: Iteration number ' + str(j))
        elif j == 3:
            print('NESTED: Iteration number ' + str(j))
        elif j == 2:
            print('NESTED: Iteration number ' + str(j))
        elif j == 1:
            print('NESTED: Iteration number ' + str(j))
        else:
            print('Not checked!')
        j += 1
        time.sleep(.5)